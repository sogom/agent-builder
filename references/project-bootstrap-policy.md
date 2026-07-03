# Project Bootstrap Policy

Use this reference when Agent Builder is asked to initialize a new project, create an AI-ready workspace, or generate project rules, skills, and agents together.

## Goal

Project Bootstrap Mode prepares a project so AI agents can work consistently. It creates shared project knowledge first, then derives reusable skills and platform-specific agents from that knowledge.

## Default Output Layers

### Shared project knowledge

Create these files when the mode is active:

```text
.agent/PROJECT.md
.agent/ARCHITECTURE.md
.agent/RULES.md
.agent/WORKFLOW.md
```

These files are runtime-neutral. Claude Code, Factory Droid, Codex, and other agents should be able to read them as project context.

### Platform artifacts

Create platform artifacts only for requested or detected platforms:

```text
.claude/agents/<agent-name>.md
.claude/skills/<skill-name>/SKILL.md
.factory/droids/<agent-name>.md
.factory/skills/<skill-name>/SKILL.md
```

### Builder artifacts

Record setup decisions, verification, and unresolved items here:

```text
.agent-builder/<project-name>/setup-plan.md
.agent-builder/<project-name>/readiness-report.md
.agent-builder/<project-name>/agent-scenarios.md
```

## Question Policy

Ask only when the answer materially affects project structure, architecture, permissions, security, or external cost. Do not ask about names, file ordering, Markdown format, or choices with safe defaults.

Prefer these defaults when absent:

- Architecture style: simple modular structure before DDD or hexagonal architecture.
- Testing: unit tests for core logic and integration tests for boundaries.
- Documentation: concise project rules and workflow docs under `.agent/`.
- Agent set: reviewer plus role agents only when the project scope supports them.
- Permissions: read/write project files, approval for package install, CI, deployment, database, auth, and external writes.

## Approval Boundaries

Allowed by default:

- Generate `.agent/` knowledge files.
- Generate `.agent-builder/` setup and validation files.
- Generate platform agent and skill files.
- Generate draft config files if explicitly requested and clearly marked as drafts.

Approval required:

- Install packages.
- Generate or regenerate lock files.
- Create full application scaffold.
- Add CI/CD workflows.
- Configure databases, auth, deployment, cloud resources, or external services.
- Modify an existing project structure.

Prohibited by default:

- Production deployment.
- Persisting real secrets.
- External write operations.
- Destructive changes.

## Completion Requirements

Do not complete Project Bootstrap Mode until:

- Shared project knowledge files exist or are provided as path-labeled code blocks.
- Platform agent and skill files exist when a platform target is selected.
- Setup plan and readiness report exist.
- Validation scenarios exist.
- Assumptions, unresolved decisions, approval-required follow-up, and limitations are reported.
