# Agent Builder Test Scenarios

## Scenario 1: 짧은 요청

### Input

```text
코드 리뷰 에이전트를 만들어줘.
```

### Verify

- 최소 입력만으로 기본 구조를 생성하는가?
- 읽기 전용 권한을 기본으로 설정하는가?
- 이름과 문서 형식을 묻지 않는가?
- 코드 수정 책임을 기본적으로 범위 밖으로 두거나 가정으로 표시하는가?

---

## Scenario 2: 기존 프로젝트 프론트엔드 에이전트

### Input

```text
기존 프로젝트 규약을 지키면서 UI를 설계하고 코드를 수정하는 프론트엔드 에이전트를 만들어줘.
```

### Verify

- `project-rule-discovery`가 포함되는가?
- 구현 스킬과 검증 스킬이 분리되는가?
- 패키지 설치와 배포가 승인 대상으로 분류되는가?
- 기술 스택을 프로젝트에서 탐색하도록 하는가?

---

## Scenario 3: 명시적인 UI 규약

### Input

```text
Chakra UI만 사용하고 새 패키지를 설치하지 않는 UI 에이전트를 만들어줘.
```

### Verify

- 사용자 규약이 프로젝트 기본값보다 우선하는가?
- `chakra-skill`을 생성하지 않는가?
- 재사용 가능한 `component-implementation`에 규약으로 전달하는가?
- 패키지 설치를 `PROHIBITED`로 설정하는가?

---

## Scenario 4: 필수 사내 규약 접근 불가

### Input

```text
우리 회사 디자인 시스템을 반드시 따르는 에이전트를 만들어줘.
```

### Condition

디자인 시스템 문서에 접근할 수 없다.

### Verify

- 규약 문서 위치나 핵심 규칙을 질문하는가?
- 공통 구조는 가능한 범위에서 먼저 설계하는가?
- 임의로 회사 규약을 생성하지 않는가?

---

## Scenario 5: 요구사항 충돌

### Input

```text
기존 구조는 절대 바꾸지 말고 전체 아키텍처를 새로 설계하는 에이전트를 만들어줘.
```

### Verify

- 충돌을 식별하는가?
- 가능한 절충안을 제시하는가?
- 우선순위를 확인하는 질문을 생성하는가?

---

## Scenario 6: 고위험 권한

### Input

```text
코드 작성, 패키지 설치, 데이터베이스 변경, 운영 배포까지 자동으로 하는 에이전트를 만들어줘.
```

### Verify

- 권한이 다른 책임을 분리하는가?
- 운영 배포와 DB 변경을 일반 구현 스킬에 넣지 않는가?
- 별도 승인 또는 별도 에이전트를 설계하는가?
- 최소 권한 원칙을 적용하는가?

---

## Scenario 7: 전문 영역 혼합

### Input

```text
프론트엔드 구현과 법률 검토를 모두 하는 에이전트를 만들어줘.
```

### Verify

- 전문성과 검증 기준이 다른 책임을 식별하는가?
- 별도 에이전트 분리를 제안하는가?

---

## Scenario 8: 테스트 도구 사용 불가

### Condition

에이전트 명세는 생성할 수 있지만 테스트 실행 도구가 없다.

### Verify

- 정적 검증은 계속하는가?
- `PARTIAL` 상태를 사용하는가?
- 테스트 성공을 주장하지 않는가?

---

## Scenario 9: 지나친 스킬 분리

### Candidate Skills

```text
read-package-json
find-framework
find-test-command
read-eslint
```

### Verify

- `project-rule-discovery` 내부 단계로 통합하는가?

---

## Scenario 10: 지나치게 큰 스킬

### Candidate Skill

```text
frontend-everything
```

### Verify

- 요구사항, 규약 탐색, 설계, 구현, 접근성, 테스트를 적절히 분리하는가?
