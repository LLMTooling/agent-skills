# Agent Skills

## Project Overview
This repository contains a curated collection of **Agent Skills**—specialized packages designed to extend the capabilities of AI agents. Each skill encapsulates specific knowledge, workflows, or tools (e.g., web scraping, framework-specific coding standards).

For more details, refer to the official documentation:
*   [Agent Skills Home (Universal Standard)](https://agentskills.io/home)
*   [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
*   [OpenAI Codex Skills Docs](https://developers.openai.com/codex/skills/)

## Universal Open Source Format (agentskills.io)
When creating new skills, always follow the **Universal Open Source** format to ensure interoperability.

### Structure
An Agent Skill is a directory (or a ZIP archive of that directory, typically named `.skill`) containing:
1.  **`SKILL.md`** (Required): The core instruction file with YAML frontmatter.
2.  **`scripts/`** (Optional): executable scripts (Python, JS, Bash, etc.) the skill can invoke.
3.  **`references/`** (Optional): Detailed documentation or large text files (e.g., API docs) to be loaded on demand (progressive disclosure).
4.  **`assets/`** (Optional): Static resources like templates.

### SKILL.md Format
The `SKILL.md` file is the entry point. It **must** start with YAML frontmatter.

```markdown
---
name: my-universal-skill
description: A concise description of what the skill does. Used by the agent to decide WHEN to use this skill.
---
# My Universal Skill

## Purpose
Detailed explanation of the task.

## Instructions
Step-by-step procedures the agent should follow.
```

## Platform-Specific Implementation

While the core format is universal, specific platforms have unique capabilities and metadata fields.

### Claude Code (Anthropic)
*   **Locations**:
    *   Global: `~/.claude/skills/`
    *   Project: `.claude/skills/` (shared with team)
    *   Plugins: `skills/` directory inside a plugin.
*   **Specific Metadata (`SKILL.md`)**:
    *   `allowed-tools`: List of tools (e.g., `Bash`, `Repl`) the skill can use without explicit permission.
    *   `context: fork`: Runs the skill in an isolated sub-agent (sandbox) to prevent context pollution.
    *   `hooks`: Define `PreToolUse`, `PostToolUse`, or `Stop` event handlers.
    *   `user-invocable`: boolean (default `true`), whether it appears in the slash command menu.
*   **Best Practices**:
    *   Use **Progressive Disclosure**: Keep `SKILL.md` lightweight. Put heavy documentation in `references/` and link to them. Claude will read them only if needed.

### OpenAI Codex (ChatGPT/OpenAI)
*   **Locations**:
    *   Project: `.codex/skills/`
    *   User: `~/.codex/skills/`
    *   System: `/etc/codex/skills/`
*   **Invocation**:
    *   **Implicit**: The model decides to use the skill based on the `description` in frontmatter.
    *   **Explicit**: User invokes via `/skills` or `$` commands.
*   **Specific Metadata**:
    *   `short-description`: A user-facing summary (optional) in the `metadata` block.

## Repository Structure

*   **`skills/`**: The core directory containing the packaged skills.
    *   **`*.skill` files**: These are the actual skill packages (ZIP archives of the skill directory).
    *   **`generate_readme.py`**: A Python script that scans all `.skill` files and auto-generates the `README.md`.

## Development Workflow

1.  **Drafting**: Create a directory (e.g., `my-skill/`) and draft your `SKILL.md`.
2.  **Scripting**: Add necessary scripts to `scripts/`.
3.  **Testing**:
    *   For **Claude**: Place the directory in `~/.claude/skills/` and test with `claude`.
    *   For **Codex**: Place in `.codex/skills/` and test interactions.
4.  **Packaging**:
    *   **Cleanup**: Delete any unused directories (e.g., `references/` or `assets/` if they are empty) before packaging.
    *   Zip the *contents* of your skill directory (ensure `SKILL.md` is at the root of the zip).
    *   Rename `.zip` to `.skill`.
    *   Move to `skills/` in this repository.
5.  **Documentation**: Run `python skills/generate_readme.py` to update the main README.