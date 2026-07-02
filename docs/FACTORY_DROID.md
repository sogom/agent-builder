# Factory Droid 사용 가이드

## 설치 위치

Factory Droid의 프로젝트 스킬 위치:

```text
<project>/.factory/skills/agent-builder/SKILL.md
```

개인 전역 설치 위치:

```text
~/.factory/skills/agent-builder/SKILL.md
```

Factory는 호환 경로인 `<project>/.agent/skills/`도 탐색하지만, 명확한 프로젝트 구성을 위해 `.factory/skills/` 사용을 권장합니다.

## Git submodule 설치

대상 프로젝트 루트에서:

```bash
git submodule add <REPOSITORY_URL> .factory/skills/agent-builder
git submodule update --init --recursive
```

업데이트:

```bash
git submodule update --remote .factory/skills/agent-builder
```

## 일반 복사 설치

```bash
mkdir -p .factory/skills
cp -R /path/to/agent-builder .factory/skills/agent-builder
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force .factory\skills | Out-Null
Copy-Item -Recurse -Force C:\path\to\agent-builder .factory\skills\agent-builder
```

설치 후 Droid 또는 IDE 통합을 다시 시작해 스킬을 재탐색합니다.

## 사용 예시

```text
/agent-builder 이 프로젝트의 프론트엔드 작업을 담당하는 Custom Droid를 만들어줘.
```

```text
/agent-builder 소스와 diff를 읽기만 하는 코드 리뷰 Droid를 만들어줘.
```

```text
/agent-builder 프로젝트의 Go API를 구현하고 테스트하지만 운영 배포는 하지 않는 Droid를 만들어줘.
```

자연어로 요청해도 description과 일치하면 Droid가 자동으로 스킬을 선택할 수 있습니다.

## 생성 결과

Factory 프로젝트 Custom Droid는 다음 위치에 생성됩니다.

```text
<project>/.factory/droids/<agent-name>.md
```

하위 스킬은 다음 위치에 생성됩니다.

```text
<project>/.factory/skills/<skill-name>/SKILL.md
```

예시:

```text
.factory/
├── droids/
│   └── frontend-expert.md
└── skills/
    ├── agent-builder/
    ├── project-rule-discovery/
    ├── ui-architecture/
    └── component-implementation/
```

Custom Droid 파일은 `.factory/droids/`의 최상위에 둡니다.

## Custom Droid 파일 형태

```markdown
---
name: frontend-expert
description: 기존 프로젝트 규약을 따라 프론트엔드 UI를 설계하고 구현한다.
model: inherit
tools: ["Read", "Grep", "Glob", "Edit", "Write", "Execute"]
---

당신은 이 프로젝트의 프론트엔드 전문가다.

작업 전에 프로젝트 규약과 기존 구현 패턴을 확인한다.
...
```

Factory 환경의 실제 도구 ID는 설치 버전과 설정에 따라 다를 수 있으므로 생성 후 `/droids`에서 검증합니다. 간단한 읽기 전용 Droid는 `tools: read-only`를 사용할 수 있습니다.

## 프로젝트 지침과 함께 사용

프로젝트 루트의 `AGENTS.md`에 다음을 추가할 수 있습니다.

```markdown
# Agent Generation

- 에이전트 생성 요청에는 `agent-builder` 스킬을 사용한다.
- 프로젝트 Custom Droid는 `.factory/droids/`에 생성한다.
- 프로젝트 스킬은 `.factory/skills/`에 생성한다.
- 생성 전에 현재 프로젝트 규약과 기술 스택을 탐색한다.
```

## 확인

Droid에서:

```text
/settings
```

Custom Droids가 활성화되어 있는지 확인합니다.

```text
/droids
```

생성된 Droid를 확인하고 도구 목록을 검증합니다.

## Claude Code 에이전트 가져오기

Factory의 `/droids` 메뉴는 Claude Code의 개인 에이전트 가져오기를 지원할 수 있습니다. 다만 도구 이름 매핑이 완전히 일치하지 않을 수 있으므로 가져온 뒤 model과 tools를 검토합니다.

두 플랫폼을 프로젝트에서 동시에 사용한다면 `agent-builder`에 “두 플랫폼용으로 생성해줘”라고 요청하는 방식이 더 명확합니다.

## 문제 해결

### 스킬이 보이지 않음

- 경로가 `.factory/skills/agent-builder/SKILL.md`인지 확인합니다.
- Droid를 다시 시작합니다.
- YAML frontmatter의 `name`이 소문자, 숫자, 하이픈 형식인지 확인합니다.

### Custom Droid가 보이지 않음

- 파일이 `.factory/droids/` 바로 아래에 있는지 확인합니다.
- `/droids` 메뉴를 다시 엽니다.
- `name`, `description`, `model`, `tools` frontmatter를 확인합니다.

### 도구 검증 오류

Factory에서 지원하는 도구 ID로 변경하거나 `tools: read-only` 같은 카테고리를 사용합니다.
