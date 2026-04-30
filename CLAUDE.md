# CLAUDE.md

이 파일은 Claude Code가 이 저장소에서 작업할 때 참고하는 영구 지침입니다.

## 프로젝트 컨텍스트

전주 영화의 거리 리빙랩 만족도조사 웹앱. 단일 `index.html` 파일에 모든 로직이 들어있는 PWA 스타일 웹앱이며, 행사 부스 환경에서 라이브로 운영됩니다.

자세한 배경은 `README.md` 참조.

## 작업 원칙

### 라라님 선호 패턴
1. **단일 HTML 파일 구조 유지** — 모듈 분리, 빌드 시스템 도입 금지. 별도 요청이 없는 한 `index.html` 하나에 모든 코드를 유지합니다.
2. **부분 패치보다 전체 파일 제공 선호** — 작은 변경이라도 수정 후 전체 파일을 다시 보여드리는 것이 라라님이 검토하기 편합니다.
3. **변경 전 안정 버전 백업** — 큰 변경 전에 `index_stable_YYYYMMDD.html` 같은 파일명으로 백업본을 만든 뒤 작업 시작.
4. **라이브 서비스 의식** — 실제 사용자가 부스에서 응답 중일 수 있으므로, 데이터 구조 변경 시 하위 호환성 고려.

### 코드 스타일
- 이벤트 핸들러 매개변수는 `event`가 아닌 `ev`로 명명 (예약어 충돌 방지 패턴 — 라라님이 과거 디버깅 경험으로 정착)
- 한글 주석 OK
- CSS 변수 적극 활용 (`--red`, `--bg` 등 이미 정의됨)
- Vanilla JS만 사용 (jQuery, React 등 도입 금지)

### Firebase 관련
- **Firebase Realtime Database** 사용 (Firestore 아님)
- 데이터 경로는 `/responses/{auto-id}/` 구조
- 실시간 구독은 `db.ref('responses').on('value', cb)` 패턴
- 키즈 스케줄 프로젝트와는 별개의 Firebase 프로젝트
- LocalStorage는 보조 용도로만 사용 (iOS Safari 7일 만료 이슈 때문)

### 배포
- GitHub Pages
- 단일 파일 업로드 방식
- PR/CI 없이 main 브랜치에 직접 push

## 자주 하는 작업

### 응답 데이터 구조 변경 시
1. 새 필드는 모두 optional로 추가 (기존 응답 호환)
2. 결과 화면 렌더링 코드에 `r.newField || ''` 패턴으로 안전 처리
3. 관리자 화면 CSV 다운로드 함수에도 새 컬럼 반영

### 새 모드 추가 시
1. URL 파라미터 `?mode=xxx` 분기 추가
2. `<section id="xxx-mode" class="mode-section">` 추가
3. `init함수()` 작성
4. 모드 분기 분기문에 `else if (mode === 'xxx')` 추가
5. `#select-mode`의 메뉴에 새 링크 추가

### 디자인 변경 시
- 레드(`#C8102E`) + 화이트 컨셉 유지가 기본
- 분과별 색상은 `DIVISIONS` 배열의 `color` 필드에 정의됨 — 일관되게 적용
- 부스 큰 모니터 가독성 고려 (1200px 이상 미디어쿼리에서 폰트 키우기)

## 금지 사항

- ❌ React, Vue, jQuery 등 라이브러리 도입
- ❌ 빌드 도구 (webpack, vite 등) 도입
- ❌ 파일 분리 (CSS/JS 별도 파일로 빼기)
- ❌ TypeScript 변환
- ❌ 기존 응답 데이터를 깨뜨리는 스키마 변경

## 테스트 방법

1. **로컬 테스트**: `python3 -m http.server 8000` 후 `http://localhost:8000/?mode=respond` 접속
2. **Firebase 미설정 시**: 응답이 LocalStorage에 저장되며 경고 alert 표시 — 정상
3. **모드별 동작 확인**:
   - `?mode=respond` → 폼 표시
   - `?mode=display` → 빈 결과 화면 (Firebase 미설정 시 안내 메시지)
   - `?mode=admin` → 비밀번호 입력창

## 향후 작업 우선순위 (라라님이 정하실 부분)

`README.md`의 "다음 작업 후보" 섹션 참조. 구체적인 작업 시작 전 라라님께 어떤 것부터 할지 확인.
