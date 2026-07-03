---
name: agent-builder
description: 프로젝트의 목적, 코드, 규약과 사용 맥락을 분석하여 AI-ready 프로젝트 문서, 재사용 가능한 하위 스킬, Claude Code 또는 Factory Droid용 프로젝트 전용 에이전트를 생성한다. 에이전트 제작, 전문 에이전트 구성, 서브에이전트, Custom Droid 생성, 새 프로젝트 AI 작업 환경 초기화, 프로젝트 규칙/스킬/에이전트 세팅 요청에 사용한다.
user-invocable: true
disable-model-invocation: false
---

# Agent Builder

## Purpose

사용자가 만들고자 하는 에이전트의 목적과 업무를 분석하여 실행 가능한 에이전트 명세, 하위 스킬 구조, 프로젝트 규약, 도구와 권한 정책 및 검증 시나리오를 설계한다.

새 프로젝트나 AI 작업 환경 초기화 요청에서는 프로젝트 목적, 아키텍처, 규칙과 워크플로를 먼저 정리한 뒤 그 위에서 동작할 하위 스킬과 에이전트를 생성한다.

이 스킬은 생성 대상 에이전트의 실제 업무를 대신 수행하지 않는다.

예를 들어 프론트엔드 에이전트를 설계할 때 이 스킬이 직접 화면을 구현하는 것이 아니라, 프론트엔드 에이전트의 책임과 필요한 하위 스킬을 설계한다.

---

## Primary Outputs

기본적으로 다음 결과물을 생성한다.

- 에이전트 개요
- 에이전트의 최종 책임
- 담당 업무와 범위 밖 업무
- 사용자 승인이 필요한 업무
- 입력과 출력
- 작업 흐름
- 하위 스킬 구조
- 각 스킬의 호출 조건
- 각 스킬의 입력과 출력
- 스킬 간 의존성
- 프로젝트 규약 적용 방식
- 프로젝트 목적, 아키텍처, 규칙과 워크플로 문서
- 도구와 권한 명세
- 사용자 질문 정책
- 실패 및 예외 처리 정책
- 검증 시나리오
- 가정과 미확정 사항

---

## Minimum Input

사용자는 만들고자 하는 에이전트의 역할 또는 목적만 제공해도 된다.

예시:

```text
프론트엔드 전문가 에이전트를 만들어줘.
```

그 외 정보는 다음 순서로 보완한다.

1. 현재 사용자 요청
2. 현재 대화에서 이미 제공된 정보
3. 접근 가능한 프로젝트와 문서
4. 기존 구현 패턴
5. 합리적인 추론
6. 안전한 기본값
7. 사용자 질문

모든 입력 항목을 사용자에게 양식으로 채우게 하지 않는다.

---

## Operating Modes

요청의 목적에 따라 다음 모드 중 하나를 선택한다.

### Agent-Only Mode

기존 프로젝트 또는 이미 알려진 프로젝트 맥락 위에 전문 에이전트와 하위 스킬만 생성한다.

사용 예:

```text
이 프로젝트의 코드 리뷰 에이전트를 만들어줘.
프론트엔드 구현 에이전트와 UI 스킬을 만들어줘.
```

### Project Bootstrap Mode

새 프로젝트 또는 아직 AI 작업 규칙이 없는 프로젝트를 AI-ready workspace로 초기화하고, 공통 프로젝트 지식과 필요한 에이전트/스킬을 함께 생성한다.

사용 예:

```text
Go Fiber, Next.js, PostgreSQL 프로젝트를 시작할 건데 AI가 일할 수 있게 세팅해줘.
새 회사 시스템 프로젝트의 규칙, 스킬, 에이전트까지 만들어줘.
```

이 모드는 `references/project-bootstrap-policy.md`를 따른다.

### Existing Project Analysis Mode

기존 프로젝트를 분석해 `.agent/` 문서, 규칙, 스킬과 에이전트를 생성한다. 이 모드는 기본적으로 v3 범위로 취급하되, 현재 접근 가능한 파일을 읽어 안전하게 생성할 수 있는 문서와 에이전트는 만든다.

사용 예:

```text
이 레거시 Go 프로젝트를 분석해서 AI 작업 환경으로 정리해줘.
```

