# 생성 결과 구조

## Project Bootstrap Mode 공통 산출물

```text
target-project/
├── .agent/
│   ├── PROJECT.md
│   ├── ARCHITECTURE.md
│   ├── RULES.md
│   └── WORKFLOW.md
└── .agent-builder/
    └── <project-name>/
        ├── setup-plan.md
        ├── readiness-report.md
        └── agent-scenarios.md
```

`.agent/`는 여러 에이전트 런타임이 함께 읽는 프로젝트 지식입니다. `.agent-builder/`는 생성 과정의 계획, 검증과 미확정 사항을 기록합니다.

명시 경로:

- `.agent/PROJECT.md`
- `.agent/ARCHITECTURE.md`
- `.agent/RULES.md`
- `.agent/WORKFLOW.md`
- `.agent-builder/<project-name>/setup-plan.md`
- `.agent-builder/<project-name>/readiness-report.md`
- `.agent-builder/<project-name>/agent-scenarios.md`

## Claude Code 단일 대상

```text
target-project/
├── CLAUDE.md
├── .claude/
│   ├── agents/
│   │   └── <agent-name>.md
│   └── skills/
│       ├── agent-builder/
│       └── <generated-skill>/
│           ├── SKILL.md
│           └── references/
└── .agent-builder/
    └── <agent-name>/
        └── agent-scenarios.md
```

## Factory Droid 단일 대상

```text
target-project/
├── AGENTS.md
├── .factory/
│   ├── droids/
│   │   └── <agent-name>.md
│   └── skills/
│       ├── agent-builder/
│       └── <generated-skill>/
│           ├── SKILL.md
│           └── references/
└── .agent-builder/
    └── <agent-name>/
        └── agent-scenarios.md
```

## 두 플랫폼 동시 대상

```text
target-project/
├── CLAUDE.md
├── AGENTS.md
├── .claude/
│   ├── agents/<agent-name>.md
│   └── skills/<generated-skill>/SKILL.md
├── .factory/
│   ├── droids/<agent-name>.md
│   └── skills/<generated-skill>/SKILL.md
└── .agent-builder/
    └── <agent-name>/
        └── agent-scenarios.md
```

## 공통 명세와 플랫폼 어댑터

두 플랫폼용 파일은 같은 프로젝트 요구사항 모델을 사용해야 합니다.

공통으로 유지할 내용:

- 목적
- 책임
- 범위 밖 업무
- 프로젝트 지식
- 성공 기준
- 프로젝트 규약
- 질문 정책
- 승인 정책
- 실패 처리

플랫폼별로 변환할 내용:

- 저장 경로
- YAML frontmatter
- 도구 이름
- 권한 표현
- 하위 스킬 preload 방식
- 호출 및 관리 UI

## 완료 보고

생성 후 다음을 보고합니다.

```markdown
## Generated Agent

- Platform:
- Agent file:
- Supporting skills:
- Project rule sources:
- Allowed actions:
- Approval-required actions:
- Validation performed:
- Limitations:
```
