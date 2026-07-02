# Expected Results

## Scenario 1

```yaml
agent:
  type: code-review
  default_permissions:
    allowed:
      - file_search
      - file_read
    prohibited:
      - file_write
      - deployment
```

질문 없이 기본 명세를 생성하되, 수정 기능은 범위 밖으로 명시한다.

---

## Scenario 2

예상 스킬:

```text
requirement-analysis
project-rule-discovery
change-impact-analysis
ui-architecture
component-implementation
accessibility-review
code-quality-review
test-validation
```

---

## Scenario 3

예상 규칙:

```yaml
applicable_rules:
  ui_library: chakra-ui
  dependency_installation: prohibited
```

기술 이름 기반 스킬은 만들지 않는다.

---

## Scenario 4

예상 상태:

```yaml
status: NEEDS_CLARIFICATION
reason:
  type: missing_mandatory_rule
```

---

## Scenario 5

예상 질문:

> 기존 구조를 유지한다는 조건과 전체 아키텍처를 새로 설계한다는 조건이 충돌합니다. 기존 외부 인터페이스와 폴더 구조는 유지하되 내부 컴포넌트 경계만 재설계하는 방향을 우선할까요?

---

## Scenario 6

예상 구조:

```text
Development Agent
Database Migration Agent
Deployment Agent
```

또는 하나의 상위 오케스트레이터와 권한이 분리된 실행 에이전트들.

---

## Scenario 7

예상 구조:

```text
Frontend Development Agent
Legal Review Agent
```

---

## Scenario 8

예상 상태:

```yaml
status: PARTIAL
limitations:
  - runtime_validation_not_executed
```

---

## Scenario 9

예상 통합:

```text
project-rule-discovery
```

---

## Scenario 10

예상 분리:

```text
requirement-analysis
project-rule-discovery
ui-architecture
component-implementation
accessibility-review
test-validation
```
