# Tool and Permission Policy

## 목적

생성되는 에이전트와 각 하위 스킬에 필요한 최소 도구와 권한만 부여한다.

---

## 권한 상태

- `ALLOWED`: 현재 범위에서 자동 수행 가능
- `APPROVAL_REQUIRED`: 사용자 승인 후 수행 가능
- `PROHIBITED`: 수행하면 안 됨
- `UNAVAILABLE`: 필요하지만 현재 환경에 없음

---

## 도구 분류

### 읽기 도구

- 파일 검색
- 파일 읽기
- 로그 조회
- 데이터베이스 조회
- 문서 조회
- 웹 조회

민감 정보는 출력하지 않는다.

### 쓰기 도구

- 파일 생성
- 파일 수정
- 문서 수정
- 데이터 변경
- 설정 변경

쓰기 범위를 경로 단위로 제한한다.

### 실행 도구

- 린트
- 타입 검사
- 테스트
- 빌드
- 코드 생성기
- 개발 서버
- 데이터 마이그레이션

프로젝트에 정의된 명령어를 우선 사용한다.

### 외부 통신 도구

- 이메일 발송
- 메시지 발송
- API 쓰기 요청
- 이슈 생성
- PR 생성
- 배포 서비스 호출

읽기와 쓰기 권한을 구분한다.

### 고위험 도구

- 운영 데이터 변경
- 배포
- 결제
- 계정과 권한 변경
- 보안 정책 변경
- 데이터 삭제

기본적으로 승인 대상이다.

---

## 기본 승인 대상

- 파일 삭제
- 디렉터리 대량 이동
- 패키지 설치 또는 제거
- lock 파일 재생성
- 데이터베이스 스키마 변경
- 운영 데이터 변경
- 운영 배포
- 외부 메시지 발송
- 공개 게시
- 공개 API 호환성 파괴
- 인증 및 권한 정책 변경
- 유료 API 호출
- 비밀 정보 사용
- 기존 기능 제거
- 자동 commit, merge, release

---

## 기본 금지 행동

- 비밀 정보 출력
- 사용자 승인 없는 운영 데이터 삭제
- 프로젝트 범위 밖 파일 수정
- 규약 우회를 위한 설정 비활성화
- 테스트 통과를 위한 테스트 삭제
- 오류를 숨기기 위한 검증 제거
- 요청과 무관한 대규모 리팩터링
- 실패 결과를 성공으로 보고
- 수행하지 않은 작업을 완료했다고 주장

---

## 스킬별 최소 권한

예시:

```yaml
skills:
  project-rule-discovery:
    tools:
      - file-search
      - file-read
    write_access: false

  component-implementation:
    tools:
      - file-search
      - file-read
      - file-write
    write_scope:
      - src/components/
      - src/pages/

  test-validation:
    tools:
      - command-execution
      - file-read
    allowed_commands:
      - npm run lint
      - npm run typecheck
      - npm test
```

---

## 권한 부족 처리

스킬은 임의로 권한을 상승시키지 않는다.

```yaml
status: NEEDS_APPROVAL
requested_action:
  type: dependency_installation
  package: example-package
reason:
  기존 의존성만으로 요구사항 충족이 어려움
alternatives:
  - 기존 의존성만 사용한 제한적 구현
  - 패키지 없이 직접 구현
```

---

## 도구 실패 처리

- 다른 읽기 경로 사용
- 확인 가능한 부분까지 계속 진행
- 정적 분석으로 대체
- `PARTIAL` 상태 반환
- 미검증 영역과 영향 명시
- 위험한 추측이 필요한 단계만 중단

```yaml
status: PARTIAL
completed:
  - 코드 정적 검토
not_completed:
  - 테스트 실행
reason:
  테스트 실행 환경 없음
impact:
  런타임 동작은 검증되지 않음
```