코드 수정, 패키지 설치, 설정 변경, 대규모 재구성은 별도 승인 대상으로 둔다.

---

## Requirement Model

요구사항을 다음 항목으로 구조화한다.

```yaml
identity:
  agent_name:
  purpose:
  primary_users:
  agent_category:

scope:
  primary_responsibilities:
  optional_responsibilities:
  out_of_scope:
  requires_approval:
  delegated_to_other_agents:

environment:
  project_type:
  target_resource:
  languages:
  frameworks:
  libraries:
  runtime:
  build_tools:
  test_tools:
  deployment_environment:

rules:
  user_rules:
  task_rules:
  project_rules:
  organization_rules:
  agent_defaults:
  skill_defaults:

inputs:
  primary_input:
  optional_inputs:
  required_context:

outputs:
  primary_output:
  output_format:
  files_to_create:
  project_documents:
  completion_report:

tools:
  available:
  restricted:
  unavailable:

permissions:
  allowed:
  approval_required:
  prohibited:

autonomy:
  level:
  allowed_assumptions:
  question_conditions:

validation:
  success_criteria:
  required_tests:
  quality_checks:
  failure_conditions:
```

---

## Information Status

각 정보는 다음 상태 중 하나로 관리한다.

- `CONFIRMED`: 사용자가 직접 제공하거나 명시적으로 확인된 정보
- `DISCOVERED`: 프로젝트 파일이나 환경에서 발견한 정보
- `INFERRED`: 다른 정보에 근거하여 추론한 정보
- `DEFAULTED`: 명시된 정보가 없어 기본값을 사용한 정보
- `UNRESOLVED`: 결과에 중요하지만 아직 확인되지 않은 정보
- `UNRESOLVED_NON_BLOCKING`: 확인되지 않았지만 현재 설계를 진행할 수 있는 정보

추론과 기본값은 사실처럼 표현하지 않는다.

최종 결과의 `Assumptions`에 기록한다.

---

## Core Principles

### Agent Owns the Final Goal

에이전트는 다음을 책임진다.

- 사용자 목적 해석
- 작업 범위 결정
- 하위 스킬 선택
- 스킬 호출 순서 결정
- 사용자 질문 여부 판단
- 승인 필요 여부 판단
- 스킬 출력 충돌 해결
- 결과 통합
- 최종 성공 여부 판단

### Skills Own Repeatable Procedures

스킬은 다음 특성을 가진 특정 작업 절차다.

- 호출 조건이 명확하다.
- 입력과 출력이 명확하다.
- 반복할 수 있다.
- 독립적으로 검증할 수 있다.
- 실패 상태를 반환할 수 있다.

### Tools Perform Actions

도구는 파일 읽기, 파일 수정, 명령어 실행, 외부 조회와 같은 실제 행동을 수행한다.

```text
사용자 요청
→ 에이전트 판단
→ 스킬 선택
→ 스킬의 도구 사용
→ 스킬 결과
→ 에이전트 통합
```

---

## Requirement Collection Procedure

1. 사용자 요청에서 목적, 대상, 업무와 제한을 추출한다.
2. 현재 대화에서 이미 제공된 정보를 확인한다.
3. 기존 프로젝트가 있다면 규약과 기술 환경을 탐색한다.
4. 각 요구사항에 정보 상태를 부여한다.
5. 결과에 중요한 미확정 정보를 식별한다.
6. 탐색 가능한 정보는 먼저 탐색한다.
7. 낮은 영향도의 정보는 기본값을 사용한다.
8. 높은 영향도이며 탐색할 수 없는 정보만 질문 후보로 둔다.
9. 질문하지 않은 가정은 최종 결과에 기록한다.

상세 기준은 `references/question-policy.md`를 따른다.

---

## User Question Policy

모든 누락 정보에 대해 질문하지 않는다.

질문 전에 다음 순서로 해결을 시도한다.

```text
현재 요청
→ 기존 대화
→ 프로젝트 탐색
→ 기존 구현 패턴
→ 합리적인 추론
→ 안전한 기본값
→ 사용자 질문
```

다음 항목에 실질적인 영향을 주는 정보가 없을 때 질문을 검토한다.

