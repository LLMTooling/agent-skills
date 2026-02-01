# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a curated collection of **Agent Skills** - specialized packages that extend AI agent capabilities (Claude Code, Gemini CLI, etc.). Each skill is a `.skill` file (zip archive) containing documentation, scripts, and resources for specific technologies or workflows.

### Directory Structure

```
agent-skills/
├── skills/                 # All packaged .skill files
│   ├── category-name/      # Skills organized by category
│   │   └── skill-name.skill
├── scripts/                # Maintenance and packaging scripts
└── README.md               # Published skill catalog
```

## Skill Packaging Workflow

### Critical: Packaging Must Follow Correct Structure

**Always package skills from the source skill FOLDER, not by manipulating .skill files directly.** The `.skill` file must have this exact structure:

```
skill-name.skill (zip archive)
├── SKILL.md               # MUST be at root level
├── references/            # Optional: at root level
└── scripts/               # Optional: at root level
```

**COMMON MISTAKE TO AVOID**: Do NOT create a nested folder structure like:
```
skill-name.skill
└── skill-name/            # WRONG! This breaks the skill
    ├── SKILL.md
    └── references/
```

### When Asked to Package a Skill

1. **Navigate to the skills directory** before packaging:
   ```bash
   cd skills/<category-name>
   python ../../scripts/package_skill.py <skill-folder-name>
   ```

2. **The script automatically**:
   - Validates SKILL.md frontmatter (YAML format, required fields)
   - Creates the .skill file in the current directory
   - Ensures SKILL.md is at root level (not nested)

3. **Verify the package** after creation:
   ```bash
   python ../../scripts/audit_skills.py              # Structural check
   python ../../scripts/audit_skill_integrity.py     # Filename sanity check
   ```

### When Asked to Commit Changes

**Always run the full audit suite before committing:**

```bash
# From repository root
python scripts/audit_skills.py
python scripts/audit_skill_integrity.py
```

Both must pass (exit 0) before proceeding with the commit. This catches:
- Nested folder structures (most common packaging error)
- Corrupted filenames from improper operations
- Missing SKILL.md at root level

## Validation Requirements (SKILL.md Frontmatter)

Every skill's SKILL.md must have valid YAML frontmatter with these rules:

```yaml
---
name: skill-name                    # Required: hyphen-case, max 64 chars
description: Skill description      # Required: no < > brackets, max 1024 chars
license: MIT                        # Optional
allowed-tools: []                   # Optional: list of tools
metadata:                           # Optional: custom key-values
  custom-key: value
---
```

**Validation rules:**
- `name`: hyphen-case (lowercase, digits, hyphens), no leading/trailing/consecutive hyphens
- `description`: no angle brackets allowed
- Only allowed properties: `name`, `description`, `license`, `allowed-tools`, `metadata`

## Local Maintenance Scripts (gitignored)

The `scripts/` folder is **gitignored** but available locally for maintenance. It contains utility scripts for skill development and validation:

### Available Scripts

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `package_skill.py <folder>` | Package a skill folder into .skill file | After creating or modifying a skill - run from the category directory |
| `quick_validate.py <folder>` | Validate SKILL.md frontmatter | Before packaging to check YAML syntax and required fields |
| `audit_skills.py` | Check all .skill files for correct structure | Before committing - ensures SKILL.md and references/ are at root level |
| `audit_skill_integrity.py` | Check for filename corruption | Before committing - detects broken characters or suspicious patterns |
| `fix_skill_packaging.py [--dry-run]` | Auto-fix nested folder packaging issues | When audit fails - removes nested folder structure from .skill files |
| `init_skill.py` | Initialize a new skill from template | When creating a brand new skill from scratch |

### Detailed Usage

#### `package_skill.py <folder-name>`
**Run from:** `skills/<category>/` directory
**Purpose:** Creates a `.skill` file from a skill folder
```bash
cd skills/animation-graphics
python ../../scripts/package_skill.py gsap
```
Validates SKILL.md frontmatter, creates zip with correct structure (SKILL.md at root, no nested folders).

#### `quick_validate.py <folder-name>`
**Run from:** Any directory
**Purpose:** Check SKILL.md frontmatter before packaging
```bash
python scripts/quick_validate.py skills/animation-graphics/gsap
```
Checks: YAML syntax, required fields (name, description), hyphen-case naming, description length limits.

#### `audit_skills.py`
**Run from:** Repository root
**Purpose:** Validate all .skill files have correct structure
```bash
python scripts/audit_skills.py
```
Checks that SKILL.md and references/ are at root level (not inside nested folder). Run before every commit.

#### `audit_skill_integrity.py`
**Run from:** Repository root
**Purpose:** Detect filename corruption in all .skill files
```bash
python scripts/audit_skill_integrity.py
```
Checks for: control characters, shell operators in filenames, unusual unicode, corrupted paths. Run before every commit.

#### `fix_skill_packaging.py [--dry-run] [path]`
**Run from:** Repository root
**Purpose:** Auto-fix incorrectly packaged .skill files
```bash
# Preview changes
python scripts/fix_skill_packaging.py --dry-run

# Fix all skills
python scripts/fix_skill_packaging.py

# Fix specific skill
python scripts/fix_skill_packaging.py skills/animation-graphics/gsap.skill
```
Creates backup (.skill.backup), removes nested folder prefix, verifies result, auto-rollback on failure.

#### `init_skill.py`
**Run from:** Any directory
**Purpose:** Create a new skill from template
```bash
python scripts/init_skill.py
```
Interactively prompts for skill details and creates folder with SKILL.md template.

### Fixing Corrupted Skills

If audit fails for a skill:
1. Try auto-fix: `python scripts/fix_skill_packaging.py <path-to-skill>`
2. The script creates backups (.skill.backup) before modifying
3. Verify with audit after fix
4. Only repackage from source if auto-fix fails

## Skill Categories (for reference)

When creating new skills, use appropriate categories:

- **ai-llm-integration**: LLM/AI framework integrations
- **animation-graphics**: Animation and graphics libraries
- **apis-services**: API integrations
- **astro**: Astro framework
- **angular**: Angular framework
- **backend-frameworks**: Server-side frameworks
- **build-tools**: Build tools and bundlers
- **code-quality**: Linting, formatting, best practices
- **design**: Design principles
- **editor-integration**: Editor/IDE extensions
- **electron**: Electron and related tools
- **expo**: Expo and React Native
- **go-dev**: Go development
- **iot-smart-home**: IoT and home automation
- **mcp**: Model Context Protocol (MCP)
- **migration-tools**: Migration guides
- **python-dev**: Python development tools
- **react-ecosystem**: React and ecosystem
- **rust-dev**: Rust development
- **styling**: CSS and styling frameworks
- **svelte**: Svelte framework
- **tauri**: Tauri framework
- **terminal-cli**: CLI and terminal tools
- **testing**: Testing frameworks
- **typescript-dev**: TypeScript development
- **utilities**: General utilities
