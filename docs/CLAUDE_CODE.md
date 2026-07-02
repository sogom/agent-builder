# Claude Code 사용 가이드

## 설치 위치

Claude Code의 프로젝트 스킬 위치:

```text
<project>/.claude/skills/agent-builder/SKILL.md
```

개인 전역 설치 위치:

```text
~/.claude/skills/agent-builder/SKILL.md
```

프로젝트마다 다른 코드와 규약을 분석해 에이전트를 생성하려면 프로젝트 설치를 권장합니다.

## Git submodule 설치

대상 프로젝트 루트에서:

```bash
git submodule add <REPOSITORY_URL> .claude/skills/agent-builder
git submodule update --init --recursive
```

업데이트:

```bash
git submodule update --remote .claude/skills/agent-builder
```

## 일반 복사 설치

```bash
mkdir -p .claude/skills
cp -R /path/to/agent-builder .claude/skills/agent-builder
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Copy-Item -Recurse -Force C:\path\to\agent-builder .claude\skills\agent-builder
```

## 확인

Claude Code에서 다음을 실행합니다.

```text
What skills are available?
```

또는 `/` 메뉴에서 `agent-builder`를 확인합니다.

스킬 디렉터리 이름이 호출 이름이므로 직접 호출은 다음과 같습니다.

```text
/agent-builder
```

## 사용 예시

```text
/agent-builder 이 프로젝트에서 실제 파일을 수정하는 프론트엔드 전문가 에이전트를 만들어줘.
```

```text
/agent-builder Git diff를 읽고 보안과 회귀 위험을 검토하는 읽기 전용 코드 리뷰 에이전트를 만들어줘.
```

```text
/agent-builder 백엔드 API 설계와 구현을 담당하지만 DB 마이그레이션은 승인받도록 하는 에이전트를 만들어줘.
```

## 생성 결과

Claude Code 프로젝트 에이전트는 다음 위치에 생성됩니다.

```text
<project>/.claude/agents/<agent-name>.md
```

필요한 하위 스킬은 다음 위치에 생성됩니다.

```text
<project>/.claude/skills/<skill-name>/SKILL.md
```

예시:

```text
.claude/
├── agents/
│   └── frontend-expert.md
└── skills/
    ├── agent-builder/
    ├── project-rule-discovery/
    ├── ui-architecture/
    └── component-implementation/
```

## Claude 에이전트 파일 형태

```markdown
---
name: frontend-expert
description: 기존 프론트엔드 프로젝트의 규약을 따라 UI 기능을 설계하고 구현할 때 사용한다.
model: inherit
tools: Read, Grep, Glob, Edit, Write, Bash
skills:
  - project-rule-discovery
  - ui-architecture
  - component-implementation
---

당신은 이 프로젝트의 프론트엔드 전문가다.

작업 전에 프로젝트 규약과 기존 구현 패턴을 확인한다.
...
```

`skills`에 나열한 스킬은 서브에이전트 시작 시 전체 내용이 미리 로드됩니다.

## 프로젝트 지침과 함께 사용

프로젝트 루트에 `CLAUDE.md`가 있다면 에이전트 생성 규칙을 추가할 수 있습니다.

```markdown
# Agent Generation

- 에이전트 생성 요청에는 `agent-builder` 스킬을 사용한다.
- 프로젝트 에이전트는 `.claude/agents/`에 생성한다.
- 프로젝트 스킬은 `.claude/skills/`에 생성한다.
- 생성 전에 현재 프로젝트 규약과 기술 스택을 탐색한다.
```

## 문제 해결

### 스킬이 보이지 않음

- 경로가 `.claude/skills/agent-builder/SKILL.md`인지 확인합니다.
- `SKILL.md`의 YAML frontmatter 문법을 확인합니다.
- Claude Code에서 `/doctor`를 실행합니다.
- 직접 `/agent-builder`로 호출합니다.

### 자동 호출이 되지 않음

`SKILL.md`의 `description`에 “에이전트 생성”, “서브에이전트”, “프로젝트 전용 에이전트” 같은 실제 요청 표현이 포함되어 있는지 확인합니다.

### 생성된 에이전트가 스킬을 사용하지 않음

- 에이전트 frontmatter의 `skills` 항목을 확인합니다.
- 해당 스킬이 `.claude/skills/<name>/SKILL.md`에 있는지 확인합니다.
- 에이전트 `tools`에 필요한 도구가 허용되어 있는지 확인합니다.