- 에이전트 목적
- 책임 범위
- 에이전트 또는 스킬 구조
- 도구 선택
- 권한 범위
- 안전
- 외부 영향
- 되돌리기 어려운 결정
- 필수 프로젝트 규약
- 검증 및 성공 기준

다음 조건에서는 질문한다.

- 답에 따라 에이전트 구조가 크게 달라진다.
- 필수 프로젝트 또는 조직 규약이 언급됐지만 접근할 수 없다.
- 요구사항이 충돌하고 우선순위를 추론할 수 없다.
- 작업 대상이나 핵심 책임이 불명확하다.
- 파괴적, 외부 영향, 비용 또는 보안 관련 권한이 필요하다.
- 성공 여부를 판단할 기준을 일반적인 기본값으로도 만들 수 없다.

다음 조건에서는 질문하지 않는다.

- 이미 현재 대화에서 제공된 정보다.
- 프로젝트 파일에서 확인할 수 있다.
- 안전하고 일반적인 기본값이 존재한다.
- 잘못 선택해도 쉽게 변경할 수 있다.
- 이름, 문서 순서, 파일명과 같은 낮은 영향도의 항목이다.
- 일부 불확실성이 있어도 공통 구조를 설계할 수 있다.

질문은 다음 원칙을 따른다.

- 질문 이유를 설명한다.
- 결과에 중요한 질문만 한다.
- 관련 질문을 한 번에 묶는다.
- 가능한 경우 선택지를 제공한다.
- 전문적인 권장 기본값을 함께 제시한다.
- 사용자가 이미 답한 내용을 다시 묻지 않는다.

요구사항 질문과 행동 승인은 구분한다.

---

## Approval Policy

다음 작업은 기본적으로 사용자 승인을 필요로 한다.

- 파일 삭제
- 대규모 파일 이동 또는 일괄 수정
- 패키지 설치 또는 제거
- lock 파일 대규모 재생성
- 데이터베이스 스키마 변경
- 운영 데이터 변경
- 운영 배포
- 외부 메시지 발송
- 공개 저장소 또는 외부 서비스 게시
- 기존 공개 API의 호환성 파괴
- 인증 및 권한 정책 변경
- 비용이 발생하는 작업
- 비밀 정보 사용
- 기존 기능 제거
- 자동 commit, merge 또는 release

생성되는 에이전트의 역할에 필요하지 않은 권한은 부여하지 않는다.

상세 기준은 `references/permission-policy.md`를 따른다.

---

## Agent and Skill Decomposition

### Keep as Agent Responsibility

다음은 에이전트의 직접 책임으로 유지한다.

- 사용자 최종 목표 해석
- 전체 작업 범위 결정
- 스킬 선택과 순서 결정
- 질문 및 승인 판단
- 스킬 간 충돌 해결
- 결과 통합
- 최종 성공 판단

### Extract as a Skill

다음 조건을 하나 이상 충족하는 업무는 스킬 분리를 검토한다.

- 여러 요청에서 반복된다.
- 여러 에이전트가 재사용할 수 있다.
- 입력과 출력이 명확하다.
- 독립적으로 테스트할 수 있다.
- 전문적인 판단 기준이 있다.
- 별도 도구가 필요하다.
- 별도 권한 또는 승인 정책이 필요하다.
- 독립적인 실패 처리가 필요하다.
- 결과물이 다른 스킬의 입력으로 재사용된다.

### Keep as an Internal Step

다음 업무는 별도 스킬로 만들지 않는다.

- 한두 단계로 끝나는 작은 작업
- 상위 절차와 긴밀하게 결합된 작업
- 독립적인 결과가 없는 작업
- 반복 가능성이 낮은 세부 구현
- 파일 열기, 변수 확인, 한 줄 수정 같은 작업

### Extract as a Separate Agent

다음 조건에서는 별도 에이전트를 검토한다.

- 별도의 최종 목표를 가진다.
- 대상 사용자가 크게 다르다.
- 권한 수준이 크게 다르다.
- 실행 방식이 다르다.
- 전문성 또는 거버넌스 경계가 다르다.
- 독립적인 검증 책임이 반드시 필요하다.

상세 기준은 `references/skill-decomposition.md`를 따른다.

---

## Skill Size Rules

스킬은 하나의 주요 질문에 답할 수 있어야 한다.

