# Agent Builder

Build AI-ready projects with reusable Agents and Skills.

`Agent Builder`는 프로젝트의 목적, 규약, 기술 스택과 사용 맥락을 분석해 **AI가 일관되게 작업할 수 있는 프로젝트 지식, 하위 스킬, 프로젝트 전용 에이전트**를 생성하는 메타 스킬입니다.

생성 결과는 단순 설계 문서가 아니라 다음과 같은 플랫폼용 파일입니다.

- 공통 프로젝트 지식: `.agent/PROJECT.md`, `.agent/ARCHITECTURE.md`, `.agent/RULES.md`
- Claude Code: `.claude/agents/<agent-name>.md`
- Factory Droid: `.factory/droids/<agent-name>.md`
- 에이전트가 사용할 하위 스킬: 각 플랫폼의 `skills/<skill-name>/SKILL.md`

## 지원 대상

- Claude Code project skills and subagents
- Factory Droid workspace skills and Custom Droids
- 두 플랫폼 동시 생성
- 새 프로젝트를 AI-ready workspace로 초기화하는 Project Bootstrap Mode
- 기존 프로젝트 분석 기반 AI workspace 생성은 향후 v3 범위

## 저장소 구성

```text
agent-builder/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── VERSION
├── docs/
│   ├── CLAUDE_CODE.md
│   ├── FACTORY_DROID.md
│   ├── GENERATED_OUTPUT.md
│   └── PUBLISHING.md
├── references/
├── templates/
│   ├── platforms/
│   └── ...
├── examples/
├── tests/
└── scripts/
    ├── install.sh
    ├── install.ps1
    └── validate_repository.py
```

## 빠른 설치

### Claude Code 프로젝트에 설치

대상 프로젝트 루트에서 저장소를 다음 위치로 복사하거나 Git submodule로 추가합니다.

```bash
git submodule add <REPOSITORY_URL> .claude/skills/agent-builder
```

Claude Code는 프로젝트 스킬을 `.claude/skills/<skill-name>/SKILL.md`에서 탐색합니다.

직접 호출:

```text
/agent-builder 이 프로젝트의 프론트엔드 전문가 에이전트를 만들어줘.
```

자연어 호출:

```text
이 프로젝트 규약을 따르면서 UI 구현을 전담하는 에이전트를 만들어줘.
```

자세한 내용: [`docs/CLAUDE_CODE.md`](docs/CLAUDE_CODE.md)

### Factory Droid 프로젝트에 설치

```bash
git submodule add <REPOSITORY_URL> .factory/skills/agent-builder
```

Factory Droid는 프로젝트 스킬을 `.factory/skills/<skill-name>/SKILL.md`에서 탐색합니다. 설치 후 Droid를 다시 시작해 스킬을 재탐색합니다.

직접 호출:

```text
/agent-builder 이 프로젝트의 코드 리뷰 Custom Droid를 만들어줘.
```

자세한 내용: [`docs/FACTORY_DROID.md`](docs/FACTORY_DROID.md)

### 설치 스크립트 사용

macOS/Linux/WSL:

```bash
./scripts/install.sh --target /path/to/project --platform both
```

Windows PowerShell:

```powershell
.\scripts\install.ps1 -Target C:\path\to\project -Platform both
```

`both` 대신 `claude` 또는 `factory`를 사용할 수 있습니다.

## 생성 예시

요청:

```text
기존 Next.js 프로젝트 규약을 지키면서 UI 설계와 코드 수정을 담당하는 프론트엔드 전문가 에이전트를 만들어줘.
```

Claude Code에서 예상 결과:

```text
.claude/
├── agents/
│   └── frontend-expert.md
└── skills/
    ├── project-rule-discovery/
    │   └── SKILL.md
    ├── ui-architecture/
    │   └── SKILL.md
    ├── component-implementation/
    │   └── SKILL.md
    └── test-validation/
        └── SKILL.md
```

Factory Droid에서 예상 결과:

```text
.factory/
├── droids/
│   └── frontend-expert.md
└── skills/
    ├── project-rule-discovery/
    │   └── SKILL.md
    ├── ui-architecture/
    │   └── SKILL.md
    ├── component-implementation/
    │   └── SKILL.md
    └── test-validation/
        └── SKILL.md
```

Project Bootstrap Mode에서 예상 결과:

```text
.agent/
├── PROJECT.md
├── ARCHITECTURE.md
├── RULES.md
└── WORKFLOW.md
.agent-builder/
└── company-system/
    ├── setup-plan.md
    ├── readiness-report.md
    └── agent-scenarios.md
```

## 동작 원칙

1. 현재 요청과 대화에서 이미 알려진 정보를 먼저 사용합니다.
2. 프로젝트 규약과 기술 스택을 파일에서 탐색합니다.
3. 새 프로젝트라면 목적, 스택, 아키텍처, 운영 제약을 정리해 AI-ready 프로젝트 문서를 생성합니다.
4. 구조, 권한, 안전에 큰 영향을 주는 정보만 질문합니다.
5. 에이전트가 최종 목표를 책임하고 하위 스킬은 반복 가능한 전문 절차를 담당합니다.
6. 최소 권한 원칙을 적용합니다.
7. 실제 플랫폼용 에이전트 파일과 하위 스킬 파일을 생성합니다.
8. 테스트 시나리오를 작성하고 결과를 검증합니다.

## 저장소 게시

개인 Git 저장소를 만든 뒤 [`docs/PUBLISHING.md`](docs/PUBLISHING.md)의 명령을 사용하면 됩니다.

## 검증

```bash
python scripts/validate_repository.py
```

## 주의

- 저장소 자체는 `agent-builder` 스킬 패키지입니다.
- 대상 프로젝트에 설치한 뒤 그 프로젝트 안에서 실행해야 프로젝트 규약을 제대로 분석할 수 있습니다.
- 생성된 에이전트의 도구와 권한은 적용 전에 검토하세요.
- 운영 배포, 데이터 변경, 패키지 설치 같은 작업은 기본적으로 승인 대상으로 설계됩니다.
