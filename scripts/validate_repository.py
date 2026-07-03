from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "SKILL.md",
    "README.md",
    "docs/GENERATED_OUTPUT.md",
    "references/question-policy.md",
    "references/skill-decomposition.md",
    "references/rule-resolution.md",
    "references/permission-policy.md",
    "references/project-bootstrap-policy.md",
    "references/validation-policy.md",
    "templates/agent-spec-template.md",
    "templates/project-profile.md",
    "templates/project-rules.md",
    "templates/project-setup-plan.md",
    "templates/project-readiness-report.md",
    "templates/skill-spec-template.md",
    "templates/platforms/claude-agent.md",
    "templates/platforms/factory-droid.md",
    "docs/CLAUDE_CODE.md",
    "docs/FACTORY_DROID.md",
    "tests/scenarios.md",
    "tests/expected-results.md",
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
        "Completion Conditions",
        "Project Bootstrap Mode",
        "Operating Modes",
        ".agent/PROJECT.md",
        ".agent/ARCHITECTURE.md",
        ".agent/RULES.md",
        ".agent/WORKFLOW.md",
        ".agent-builder/<project-name>/setup-plan.md",
        "references/project-bootstrap-policy.md",
        ".agent-builder/<agent-name>/agent-scenarios.md",
        "파일을 생성할 수 없는 환경",
    ]:
        if phrase not in content:
            errors.append(f"SKILL.md is missing required content: {phrase}")

    completion_conditions = content.split("## Completion Conditions", 1)[-1]
    for phrase in [
        "대상 플랫폼의 실제 에이전트 파일이 생성되어 있다",
        "필요한 모든 하위 스킬 파일이 생성되어 있다",
        ".agent-builder/<agent-name>/agent-scenarios.md",
        ".agent-builder/<project-name>/setup-plan.md",
        "readiness-report.md",
        "경로별 완성본",
    ]:
        if phrase not in completion_conditions:
            errors.append(f"SKILL.md Completion Conditions is missing: {phrase}")

generated_output = ROOT / "docs/GENERATED_OUTPUT.md"
if generated_output.is_file():
    content = generated_output.read_text(encoding="utf-8")
    if "tests/agent-scenarios.md" in content:
        errors.append("docs/GENERATED_OUTPUT.md should not write generated scenarios into target tests/.")
    if ".agent-builder/" not in content:
        errors.append("docs/GENERATED_OUTPUT.md must document the generated scenario namespace.")
    for phrase in [
        ".agent/PROJECT.md",
        ".agent/ARCHITECTURE.md",
        ".agent/RULES.md",
        ".agent/WORKFLOW.md",
        "readiness-report.md",
    ]:
        if phrase not in content:
            errors.append(f"docs/GENERATED_OUTPUT.md is missing project bootstrap output: {phrase}")

template_heading_checks = {
    "templates/agent-spec-template.md": [
        r"(?m)^##\s+\d+\.\s+Purpose\s*$",
        r"(?m)^##\s+\d+\.\s+Tools and Permissions\s*$",
        r"(?m)^##\s+\d+\.\s+Validation Scenarios\s*$",
    ],
    "templates/skill-spec-template.md": [
        r"(?m)^##\s+Purpose\s*$",
        r"(?m)^##\s+Tools\s*$",
        r"(?m)^##\s+Validation Scenarios\s*$",
    ],
    "templates/project-profile.md": [
        r"(?m)^##\s+Purpose\s*$",
        r"(?m)^##\s+Technology Stack\s*$",
        r"(?m)^##\s+Unresolved Decisions\s*$",
    ],
    "templates/project-rules.md": [
        r"(?m)^##\s+Rule Priority\s*$",
        r"(?m)^##\s+Approval Required\s*$",
        r"(?m)^##\s+Prohibited By Default\s*$",
    ],
    "templates/project-setup-plan.md": [
        r"(?m)^##\s+Files To Create\s*$",
        r"(?m)^##\s+Agents To Create\s*$",
        r"(?m)^##\s+Validation Plan\s*$",
    ],
    "templates/project-readiness-report.md": [
        r"(?m)^##\s+Status\s*$",
        r"(?m)^##\s+Generated Project Knowledge\s*$",
        r"(?m)^##\s+Approval-Required Follow-Up\s*$",
    ],
}

for relative, heading_patterns in template_heading_checks.items():
    path = ROOT / relative
    if path.is_file():
        content = path.read_text(encoding="utf-8")
        for pattern in heading_patterns:
            if not re.search(pattern, content):
                errors.append(f"{relative} is missing required heading pattern: {pattern}")

for relative in [
    "templates/platforms/claude-agent.md",
    "templates/platforms/factory-droid.md",
]:
    path = ROOT / relative
    if path.is_file():
        content = path.read_text(encoding="utf-8")
        for phrase in [
            "name:",
            "description:",
            "model:",
            "tools:",
            "# Completion Report",
        ]:
            if phrase not in content:
                errors.append(f"{relative} is missing required content: {phrase}")

bootstrap_policy = ROOT / "references/project-bootstrap-policy.md"
if bootstrap_policy.is_file():
    content = bootstrap_policy.read_text(encoding="utf-8")
    for phrase in [
        "Allowed by default",
        "Approval required",
        "Prohibited by default",
        ".agent/PROJECT.md",
        ".agent-builder/<project-name>/readiness-report.md",
    ]:
        if phrase not in content:
            errors.append(f"references/project-bootstrap-policy.md is missing required content: {phrase}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
print(f"Repository root: {ROOT}")
print(f"Required files checked: {len(REQUIRED)}")
