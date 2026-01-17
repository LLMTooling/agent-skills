#!/usr/bin/env python3
"""
Generate README.md by scanning packaged .skill files (ZIP archives).

Scans the current directory for .skill files, reads them in-memory,
and creates an alphabetically sorted index.
"""

import os
import re
import zipfile
from pathlib import Path
from typing import Dict, List, Optional


def parse_yaml_frontmatter(content: str) -> Optional[Dict[str, str]]:
    """Extract YAML frontmatter from SKILL.md content."""
    # Match YAML frontmatter between --- delimiters
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None

    yaml_content = match.group(1)
    frontmatter = {}

    lines = yaml_content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('name:'):
            frontmatter['name'] = line.split(':', 1)[1].strip()
        elif line.strip().startswith('description:'):
            val = line.split(':', 1)[1].strip()
            if val == '|':
                # Multiline block
                desc_lines = []
                for j in range(i + 1, len(lines)):
                    next_line = lines[j]
                    # Stop if we hit a non-indented line that isn't empty
                    if next_line.strip() and not next_line.startswith(' '):
                        break
                    if next_line.strip():
                        desc_lines.append(next_line.strip())
                frontmatter['description'] = ' '.join(desc_lines)
            else:
                frontmatter['description'] = val

    return frontmatter


def analyze_zip_content(zip_path: Path) -> Optional[Dict[str, any]]:
    """Analyze a single .skill zip file."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            # Find SKILL.md (it might be inside a subdirectory if the zip preserved folder structure)
            # We look for */SKILL.md or SKILL.md
            skill_md_path = None
            file_list = z.namelist()
            
            for file in file_list:
                if file.endswith('SKILL.md'):
                    skill_md_path = file
                    break
            
            if not skill_md_path:
                print(f"Warning: Skipping {zip_path.name} - no SKILL.md found")
                return None

            # Read SKILL.md
            with z.open(skill_md_path) as f:
                content = f.read().decode('utf-8')
            
            frontmatter = parse_yaml_frontmatter(content)
            if not frontmatter or 'name' not in frontmatter:
                print(f"Warning: Skipping {zip_path.name} - invalid frontmatter")
                return None

            # Determine the root prefix (e.g., "my-skill/" if structure is my-skill/SKILL.md)
            root_prefix = os.path.dirname(skill_md_path)
            if root_prefix:
                root_prefix += '/'

            # Count references and scripts
            reference_count = 0
            script_counts = {}
            
            language_map = {
                '.py': 'Python',
                '.js': 'JavaScript',
                '.ts': 'TypeScript',
                '.go': 'Go',
                '.sh': 'Shell',
                '.bash': 'Bash',
                '.rb': 'Ruby',
                '.rs': 'Rust',
                '.java': 'Java',
                '.kt': 'Kotlin',
                '.swift': 'Swift',
                '.cpp': 'C++',
                '.c': 'C',
                '.cs': 'C#',
                '.php': 'PHP',
            }

            for file in file_list:
                # Ignore directories
                if file.endswith('/'):
                    continue
                
                # Normalize path relative to the skill root
                if root_prefix and file.startswith(root_prefix):
                    rel_path = file[len(root_prefix):]
                else:
                    rel_path = file

                # Count references
                if rel_path.startswith('references/'):
                    reference_count += 1
                
                # Count scripts (in scripts/ or assets/)
                if rel_path.startswith('scripts/') or rel_path.startswith('assets/'):
                    ext = os.path.splitext(file)[1].lower()
                    if ext in language_map:
                        lang = language_map[ext]
                        script_counts[lang] = script_counts.get(lang, 0) + 1

            return {
                'name': frontmatter['name'],
                'description': frontmatter.get('description', 'No description available'),
                'references': reference_count,
                'script_counts': script_counts
            }

    except zipfile.BadZipFile:
        print(f"Error: {zip_path.name} is not a valid zip file")
        return None
    except Exception as e:
        print(f"Error processing {zip_path.name}: {e}")
        return None


def generate_readme_md(skills: List[Dict[str, any]]) -> str:
    """Generate README.md content."""
    lines = [
        "# Agent Skills",
        "",
        f"This repository contains {len(skills)} skills available in this directory.",
        "",
        "## Skills",
        ""
    ]

    for skill in skills:
        lines.append(f"### {skill['name']}")
        lines.append("")
        lines.append(f"**Description:** {skill['description']}")
        lines.append("")

        # Add metadata line
        metadata_parts = []
        if skill['references'] > 0:
            ref_text = "reference" if skill['references'] == 1 else "references"
            metadata_parts.append(f"{skill['references']} {ref_text}")

        # Format script counts
        script_counts = skill['script_counts']
        if script_counts:
            total_scripts = sum(script_counts.values())
            script_text = "script" if total_scripts == 1 else "scripts"

            # Build language breakdown
            if len(script_counts) == 1:
                # Single language: "3 Python scripts"
                lang, count = list(script_counts.items())[0]
                metadata_parts.append(f"{count} {lang} {script_text}")
            else:
                # Multiple languages: "5 scripts (3 Python, 2 Go)"
                lang_parts = [f"{count} {lang}" for lang, count in sorted(script_counts.items())]
                metadata_parts.append(f"{total_scripts} {script_text} ({', '.join(lang_parts)})")

        if metadata_parts:
            lines.append(f"**Resources:** {' • '.join(metadata_parts)}")
            lines.append("")

    return '\n'.join(lines)


def main():
    """Main entry point."""
    current_dir = Path('.')
    output_file = current_dir / 'README.md'
    
    print(f"Scanning .skill files in: {current_dir.absolute()}")
    
    skills = []
    for skill_file in sorted(current_dir.glob('*.skill')):
        skill_data = analyze_zip_content(skill_file)
        if skill_data:
            skills.append(skill_data)

    if not skills:
        print("No valid .skill files found.")
        return 1

    # Sort alphabetically by name
    skills.sort(key=lambda x: x['name'].lower())

    print(f"Found {len(skills)} valid skills")
    print(f"Generating README.md...")
    
    readme_content = generate_readme_md(skills)
    output_file.write_text(readme_content, encoding='utf-8')
    
    print(f"Successfully wrote README.md to: {output_file}")
    return 0


if __name__ == '__main__':
    exit(main())