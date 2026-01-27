List all available skills in the repository

You must output a clean ASCII table showing all skills in the skills folder.

## Get the list of skills

Use Glob to find all .skill files:
```
skills/**/*.skill
```

## Extract skill names

Extract just the filename (without path and .skill extension) from each result.

## Output ASCII table

Format the output as a clean ASCII table with two columns:

```
+------------------------+--------------------------------------------------------------+
| Skill Name             | Description                                                  |
+------------------------+--------------------------------------------------------------+
| astro-build           | Build and deployment documentation for Astro framework       |
| ...                   | ...                                                          |
+------------------------+--------------------------------------------------------------+
```

For the Description column:
- Read the first few lines of each .skill file to extract its purpose/description
- If a description isn't readily available, use a brief summary based on the skill name
- Keep descriptions concise (under 50 characters when possible, wrap to next line if longer)

## Sort the table

Sort skills alphabetically by skill name for easier reading.
