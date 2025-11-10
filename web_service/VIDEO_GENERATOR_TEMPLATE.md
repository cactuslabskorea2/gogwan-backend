# 🎬 영상 생성기 추가 가이드

이 문서는 새로운 영상 생성기를 추가하는 방법을 설명합니다.

---

## 🎯 생성기 추가 3단계

### 1단계: 생성기 HTML 파일 생성
### 2단계: video-generators.html에 카드 추가
### 3단계: 관리자 페이지 업데이트

---

## 📋 1단계: 생성기 HTML 파일 생성

`lecture-generator.html`을 참고하여 새로운 영상 생성기를 만드세요.

### 기본 구조:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <script type="module" src="admin/auth-check.js"></script>
  <script src="analytics.js" type="module"></script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[생성기 이름] - Cactus Labs</title>

  <!-- Cactus Labs 통일 스타일 사용 -->
  <style>
    /* lecture-generator.html의 스타일 복사 */
    /* 색상 테마: #ec4899 (핑크) ~ #8b5cf6 (퍼플) */
  </style>
</head>
<body>
  <!-- Navigation -->
  <nav>
    <div class="nav-container">
      <a href="index.html" class="logo">Cactus Labs</a>
      <div class="nav-links">
        <a href="index.html">홈</a>
        <a href="admin/index.html">관리자</a>
        <a href="content-generators.html">교육 컨텐츠</a>
        <a href="video-generators.html">영상 생성</a>
        <button onclick="adminLogout()">🚪 로그아웃</button>
      </div>
    </div>
  </nav>

  <!-- Main Container -->
  <div class="main-container">
    <!-- 설정 섹션 -->
    <div class="card">
      <h2 class="card-title">⚙️ 설정</h2>
      <!-- API 키, 파일 업로드, 텍스트 입력 등 -->
    </div>

    <!-- 진행 상황 섹션 -->
    <div class="card" id="progressCard" style="display: none;">
      <h2 class="card-title">📊 진행 상황</h2>
      <!-- 프로그레스바, 통계 등 -->
    </div>

    <!-- 로그 섹션 -->
    <div class="card" id="logCard" style="display: none;">
      <h2 class="card-title">📝 로그</h2>
      <div class="log-container" id="logContainer"></div>
    </div>

    <!-- 다운로드 섹션 -->
    <div class="download-section" id="downloadSection">
      <!-- 다운로드 버튼 -->
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
  <script>
    // 영상 생성기 로직
  </script>
</body>
</html>
```

### 필수 기능:

1. **Firebase 인증** (관리자 전용)
   ```html
   <script type="module" src="admin/auth-check.js"></script>
   ```

2. **Analytics 추적**
   ```html
   <script src="analytics.js" type="module"></script>
   ```

3. **Gemini API 호출** (영상 생성)
   ```javascript
   async function generateVideo(prompt, apiKey) {
     // Gemini API를 사용한 영상 생성 로직
     // 또는 Gemini로 스크립트 생성 후 다른 API로 영상 생성
   }
   ```

4. **진행 상황 UI**
   - 프로그레스바
   - 통계 (현재/전체/오류/남은시간)
   - 로그 표시

5. **다운로드 기능**
   - MP4, GIF, ZIP 등 영상 파일 다운로드
   - 다중 파일 ZIP 압축

---

## 📋 2단계: video-generators.html에 카드 추가

`video-generators.html` 파일의 `generatorsGrid` 섹션에 새로운 카드를 추가하세요.

### 활성 생성기 카드 템플릿:

```html
<div class="generator-card" onclick="location.href='[파일명].html'">
  <div class="card-icon">[아이콘 이모지]</div>
  <div class="card-title">[생성기 이름]</div>
  <div class="card-description">[간단한 설명]</div>
  <ul class="card-features">
    <li>[주요 기능 1]</li>
    <li>[주요 기능 2]</li>
    <li>[주요 기능 3]</li>
    <li>[주요 기능 4]</li>
  </ul>
  <span class="card-status status-active">운영 중</span>
</div>
```

### Coming Soon 카드 템플릿:

```html
<div class="generator-card disabled">
  <div class="card-icon">[아이콘 이모지]</div>
  <div class="card-title">[생성기 이름]</div>
  <div class="card-description">[간단한 설명]</div>
  <ul class="card-features">
    <li>[예정 기능 1]</li>
    <li>[예정 기능 2]</li>
    <li>[예정 기능 3]</li>
    <li>[예정 기능 4]</li>
  </ul>
  <span class="card-status status-coming-soon">준비 중</span>
</div>
```

### 카드 추가 후:

기존 "영상 생성기 #1", "영상 생성기 #2" 등의 샘플 카드를 제거하고, 실제 생성기 카드로 교체하세요.

---

## 📋 3단계: 관리자 페이지 업데이트

### 3-1. admin/index.html 업데이트

"재밌는 영상 만들기" 섹션을 추가하세요.

```html
<!-- 재밌는 영상 만들기 허브 -->
<a href="../video-generators.html" class="menu-card analytics">
  <div class="card-icon">🎬</div>
  <h2>재밌는 영상 만들기</h2>
  <p>AI 기반 영상 자동 생성 플랫폼</p>
  <div class="features">
    <ul>
      <li>[생성기 1]</li>
      <li>[생성기 2]</li>
      <li>[생성기 3]</li>
      <li>[생성기 4]</li>
    </ul>
  </div>
