# Project Rule Resolution

## 목적

프로젝트마다 다른 코딩 규약, UI 규약, 보안 정책과 실행 방식을 탐색하고 현재 작업에 적용할 규칙을 결정한다.

---

## 규약 종류

- 사용자 현재 요청
- 현재 작업 전용 규약
- 프로젝트 규약
- 조직 규약
- 에이전트 기본 규약
- 스킬 기본 규약
- 안전·보안·법적 제한

---

## 탐색 순서

1. 현재 사용자 요청
2. 현재 대화에서 확정된 조건
3. 작업 대상과 함께 제공된 문서
4. 프로젝트 루트의 에이전트 지침
5. 프로젝트 문서
6. 기술 설정 파일
7. 디자인 시스템과 테마
8. 기존 구현 패턴
9. 테스트 코드
10. CI/CD와 배포 설정
11. 에이전트 기본 규약
12. 스킬 안전 기본값

---

## 주요 탐색 대상

```text
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
README.md
DEVELOPMENT.md
STYLEGUIDE.md
SECURITY.md
.cursor/rules/
.github/instructions/
package.json
tsconfig.json
eslint.config.js
.prettierrc
Dockerfile
theme/
styles/
tokens/
design-system/
components/
tests/
.github/workflows/
```

---

## 규약 우선순위

```text
안전·보안·법적 제한
> 사용자의 현재 명시적 지시
> 현재 작업 전용 규약
> 프로젝트 필수 규약
> 조직 규약
> 에이전트 기본 규약
> 스킬 기본값
```

---

## 경로 범위

작업 파일에 가장 가까운 범위의 규약을 우선 적용한다.

예시:

```text
/project/AGENTS.md
/project/frontend/AGENTS.md
/project/frontend/admin/AGENTS.md
```

`frontend/admin` 파일을 수정하면 `frontend/admin/AGENTS.md`를 우선한다.

상위 규약은 하위 규약에서 변경하지 않은 범위에 계속 적용된다.

---

## 명시 규칙과 코드 패턴

명시적인 규약은 기존 코드 패턴보다 우선한다.

명시적인 규약이 없다면 반복되고 일관된 기존 패턴을 규칙으로 추론할 수 있다.

다음은 규약으로 추론하지 않는다.

- 한두 파일에만 나타나는 예외
- deprecated 코드
- 오래된 레거시 패턴
- 명백한 버그
- 서로 충돌하는 구현

---

## 규칙 기록 형식

```yaml
rules:
  - id: UI-001
    description: 공통 버튼은 기존 Button 컴포넌트를 사용한다.
    category: ui
    source_type: project_file
    source: src/components/common/Button.tsx
    scope: src/pages/admin
    priority: project
    confidence: high
```

---

## 규약 충돌 처리

1. 각 규약의 출처를 확인한다.
2. 적용 범위를 확인한다.
3. 현재 유효성을 확인한다.
4. 상위 우선순위를 적용한다.
5. 더 구체적인 범위의 규칙을 적용한다.
6. deprecated 여부를 확인한다.
7. 해결할 수 없고 결과에 중요하면 `NEEDS_CLARIFICATION`을 반환한다.

---

## 스킬에 전달하는 규칙 세트

```yaml
applicable_rules:
  task_scope: src/pages/admin/users

  technology:
    framework: nextjs
    language: typescript
    ui_library: chakra-ui

  implementation:
    use_existing_components: true
    package_installation: approval_required
    api_contract_change: prohibited

  naming:
    component: PascalCase
    file: PascalCase

  validation:
    lint_required: true
    typecheck_required: true
    tests_required: conditional

  sources:
    - AGENTS.md
    - package.json
    - src/theme/index.ts
```

프로젝트 규칙을 재사용 가능한 스킬 내부에 하드코딩하지 않는다.

---

## 규약이 없을 때 기본값

- 기존 코드와 구조 우선
- 새 패턴 임의 도입 금지
- 최소 변경
- 일반적인 보안과 접근성 기준 적용
- 파괴적 작업 금지
- 불확실한 사항은 `Assumptions`에 기록
