# 개인 Git 저장소에 게시하기

## 1. 원격 저장소 만들기

GitHub, GitLab 또는 다른 Git 호스팅에서 빈 저장소를 만듭니다.

권장 저장소 이름:

```text
agent-builder
```

README, `.gitignore`, 라이선스를 원격에서 미리 생성하지 않고 빈 저장소로 만드는 편이 충돌이 적습니다.

## 2. 로컬 저장소 초기화

이 패키지의 루트에서:

```bash
git init
git add .
git commit -m "feat: add project agent builder skill"
git branch -M main
```

## 3. 원격 저장소 연결

```bash
git remote add origin <REPOSITORY_URL>
git push -u origin main
```

예시 형식:

```text
https://github.com/<username>/agent-builder.git
```

## 4. 버전 태그 만들기

```bash
git tag -a v1.0.0 -m "Agent Builder v1.0.0"
git push origin v1.0.0
```

## 5. 다른 프로젝트에서 설치

Claude Code:

```bash
git submodule add <REPOSITORY_URL> .claude/skills/agent-builder
```

Factory Droid:

```bash
git submodule add <REPOSITORY_URL> .factory/skills/agent-builder
```

두 플랫폼:

```bash
git submodule add <REPOSITORY_URL> .claude/skills/agent-builder
git submodule add <REPOSITORY_URL> .factory/skills/agent-builder
```

## 6. 업데이트 배포

Agent Builder 저장소에서:

```bash
git add .
git commit -m "fix: improve generated agent validation"
git push
git tag -a v1.0.1 -m "Agent Builder v1.0.1"
git push origin v1.0.1
```

사용 프로젝트에서:

```bash
git submodule update --remote
git add .gitmodules .claude/skills/agent-builder .factory/skills/agent-builder
git commit -m "chore: update agent-builder skill"
```

## 7. 공개 공유 시 추가 고려사항

저장소를 공개할 경우 라이선스를 선택해 `LICENSE` 파일을 추가합니다.

- 자유로운 재사용 허용: MIT, Apache-2.0 등
- 개인 보관만 목적: 비공개 저장소 유지
- 라이선스가 없으면 다른 사용자의 재사용 권한이 명확하지 않을 수 있음

라이선스 선택은 저장소 공개 범위와 원하는 재사용 조건에 맞춰 결정합니다.