적절한 예시:

```text
requirement-analysis
project-rule-discovery
ui-architecture
component-implementation
accessibility-review
test-validation
```

지나치게 큰 예시:

```text
frontend-everything
```

지나치게 작은 예시:

```text
read-package-json
find-react-version
change-button-padding
```

항상 함께 호출되고 독립적인 실패 처리가 없는 스킬은 통합한다.

서로 다른 전문 기준과 실패 조건을 가진 책임은 분리한다.

---

## Skill Specification

각 스킬은 다음 항목을 반드시 정의한다.

```markdown
# Skill Name

## Purpose

## Called When

## Not Called When

## Required Inputs

## Optional Inputs

## Outputs

## Preconditions

## Procedure

## Tools

## Permissions

## Applicable Rules

## Dependencies

## Success Conditions

## Failure States

## Failure Handling

## Result Schema

## Validation Scenarios
```

스킬 이름은 기술 이름이 아니라 책임을 표현해야 한다.

권장:

```text
component-implementation
state-management-design
project-rule-discovery
```

비권장:

```text
react-skill
typescript-skill
chakra-skill
helper
smart-tool
```

기술 스택은 재사용 가능한 스킬에 입력 또는 규약으로 전달한다.

---

## Skill Interaction Policy

하위 스킬은 기본적으로 사용자에게 직접 질문하지 않는다.

필요한 정보나 승인이 없으면 구조화된 상태를 반환한다.

- `SUCCESS`
- `PARTIAL`
- `NEEDS_CLARIFICATION`
- `NEEDS_APPROVAL`
- `FAILED`

예시:

```yaml
status: NEEDS_CLARIFICATION

reason:
  type: missing_mandatory_rule
  description: 필수 디자인 규약에 접근할 수 없음

affected_outputs:
  - ui_architecture
  - component_implementation

suggested_question:
  적용해야 할 디자인 시스템 문서나 핵심 규칙을 제공해 주세요.
```

에이전트가 이 상태를 바탕으로 탐색, 기본값 적용, 질문 또는 중단 여부를 판단한다.

---

## Project Rule Discovery

기존 프로젝트에서는 다음 순서로 규약을 탐색한다.

1. 현재 사용자 요청
2. 현재 작업 전용 규칙
3. `AGENTS.md`, `CLAUDE.md`와 같은 에이전트 지침
4. `README.md`, `CONTRIBUTING.md`, `SECURITY.md`
5. 기술 설정 파일
6. 디자인 시스템과 테마
7. 기존 구현 패턴
8. 테스트 코드
9. CI/CD 및 배포 설정
10. 에이전트 기본 규약
11. 스킬 안전 기본값

탐색 대상 예시:

```text
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
README.md
SECURITY.md
.cursor/rules/
.github/instructions/
package.json
tsconfig.json
eslint.config.js
Dockerfile
theme/
tokens/
components/
tests/
.github/workflows/
```

규칙은 출처, 적용 범위, 우선순위와 신뢰도를 함께 기록한다.

```yaml
rule:
  id: UI-001
  description: 기존 공통 Button 컴포넌트를 우선 사용한다.
  source: src/components/common/Button.tsx
  source_type: inferred_pattern
  priority: project
  confidence: medium
```

상세 기준은 `references/rule-resolution.md`를 따른다.

---

## Project Bootstrap Mode

새 프로젝트를 AI-ready workspace로 초기화할 때는 코드 생성을 먼저 하지 않는다. 프로젝트 목적, 작업 방식, 규칙, 권한 경계와 에이전트 구성을 먼저 고정한다.

### Bootstrap Outputs

기본 생성물:

```text
.agent/
├── PROJECT.md
├── ARCHITECTURE.md
├── RULES.md
└── WORKFLOW.md
.agent-builder/
└── <project-name>/
    ├── setup-plan.md
    ├── readiness-report.md
    └── agent-scenarios.md
```

플랫폼 대상이 있으면 기존 Agent-Only Mode 산출물도 함께 생성한다.

```text
.claude/agents/<agent-name>.md
.claude/skills/<skill-name>/SKILL.md
.factory/droids/<agent-name>.md
.factory/skills/<skill-name>/SKILL.md
```

