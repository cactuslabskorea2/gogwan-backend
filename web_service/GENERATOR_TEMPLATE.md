# 📝 교육 컨텐츠 생성기 추가 가이드

이 문서는 새로운 교육 컨텐츠 생성기를 추가하는 방법을 설명합니다.

---

## 🎯 생성기 추가 3단계

### 1단계: 생성기 HTML 파일 생성
### 2단계: content-generators.html에 카드 추가
### 3단계: 관리자 페이지 업데이트

---

## 📋 1단계: 생성기 HTML 파일 생성

`lecture-generator.html`을 참고하여 새로운 생성기를 만드세요.

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
        <a href="content-generators.html">컨텐츠 생성기</a>
        <button onclick="adminLogout()">🚪 로그아웃</button>
      </div>
    </div>
  </nav>

  <!-- Main Container -->
  <div class="main-container">
    <!-- 설정 섹션 -->
    <div class="card">
      <h2 class="card-title">⚙️ 설정</h2>
      <!-- API 키, 파일 업로드 등 -->
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
    // 생성기 로직
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

3. **Gemini API 호출**
   ```javascript
   async function generateContent(prompt, apiKey) {
     const response = await fetch(
       `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${apiKey}`,
       {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify({
           contents: [{ parts: [{ text: prompt }] }]
         })
       }
     );
     const data = await response.json();
     return data.candidates[0].content.parts[0].text;
   }
   ```

4. **진행 상황 UI**
   - 프로그레스바
   - 통계 (현재/전체/오류/남은시간)
   - 로그 표시

5. **다운로드 기능**
   - ZIP 파일 생성 (JSZip 사용)
   - JSON, CSV, 이미지 등 다양한 형식 지원

---

## 📋 2단계: content-generators.html에 카드 추가

`content-generators.html` 파일의 `generatorsGrid` 섹션에 새로운 카드를 추가하세요.

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

기존 "생성기 #2", "생성기 #3" 등의 샘플 카드를 제거하고, 실제 생성기 카드로 교체하세요.

---

## 📋 3단계: 관리자 페이지 업데이트

### 3-1. admin/index.html 업데이트

"교육 컨텐츠 생성기" 섹션을 추가하거나, 기존 섹션에 링크를 업데이트하세요.

```html
<!-- 교육 컨텐츠 생성기 허브 -->
<a href="../content-generators.html" class="menu-card">
  <div class="card-icon">🎓</div>
  <h2>교육 컨텐츠 생성기</h2>
  <p>AI 기반 교육 컨텐츠 자동 생성 플랫폼</p>
  <div class="features">
    <ul>
      <li>AIVOCA 강의 생성기</li>
      <li>[새 생성기 1]</li>
      <li>[새 생성기 2]</li>
      <li>[새 생성기 3]</li>
    </ul>
  </div>
</a>
```

### 3-2. admin/content.html 업데이트

`serviceStructure` 배열의 `learning` 카테고리에 새 페이지를 추가하세요.

```javascript
{
  id: 'learning',
  name: '학습도구',
  icon: '📚',
  description: 'AI 기반 학습 및 문제풀이',
  color: '#ffedd5',
  pages: [
    { name: 'ai-problem-solver', title: 'AI 문제풀이', parent: 'index', apis: ['Gemini 2.5 Pro'], analytics: true },
    { name: 'gemsem', title: '젬셈 AI 교육 (MVP)', parent: 'index', apis: ['Gemini 2.0 Flash'], analytics: false },
    { name: 'gemsem-full', title: '젬셈 AI 교육 (Full)', parent: 'index', apis: ['Gemini 2.0 Flash'], analytics: false },
    { name: 'lecture-generator', title: 'AIVOCA 강의 생성기', parent: 'admin', apis: ['Gemini 2.0 Flash', 'TTS'], analytics: true },
    // 👇 여기에 새 생성기 추가
    { name: '[파일명]', title: '[생성기 이름]', parent: 'admin', apis: ['Gemini 2.0 Flash'], analytics: true }
  ]
}
```

---

## 🎨 디자인 가이드라인

### 색상:
- Primary: `#0A0E27`
- Secondary: `#6366F1`
- Accent: `#8B5CF6`
- Success: `#10B981`
- Warning: `#F59E0B`
- Error: `#EF4444`

### 타이포그래피:
- 폰트: Inter, -apple-system
- 제목: 700 weight
- 본문: 400-600 weight

### 컴포넌트:
- 카드: 흰색 배경, 16px 둥근 모서리
- 버튼: 그라데이션, hover 효과
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

## ✅ 체크리스트

새 생성기를 추가할 때 다음 사항을 확인하세요:

### 파일 생성:
- [ ] `[생성기명].html` 파일 생성
- [ ] Firebase 인증 스크립트 포함
- [ ] Analytics 추적 스크립트 포함
- [ ] Gemini API 통합
- [ ] 진행 상황 UI 구현
- [ ] 다운로드 기능 구현

### UI/UX:
- [ ] Cactus Labs 디자인 시스템 적용
- [ ] 반응형 디자인 (모바일 지원)
- [ ] 로딩 상태 표시
- [ ] 에러 처리
- [ ] 사용자 피드백 (토스트, 알림 등)

### 통합:
- [ ] content-generators.html에 카드 추가
- [ ] admin/index.html 업데이트
- [ ] admin/content.html 업데이트
- [ ] SERVICE_MAP.md 문서 업데이트

### 테스트:
- [ ] 로컬에서 기능 테스트
- [ ] API 키 유효성 검증
- [ ] 파일 업로드/다운로드 테스트
- [ ] 에러 시나리오 테스트
- [ ] 모바일 반응형 테스트

### 배포:
- [ ] Git 커밋
- [ ] Netlify 배포
- [ ] 프로덕션 URL 확인

---

## 🚀 예시: 새 생성기 추가하기

### 예시: "단어장 문제 생성기"

#### 1. 파일명
```
vocabulary-quiz-generator.html
```

#### 2. content-generators.html 카드
```html
<div class="generator-card" onclick="location.href='vocabulary-quiz-generator.html'">
  <div class="card-icon">📚</div>
  <div class="card-title">단어장 문제 생성기</div>
  <div class="card-description">단어장을 기반으로 다양한 유형의 퀴즈 자동 생성</div>
  <ul class="card-features">
    <li>CSV 파일 배치 처리</li>
    <li>객관식/주관식 문제 생성</li>
    <li>난이도 자동 조절</li>
    <li>JSON + PDF 다운로드</li>
  </ul>
  <span class="card-status status-active">운영 중</span>
</div>
```

#### 3. admin/content.html 추가
```javascript
{
  name: 'vocabulary-quiz-generator',
  title: '단어장 문제 생성기',
  parent: 'admin',
  apis: ['Gemini 2.0 Flash'],
  analytics: true
}
```

---

## 📞 지원

문제가 발생하면:
1. 콘솔 로그 확인 (F12)
2. 네트워크 탭에서 API 호출 확인
3. Firebase Auth 상태 확인

---

**Happy Generating! 🎉**
