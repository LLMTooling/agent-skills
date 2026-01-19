Update skills index command

You must update the main README.md with any newly added skills. Follow these steps exactly:

## Step 1: Regenerate skills README
Run the Python script to regenerate the skills folder README.md:
```bash
cd skills && python generate_readme.py
```
Run this from the repository root directory. The script must be run from within the skills/ directory to properly find the .skill files.

## Step 2: Read both READMEs
Read the following files in parallel:
1. `skills/README.md` - the newly generated skills index
2. `README.md` - the main repository README

## Step 3: Identify new skills
Compare the two files and identify any skills present in `skills/README.md` but NOT yet listed in the main `README.md`.

## Step 4: Update main README.md
Update the main README.md by adding new skills to the appropriate category section:
- "Development & Frameworks" - for framework and language skills
- "Utilities & Tools" - for utility/helper skills
- "Migration" - for migration-related skills

Choose the most appropriate category based on the skill's purpose. Follow the existing format:
```
*   **skill-name**: Brief description of what the skill does.
```
Keep skills alphabetically sorted within each category.

## Step 5: Output new skills table
After updating, output a clean ASCII table showing only the newly added skills:

```
+------------------+--------------------------------------------------+
| New Skill        | Description                                      |
+------------------+--------------------------------------------------+
| skill-name       | Brief description                                |
+------------------+--------------------------------------------------+
```

If no new skills were found, output: "No new skills to add."