### Bootstrap Procedure

1. 프로젝트 목적, 사용자, 도메인, 주요 워크플로를 추출한다.
2. 기술 스택, 런타임, 데이터 저장소, 배포 환경과 제약을 확인한다.
3. 불명확하지만 낮은 영향도의 항목은 안전한 기본값으로 둔다.
4. 아키텍처, 코드 규칙, 테스트 기준, 보안 기준과 승인 정책을 문서화한다.
5. 프로젝트 업무를 담당할 에이전트 후보와 하위 스킬 후보를 분해한다.
6. `.agent/` 공통 문서와 플랫폼별 에이전트/스킬 파일을 생성한다.
7. `.agent-builder/<project-name>/setup-plan.md`와 `readiness-report.md`에 가정, 미확정 사항, 승인 필요 작업을 기록한다.
8. 검증 시나리오를 생성하고 완료 조건을 확인한다.

### Bootstrap Boundaries

기본 허용:

- `.agent/` 프로젝트 지식 문서 생성
- `.agent-builder/` 계획, 리포트와 검증 시나리오 생성
- 플랫폼별 에이전트와 스킬 파일 생성
- 템플릿 수준의 설정 파일 초안 생성

기본 승인 대상:

- 패키지 설치 또는 lock 파일 생성
- 실제 애플리케이션 코드 scaffold 생성
- CI/CD 설정 추가
- 데이터베이스, 인증, 권한, 배포 관련 설정
- 기존 프로젝트 구조 변경

기본 금지:

- 운영 배포
- 실제 비밀값 생성 또는 저장
- 외부 서비스 쓰기 작업
- 사용자 승인 없는 대규모 재구성

---

## Rule Priority

기본 우선순위는 다음과 같다.

```text
안전·보안·법적 제한
> 사용자의 현재 명시적 지시
> 작업 전용 규약
> 프로젝트 필수 규약
> 조직 규약
> 에이전트 기본 규약
> 스킬 기본값
```

파일 경로별로 규약이 다르면 작업 대상에 가장 가까운 범위의 규약을 우선한다.

명시적인 규약은 단순한 기존 코드 패턴보다 우선한다.

규약 충돌을 해결할 수 없고 결과에 중대한 영향을 준다면 `NEEDS_CLARIFICATION`으로 처리한다.

---

## Tools and Permissions

도구는 다음 범주로 분류한다.

- 읽기
- 쓰기
- 명령어 실행
- 외부 통신
- 고위험 작업

각 도구는 다음을 정의한다.

```yaml
tool:
  name:
  purpose:
  allowed_when:
  approval_required_when:
  prohibited_when:
  input_scope:
  output:
  failure_handling:
```

권한 상태:

- `ALLOWED`
- `APPROVAL_REQUIRED`
- `PROHIBITED`
- `UNAVAILABLE`

최소 권한 원칙을 적용한다.

하위 스킬에는 해당 스킬이 실제로 사용하는 도구만 부여한다.

읽기 전용 스킬에 파일 수정 권한을 부여하지 않는다.

---

## Default Safety Rules

별도 규약이 없더라도 다음을 적용한다.

- 비밀 정보와 인증 정보를 출력하지 않는다.
- 요청 범위를 벗어난 파일을 수정하지 않는다.
- 파괴적 변경은 사용자 승인 없이 수행하지 않는다.
- 테스트를 통과시키기 위해 검증 코드를 임의로 제거하지 않는다.
- 오류를 숨기지 않는다.
- 수행하지 않은 작업을 완료했다고 보고하지 않는다.
- 기존 구조와 구현 패턴을 우선한다.
- 필요 이상의 리팩터링을 하지 않는다.
- 일부 검증이 불가능하면 제한 사항을 명시한다.

---

## Agent Design Procedure

### Step 1: Analyze the Request

다음을 추출한다.

- 목적
- 주요 사용자
- 핵심 업무
- 작업 대상
- 기술 환경
- 규약
- 입력
- 출력
- 도구
- 권한
- 성공 기준
- 제한

### Step 2: Assign Information Status

각 항목을 다음 중 하나로 표시한다.

- `CONFIRMED`
- `DISCOVERED`
- `INFERRED`
- `DEFAULTED`
- `UNRESOLVED`
- `UNRESOLVED_NON_BLOCKING`

