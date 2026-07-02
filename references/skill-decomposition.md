# Agent and Skill Decomposition

## 기본 정의

### 에이전트

사용자의 최종 목표를 이해하고 전체 작업을 조율한다.

### 스킬

명확한 호출 조건, 입력, 절차와 출력을 가진 재사용 가능한 전문 작업이다.

### 도구

파일 읽기, 수정, 명령어 실행, 외부 조회와 같은 실제 행동을 수행한다.

---

## 에이전트가 소유해야 하는 책임

- 사용자 목적 해석
- 작업 범위 결정
- 스킬 선택
- 스킬 호출 순서 결정
- 질문 및 승인 판단
- 스킬 결과 충돌 해결
- 최종 결과 통합
- 전체 성공 여부 판단

---

## 스킬 분리 조건

다음 조건을 여러 개 충족할수록 독립 스킬로 분리할 가치가 높다.

- 반복해서 사용된다.
- 여러 에이전트가 재사용할 수 있다.
- 입력과 출력이 명확하다.
- 독립적으로 테스트할 수 있다.
- 전문적인 판단 기준이 있다.
- 별도 도구를 사용한다.
- 별도 권한이 필요하다.
- 실패 처리가 독립적이다.
- 결과가 다른 스킬의 입력으로 재사용된다.

---

## 내부 단계로 유지할 조건

- 한두 단계로 끝난다.
- 상위 절차와 강하게 결합되어 있다.
- 독립적인 결과가 없다.
- 다시 호출할 가능성이 낮다.
- 파일 열기, 변수 확인, 한 줄 수정과 같은 구현 세부다.

---

## 별도 에이전트로 분리할 조건

- 별도의 최종 목표가 있다.
- 사용자 집단이 크게 다르다.
- 권한 수준이 크게 다르다.
- 실행 주기나 방식이 다르다.
- 전문성과 검증 기준이 완전히 다르다.
- 독립적인 거버넌스 경계가 필요하다.

---

## 적절한 스킬 크기

스킬 하나는 하나의 주요 질문에 답해야 한다.

예시:

- `project-rule-discovery`: 이 프로젝트에서 지켜야 할 규칙은 무엇인가?
- `requirement-analysis`: 사용자의 요구사항과 성공 기준은 무엇인가?
- `ui-architecture`: 화면과 컴포넌트를 어떻게 구성해야 하는가?
- `accessibility-review`: 접근성 문제가 있는가?

---

## 과도하게 큰 스킬

비권장:

```text
frontend-everything
```

요구사항 분석, UI 설계, 구현, 접근성, 테스트, 배포를 모두 포함하면 사실상 또 하나의 에이전트가 된다.

---

## 과도하게 작은 스킬

비권장:

```text
read-package-json
find-react-version
change-button-padding
```

이런 작업은 상위 스킬의 내부 절차로 둔다.

---

## 기술 이름 기반 분리 금지

비권장:

```text
react-skill
typescript-skill
chakra-skill
zustand-skill
```

권장:

```text
component-implementation
state-management-design
project-rule-discovery
```

기술 스택은 스킬 입력이나 프로젝트 규약으로 전달한다.

---

## 중복 스킬 통합 기준

다음을 비교한다.

- 목적
- 호출 조건
- 입력
- 출력
- 주요 절차
- 실패 조건

대부분 같다면 통합한다.

---

## 스킬 인터페이스 필수 항목

- Name
- Purpose
- Called When
- Not Called When
- Required Inputs
- Optional Inputs
- Outputs
- Preconditions
- Procedure
- Tools
- Permissions
- Applicable Rules
- Dependencies
- Success Conditions
- Failure States
- Failure Handling
- Result Schema
- Validation Scenarios

---

## 스킬 상태 모델

- `SUCCESS`
- `PARTIAL`
- `NEEDS_CLARIFICATION`
- `NEEDS_APPROVAL`
- `FAILED`

---

## 호출 관계

### 순차 호출

앞 스킬의 출력이 다음 스킬의 입력이 된다.

### 병렬 호출

서로 독립적인 검토를 동시에 수행한다.

### 조건부 호출

API 변경, 사용자 데이터 처리 등 특정 조건에서만 호출한다.

### 반복 호출

검토 문제를 구현에 반영하고 재검토한다.

반복에는 종료 조건이 있어야 한다.

- 심각한 문제 해결
- 최대 수정 횟수 도달
- 사용자 판단 필요
- 해결 불가능한 충돌 발생
