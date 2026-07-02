from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "SKILL.md",
    "README.md",
    "references/question-policy.md",
    "references/skill-decomposition.md",
    "references/rule-resolution.md",
    "references/permission-policy.md",
    "references/validation-policy.md",
    "templates/agent-spec-template.md",
    "templates/skill-spec-template.md",
    "templates/platforms/claude-agent.md",
    "templates/platforms/factory-droid.md",
    "docs/CLAUDE_CODE.md",
    "docs/FACTORY_DROID.md",
]

errors = []

for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"Missing required file: {relative}")

skill = ROOT / "SKILL.md"
if skill.is_file():
    content = skill.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append("SKILL.md is missing YAML frontmatter.")
    if not re.search(r"(?m)^name:\s*agent-builder\s*$", content):
        errors.append("SKILL.md frontmatter must contain name: agent-builder.")
    if not re.search(r"(?m)^description:\s*.+$", content):
        errors.append("SKILL.md frontmatter must contain a description.")
    for phrase in [
        "Platform Target and Final Artifact Generation",
        ".claude/agents/",
        ".factory/droids/",
        "Completion Gate",
    ]:
        if phrase not in content:
            errors.append(f"SKILL.md is missing required content: {phrase}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
print(f"Repository root: {ROOT}")
print(f"Required files checked: {len(REQUIRED)}")
