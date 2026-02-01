Package a skill folder into a distributable .skill file

The user will provide a skill folder name as #$ ARGUMENTS.

## Step 1: Validate the skill

Run the quick_validate script to verify the skill is valid:
```
python scripts/quick_validate.py #$ ARGUMENTS
```

## Step 2: Handle validation results

If validation fails:
- Use AskUserQuestion tool to suggest remediation options
- Provide clear error messages from the validation
- Ask if the user wants to:
  1. Fix the issues manually (exit and let them fix)
  2. Attempt automatic fixes (if possible)
  3. Continue anyway (not recommended)

If validation passes:
- Proceed to packaging

## Step 3: Package the skill

Run the package_skill script to create the .skill file:
```
python scripts/package_skill.py #$ ARGUMENTS
```

The output will be at the workspace root (current working directory).

## Step 4: Report results

Inform the user of the final result:
- If successful: Show the path to the created .skill file
- If failed: Explain what went wrong