### Step 3: Discover Existing Rules

기존 프로젝트라면 규약 문서, 설정 파일과 구현 패턴을 탐색한다.

### Step 4: Resolve Blocking Uncertainty

질문 정책에 따라 다음 중 하나를 선택한다.

- 기존 정보 재사용
- 프로젝트 탐색
- 추론
- 기본값 적용
- 사용자 질문
- 승인 정책 설정

### Step 5: Define Responsibility Boundaries

다음을 구분한다.

- 에이전트가 담당하는 업무
- 범위 밖 업무
- 승인 필요한 업무
- 다른 에이전트로 분리할 업무
- 하위 스킬에 위임할 업무

### Step 6: Identify Skills

각 업무에 대해 다음을 평가한다.

- 반복성
- 재사용성
- 입력과 출력
- 독립 검증 가능성
- 전문 기준
- 별도 도구
- 별도 권한
- 실패 처리

### Step 7: Remove Over-Decomposition

다음을 통합한다.

- 항상 함께 호출되는 스킬
- 목적과 출력이 중복되는 스킬
- 독립적 결과가 없는 작은 스킬
- 기술 이름만 다른 스킬

### Step 8: Define Skill Interfaces

각 스킬의 호출 조건, 입력, 출력, 의존성, 도구, 권한과 실패 상태를 정의한다.

### Step 9: Define the Skill Graph

스킬 호출 관계를 정의한다.

- 순차 호출
- 병렬 호출
- 조건부 호출
- 반복 호출

반복 호출에는 종료 조건을 둔다.

### Step 10: Define Tools and Permissions

에이전트 및 각 스킬에 필요한 최소 도구와 권한을 부여한다.

### Step 11: Define Validation

정상, 누락 정보, 규약 충돌, 권한 부족, 도구 실패와 범위 밖 요청을 검증한다.

### Step 12: Generate the Specification

에이전트 명세, 스킬 명세, 규약 정책, 권한 정책과 테스트 시나리오를 출력한다.

### Step 13: Run Quality Review

완료 조건을 확인하고 부족한 부분을 수정한다.

---

## Output Structure

```markdown
# Agent Specification

## 1. Agent Overview

## 2. Purpose

## 3. Primary Users

## 4. Responsibilities

### In Scope

### Out of Scope

### Requires Approval

### Delegated to Other Agents

## 5. Inputs and Outputs

## 6. Requirement Status

## 7. Operating Principles

## 8. Project Rule Resolution

## 9. Workflow

## 10. Skills

### Skill: name

- Purpose:
- Called when:
- Not called when:
- Required inputs:
- Optional inputs:
- Outputs:
- Dependencies:
- Tools:
- Permissions:
- Failure states:

## 11. Skill Graph

## 12. Tools and Permissions

## 13. Question Policy

## 14. Approval Policy

## 15. Error Handling

## 16. Validation Scenarios

## 17. Assumptions

## 18. Unresolved Decisions
```

---


## Platform Target and Final Artifact Generation

이 스킬의 최종 결과는 분석 보고서나 추상적인 설계안이 아니라, 현재 프로젝트의 에이전트 런타임에서 사용할 수 있는 실제 파일이어야 한다.

### Platform Detection

현재 실행 환경 또는 사용자의 요청을 기준으로 대상 플랫폼을 결정한다.

- Claude Code에서 실행 중이면 `claude-code`를 기본 대상으로 사용한다.
- Factory Droid에서 실행 중이면 `factory-droid`를 기본 대상으로 사용한다.
- 사용자가 두 플랫폼을 모두 요청하면 공통 명세를 기반으로 두 플랫폼용 파일을 모두 생성한다.
- 플랫폼을 확인할 수 없으면 중립 명세와 두 플랫폼용 어댑터를 함께 생성하고 가정에 기록한다.
- 플랫폼을 확인할 수 있다는 이유로 사용자에게 다시 묻지 않는다.

### Claude Code Output

Claude Code용 프로젝트 에이전트는 `.claude/agents/<agent-name>.md`에 생성하고, 하위 스킬은 `.claude/skills/<skill-name>/SKILL.md`에 생성한다.

권장 구조는 다음과 같다.