</a>
```

### 3-2. admin/content.html 업데이트

`serviceStructure` 배열에 새 카테고리를 추가하세요.

```javascript
{
  id: 'video',
  name: '영상 생성',
  icon: '🎬',
  description: 'AI 기반 영상 자동 생성',
  color: '#fce7f3',
  pages: [
    { name: '[파일명]', title: '[생성기 이름]', parent: 'admin', apis: ['Gemini 2.0 Flash'], analytics: true }
  ]
}
```

---

## 🎨 디자인 가이드라인

### 색상 (영상 생성기용):
- Primary Gradient: `linear-gradient(135deg, #ec4899 0%, #8b5cf6 100%)`
- Primary: `#0A0E27`
- Accent Pink: `#ec4899`
- Accent Purple: `#8b5cf6`
- Success: `#10B981`
- Warning: `#F59E0B`
- Error: `#EF4444`

### 타이포그래피:
- 폰트: Inter, -apple-system
- 제목: 700 weight
- 본문: 400-600 weight

### 컴포넌트:
- 카드: 흰색 배경, 16px 둥근 모서리
- 버튼: 핑크-퍼플 그라데이션, hover 효과
- 프로그레스바: 40px 높이, 애니메이션

---

## 📦 필수 라이브러리

### JSZip (파일 압축)
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
```

### Firebase (인증)
```javascript
// admin/auth-check.js에서 자동으로 로드됨
```

### Gemini API
```javascript
// API 키는 사용자 입력 또는 환경변수로 관리
const GEMINI_API_KEY = 'AIzaSy...';
```

---

## 🎥 영상 생성 API 옵션

### 1. Gemini Vision API
- 이미지 기반 영상 프레임 생성
- 스토리보드 자동 생성

### 2. 외부 영상 생성 API
- Runway ML
- Pika Labs
- Stable Video Diffusion

### 3. 조합 방식
- Gemini로 스크립트 생성
- 외부 API로 영상 생성
- FFmpeg로 후처리

---

## ✅ 체크리스트

새 영상 생성기를 추가할 때 다음 사항을 확인하세요:

### 파일 생성:
- [ ] `[생성기명].html` 파일 생성
- [ ] Firebase 인증 스크립트 포함
- [ ] Analytics 추적 스크립트 포함
- [ ] Gemini API 또는 영상 생성 API 통합
- [ ] 진행 상황 UI 구현
- [ ] 다운로드 기능 구현 (MP4, GIF 등)

### UI/UX:
- [ ] Cactus Labs 디자인 시스템 적용
- [ ] 핑크-퍼플 색상 테마 적용
- [ ] 반응형 디자인 (모바일 지원)
- [ ] 로딩 상태 표시
- [ ] 에러 처리
- [ ] 사용자 피드백 (토스트, 알림 등)

### 통합:
- [ ] video-generators.html에 카드 추가
- [ ] admin/index.html 업데이트
- [ ] admin/content.html 업데이트
- [ ] SERVICE_MAP.md 문서 업데이트

### 테스트:
- [ ] 로컬에서 기능 테스트
- [ ] API 키 유효성 검증
- [ ] 파일 업로드/다운로드 테스트
- [ ] 영상 생성 품질 확인
- [ ] 에러 시나리오 테스트
- [ ] 모바일 반응형 테스트

### 배포:
- [ ] Git 커밋
- [ ] Netlify 배포
- [ ] 프로덕션 URL 확인

---

## 🚀 예시: 새 생성기 추가하기

### 예시: "슬라이드쇼 영상 생성기"

#### 1. 파일명
```
slideshow-video-generator.html
```

#### 2. video-generators.html 카드
```html
<div class="generator-card" onclick="location.href='slideshow-video-generator.html'">
  <div class="card-icon">📽️</div>
  <div class="card-title">슬라이드쇼 영상 생성기</div>
  <div class="card-description">이미지를 업로드하여 자동으로 슬라이드쇼 영상 생성</div>
  <ul class="card-features">
    <li>다중 이미지 업로드</li>
    <li>AI 트랜지션 효과</li>
    <li>배경 음악 자동 매칭</li>
    <li>MP4 다운로드</li>
  </ul>
  <span class="card-status status-active">운영 중</span>
</div>
```

#### 3. admin/content.html 추가
```javascript
{
  id: 'video',
  name: '영상 생성',
  icon: '🎬',
  description: 'AI 기반 영상 자동 생성',
  color: '#fce7f3',
  pages: [
    {
      name: 'slideshow-video-generator',
      title: '슬라이드쇼 영상 생성기',
      parent: 'admin',
      apis: ['Gemini 2.0 Flash', 'FFmpeg'],
      analytics: true
    }
  ]
}
```

---

## 🎬 영상 생성기 아이디어

### 쇼츠/릴스 생성기
- 텍스트 입력으로 쇼츠 영상 생성
- 자막 자동 삽입
- 배경 음악 매칭

### 타임랩스 생성기
- 이미지 시퀀스로 타임랩스 생성
- 속도 조절
- 효과 추가

### 밈 영상 생성기
- 템플릿 기반 밈 영상 생성
- 텍스트 커스터마이징
- GIF/MP4 출력

### 인트로 영상 생성기
- 브랜드 로고 + 텍스트
- 애니메이션 효과
- 다양한 템플릿

---

## 📞 지원

문제가 발생하면:
1. 콘솔 로그 확인 (F12)
2. 네트워크 탭에서 API 호출 확인
3. Firebase Auth 상태 확인
4. 영상 파일 크기 및 포맷 확인

---

**Happy Creating! 🎬**
