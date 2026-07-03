# Codex 사용 가이드

## 설치 위치

프로젝트별 설치 위치:

```text
<project>/.agents/skills/agent-builder/SKILL.md
```

개인 전역 설치 위치:

```text
~/.agents/skills/agent-builder/SKILL.md
```

다른 프로젝트의 코드와 규약을 분석해 에이전트 설계를 만들려면 프로젝트별 설치를 권장합니다. 여러 프로젝트에서 같은 `agent-builder`를 계속 쓰려면 개인 전역 설치가 편합니다.

## Git submodule 설치

대상 프로젝트 루트에서:

```bash
git submodule add <REPOSITORY_URL> .agents/skills/agent-builder
git submodule update --init --recursive
```

업데이트:

```bash
git submodule update --remote .agents/skills/agent-builder
```

## 일반 복사 설치

macOS/Linux/WSL:

```bash
mkdir -p .agents/skills
cp -R /path/to/agent-builder .agents/skills/agent-builder
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse -Force C:\path\to\agent-builder .agents\skills\agent-builder
```

설치 후 새 Codex 세션을 시작합니다. 이미 열린 세션에서 스킬이 보이지 않으면 Codex를 다시 시작합니다.

## 사용 예시

명시적 호출:

```text
$agent-builder 이 프로젝트의 프론트엔드 전문가 에이전트를 만들어줘.
```

자연어 호출:

```text
이 프로젝트 규약을 따르는 코드 리뷰 에이전트와 필요한 하위 스킬을 설계해줘.
```

새 프로젝트 초기화:

```text
$agent-builder Go Fiber, Next.js, PostgreSQL 프로젝트를 AI가 일할 수 있게 세팅해줘.
```

## Codex에서의 역할

Codex는 `.agents/skills/<skill-name>/SKILL.md` 경로의 스킬을 읽어 작업 흐름을 확장합니다. 이 저장소를 Codex에 설치하면 Codex가 `agent-builder` 스킬을 사용해 프로젝트 목적, 규칙, 하위 스킬 구조, 에이전트 명세와 검증 시나리오를 설계할 수 있습니다.

현재 이 저장소의 생성 대상은 주로 다음 플랫폼입니다.

- Claude Code: `.claude/agents/`, `.claude/skills/`
- Factory Droid: `.factory/droids/`, `.factory/skills/`
- 공통 프로젝트 문서: `.agent/`

즉 Codex에서는 `agent-builder`를 실행 도구로 사용할 수 있지만, 생성되는 플랫폼별 에이전트 파일은 기본적으로 Claude Code와 Factory Droid 형식을 따릅니다. Codex 전용 산출물이 필요하면 요청에 다음처럼 명시합니다.

```text
$agent-builder Codex에서 사용할 AGENTS.md와 .agents/skills 구조 중심으로 만들어줘.
```

## 프로젝트 지침과 함께 사용

대상 프로젝트에 `AGENTS.md`가 있으면 Codex가 프로젝트 규칙으로 함께 읽습니다. `agent-builder`가 생성할 산출물의 경로와 정책을 고정하고 싶다면 프로젝트 루트의 `AGENTS.md`에 다음처럼 적어둡니다.

```md
# AGENTS.md

## Agent Builder

- 에이전트 생성 요청에는 `agent-builder` 스킬을 사용한다.
- Codex용 프로젝트 스킬은 `.agents/skills/`에 둔다.
- 공통 프로젝트 지식은 `.agent/`에 둔다.
- Claude Code 산출물은 명시 요청이 있을 때만 `.claude/`에 생성한다.
- Factory Droid 산출물은 명시 요청이 있을 때만 `.factory/`에 생성한다.
```

## 검증

스킬 파일이 올바른 위치에 있는지 확인합니다.

```text
.agents/skills/agent-builder/SKILL.md
```

Codex에서 다음처럼 물어봅니다.

```text
사용 가능한 스킬을 요약해줘.
```

또는 직접 호출합니다.

```text
$agent-builder 이 프로젝트에 필요한 AI 작업 환경을 점검해줘.
```

## 문제 해결

### 스킬이 보이지 않음

- 경로가 `.agents/skills/agent-builder/SKILL.md`인지 확인합니다.
- `SKILL.md` frontmatter에 `name: agent-builder`가 있는지 확인합니다.
- Codex를 새 세션으로 다시 시작합니다.

### 다른 프로젝트 규약을 읽지 못함

- Codex를 대상 프로젝트 루트에서 시작했는지 확인합니다.
- 대상 프로젝트에 `AGENTS.md`, README, 패키지 설정, 테스트 명령 문서가 있는지 확인합니다.
- 개인 전역 설치만 해둔 경우에도 작업은 반드시 분석하려는 프로젝트에서 실행합니다.

### Claude Code 또는 Factory 파일만 생성됨

현재 기본 산출물은 Claude Code와 Factory Droid 중심입니다. Codex용 산출물을 원하면 요청에 `.agents/skills`, `AGENTS.md`, `.agent/` 중심으로 생성하라고 명시합니다.