```text
<project>/
├── .claude/
│   ├── agents/
│   │   └── <agent-name>.md
│   └── skills/
│       └── <skill-name>/
│           └── SKILL.md
```

Claude Code 에이전트 파일은 YAML frontmatter와 실행 지침 본문을 포함한다.

최소 frontmatter:

```yaml
---
name: <agent-name>
description: <when and why Claude should delegate to this agent>
model: inherit
tools: Read, Grep, Glob
skills:
  - <preloaded-skill-name>
---
```

도구 이름과 권한은 현재 Claude Code 환경에서 확인한 실제 도구에 맞춘다. 읽기 전용 에이전트에는 `Write`와 `Edit`를 부여하지 않는다.

### Factory Droid Output

Factory Droid용 프로젝트 Custom Droid는 다음 위치에 생성한다.

```text
<project>/
├── .factory/
│   ├── droids/
│   │   └── <agent-name>.md
│   └── skills/
│       └── <skill-name>/
│           └── SKILL.md
```

Factory Custom Droid 파일은 `.factory/droids/` 바로 아래에 생성한다. 하위 폴더에 두지 않는다.

최소 frontmatter:

```yaml
---
name: <agent-name>
description: <when and why Droid should delegate to this custom droid>
model: inherit
tools: read-only
---
```

필요한 경우 Factory에서 지원하는 실제 도구 ID 배열을 사용한다.

### Both Platforms

두 플랫폼을 모두 대상으로 하면 다음을 생성한다.

```text
<project>/
├── .claude/
│   ├── agents/<agent-name>.md
│   └── skills/<skill-name>/SKILL.md
└── .factory/
    ├── droids/<agent-name>.md
    └── skills/<skill-name>/SKILL.md
```

공통 업무 규칙은 두 플랫폼에서 의미가 달라지지 않도록 동일한 원본 명세에서 파생한다. 플랫폼별 도구 이름, frontmatter와 저장 경로만 변환한다.

### Minimum Generated Package

별도의 제한이 없다면 최소한 다음 파일을 생성한다.

```text
<platform-agent-file>
<platform-skill-directory>/<required-skill>/SKILL.md
<platform-skill-directory>/<required-skill>/references/...
.agent-builder/<agent-name>/agent-scenarios.md
```

Project Bootstrap Mode에서는 최소한 다음 파일도 생성한다.

```text
.agent/PROJECT.md
.agent/ARCHITECTURE.md
.agent/RULES.md
.agent/WORKFLOW.md
.agent-builder/<project-name>/setup-plan.md
.agent-builder/<project-name>/readiness-report.md
.agent-builder/<project-name>/agent-scenarios.md
```

에이전트에 별도 하위 스킬이 필요하지 않다면 그 이유를 명시하고 에이전트 파일과 테스트 시나리오는 반드시 생성한다.

각 파일은 빈 템플릿이 아니라 다음을 반영한 완성된 내용이어야 한다.

- 현재 프로젝트의 기술 스택
- 현재 프로젝트의 규약
- 사용자의 목적
- Project Bootstrap Mode에서는 프로젝트 목적, 아키텍처, 규칙과 워크플로
- 허용 도구와 권한
- 승인 필요 행동
- 실패 및 부분 성공 처리
- 검증 절차

### Completion Gate

다음 조건을 만족하기 전에는 완료하지 않는다.

- 대상 플랫폼의 실제 에이전트 파일이 생성되었다.
- 모든 필수 하위 스킬에 완성된 `SKILL.md`가 생성되었다.
- 에이전트가 하위 스킬을 언제 사용하는지 정의했다.
- 프로젝트 규약과 권한 정책이 실제 파일에 반영되었다.
- 검증 시나리오 파일이 `.agent-builder/<agent-name>/agent-scenarios.md`에 생성되었다.
- Project Bootstrap Mode에서는 `.agent/` 프로젝트 문서, setup plan과 readiness report가 생성되었다.
- 생성 파일 경로와 사용 방법을 최종 보고에 포함했다.

파일을 생성할 수 없는 환경에서만 각 파일의 완성된 내용을 경로별 코드 블록으로 출력한다.

분석 보고서나 에이전트 구조만 제공하고 완료한 것으로 처리하지 않는다.

---

## Validation Requirements

최소한 다음 시나리오를 생성한다.

- 정상적인 요청
- 매우 짧은 요청
- 정보가 부족한 요청
- 프로젝트 규약이 제공된 요청
- 필수 규약에 접근할 수 없는 요청
- 서로 충돌하는 요구사항
- 권한이 필요한 요청
- 범위를 벗어난 요청
- 하위 스킬 실패
- 도구를 사용할 수 없는 요청
- 일부만 성공한 요청

상세 기준은 `references/validation-policy.md`를 따른다.

---

## Quality Checklist

완료 전에 다음을 확인한다.

- 에이전트 목적이 한 문장으로 설명되는가?
- 최종 목표의 책임자가 명확한가?
- 책임 범위와 범위 밖 업무가 구분되어 있는가?
- 승인 대상이 구체적으로 정의되어 있는가?
- 에이전트와 스킬의 역할이 중복되지 않는가?
- 각 스킬이 하나의 주요 목적을 가지는가?
- 각 스킬의 호출 조건이 명확한가?
- 각 스킬의 입력과 출력이 명확한가?
- 기술 이름만으로 만들어진 스킬이 없는가?
- 지나치게 작은 스킬이 없는가?
- 지나치게 큰 스킬이 없는가?
- 프로젝트 규약을 탐색하는 절차가 있는가?
- 규약 출처와 우선순위가 기록되는가?
- 규약 충돌 처리 방식이 있는가?
- 도구와 권한이 최소 범위로 제한되는가?
- 위험한 행동이 승인 대상으로 구분되는가?
- 하위 스킬이 무분별하게 사용자에게 질문하지 않는가?
- 실패 및 부분 성공 상태가 정의되어 있는가?
- 검증 시나리오가 존재하는가?
- 가정과 미확정 사항이 표시되는가?

하나라도 중요한 항목을 충족하지 못하면 명세를 수정한 뒤 출력한다.

---

## Prohibited Patterns

- 모든 업무를 하나의 거대한 에이전트 지침으로 만든다.
- 모든 기술 이름을 별도 스킬로 만든다.
- 모든 누락 정보를 사용자에게 질문한다.
- 프로젝트에서 확인 가능한 정보를 다시 묻는다.
- 규약을 확인하지 않고 임의의 프로젝트 규칙을 만든다.
- 동일한 책임을 여러 스킬에 중복한다.
- 입력과 출력이 없는 추상적인 스킬을 만든다.
- 하위 스킬이 각각 사용자에게 직접 질문하게 한다.
- 일반 구현 스킬에 배포와 운영 권한까지 부여한다.
- 사용자 승인 없이 파괴적 작업을 실행하도록 설계한다.
- 검증할 수 없는 성공 기준을 사용한다.
- 부분 실패를 숨기고 전체 성공으로 표시한다.

---

## Completion Conditions

다음 조건을 모두 만족하면 완료한다.

- 에이전트의 목적과 최종 책임이 정의되어 있다.
- 책임 범위, 범위 밖 업무와 승인 대상이 정의되어 있다.
- 필요한 하위 스킬이 식별되어 있다.
- 각 스킬의 호출 조건, 입력과 출력이 정의되어 있다.
- 스킬 간 의존성과 호출 흐름이 정의되어 있다.
- 프로젝트 규약 탐색 및 적용 방식이 정의되어 있다.
- 도구와 권한이 최소 범위로 정의되어 있다.
- 사용자 질문과 승인 정책이 정의되어 있다.
- 실패와 부분 성공 처리 방식이 정의되어 있다.
- 대상 플랫폼의 실제 에이전트 파일이 생성되어 있다.
- 필요한 모든 하위 스킬 파일이 생성되어 있다.
- 검증 시나리오 파일이 `.agent-builder/<agent-name>/agent-scenarios.md`에 생성되어 있다.
- Project Bootstrap Mode에서는 `.agent/` 프로젝트 문서와 `.agent-builder/<project-name>/setup-plan.md`, `readiness-report.md`가 생성되어 있다.
- 파일을 생성할 수 없는 환경에서는 생성 예정 경로별 완성본이 코드 블록으로 제공되어 있다.
- 가정과 미확정 사항이 표시되어 있다.
