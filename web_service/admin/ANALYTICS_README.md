# 📊 GOGWAN Analytics System

> 실시간 서비스 사용 통계 및 분석 시스템

---

## 🎯 개요

GOGWAN 웹 서비스의 모든 페이지 방문, 기능 실행, 다운로드 등을 자동으로 추적하고 시각화하는 분석 시스템입니다.

### 주요 기능

- ✅ **실시간 추적**: 페이지 방문, 기능 실행, 다운로드 자동 기록
- ✅ **대시보드**: 직관적인 통계 및 그래프 시각화
- ✅ **일자별 분석**: 날짜별 트렌드 및 패턴 분석
- ✅ **카테고리별 집계**: 서비스 카테고리별 사용 현황
- ✅ **시간대 분석**: 시간대별, 요일별 사용 패턴

---

## 📂 파일 구조

```
web_service/
├── analytics.js              # 추적 라이브러리 (모든 페이지에 포함)
├── index.html               # ✅ 추적 활성화
├── gogwan.html              # ✅ 추적 활성화
├── jamssam.html             # ✅ 추적 활성화
├── create.html              # ✅ 추적 활성화 + 기능 추적
├── ai-problem-solver.html   # ✅ 추적 활성화
├── background-remover.html  # ✅ 추적 활성화
├── banner-maker.html        # ✅ 추적 활성화
├── mbti-test.html           # ✅ 추적 활성화
├── saju-lifetime.html       # ✅ 추적 활성화
├── saju-yearly.html         # ✅ 추적 활성화
└── ... (기타 서비스 페이지)

web_admin/
├── analytics.html           # 📊 분석 대시보드
├── index.html               # 보도자료 관리 (대시보드 링크 포함)
└── ANALYTICS_README.md      # 이 문서
```

---

## 🗄️ Firebase 데이터 구조

### 1. **analytics_page_views** (페이지 방문 추적)

```javascript
{
  pageName: "create",                    // 페이지 이름
  category: "smart-work",                // 카테고리
  timestamp: Timestamp,                  // 방문 시간
  userAgent: "Mozilla/5.0...",          // 브라우저 정보
  referrer: "https://...",              // 유입 경로
  screenWidth: 1920,                    // 화면 너비
  screenHeight: 1080                    // 화면 높이
}
```

**카테고리 종류:**
- `main`: 메인 홈페이지
- `landing`: Gogwan, Jamssam, Fast Rabbit 소개 페이지
- `smart-work`: 스마트 워크 도구 (보도자료, 배너 등)
- `ai-image`: AI 이미지 도구 (배경제거, 증명사진 등)
- `lounge`: 라운지 (MBTI, 사주 등)
- `learning`: 학습 도구 (AI 문제풀이 등)
- `other`: 기타

---

### 2. **analytics_feature_usage** (기능 실행 추적)

```javascript
{
  featureName: "generate-press-release", // 기능 이름
  pageName: "create",                    // 실행한 페이지
  timestamp: Timestamp,                  // 실행 시간
  metadata: {                            // 추가 메타데이터
    category: "정책",
    organization: "서울시청"
  },
  userAgent: "Mozilla/5.0..."           // 브라우저 정보
}
```

**주요 기능 이름:**
- `generate-press-release`: 보도자료 AI 생성
- `remove-background`: 배경 제거
- `generate-id-photo`: 증명사진 생성
- `style-transfer`: 스타일 전환
- `solve-problem`: AI 문제 풀이
- `generate-banner`: 배너 생성
- `pdf-to-ppt`: PDF → PPT 변환
- `mbti-test`: MBTI 테스트
- `saju-lifetime`: 평생운 분석
- `saju-yearly`: 신년운 분석

---

### 3. **analytics_downloads** (다운로드 추적)

```javascript
{
  fileType: "png",                      // 파일 형식
  featureName: "background-remover",    // 관련 기능
  timestamp: Timestamp                  // 다운로드 시간
}
```

**파일 타입:**
- `word`: Word 문서 (보도자료)
- `png`: PNG 이미지 (배경제거, MBTI 결과 등)
- `pptx`: PowerPoint (PDF 변환)
- `jpg`: JPG 이미지

---

### 4. **analytics_errors** (에러 추적)

```javascript
{
  errorType: "API_ERROR",               // 에러 유형
  errorMessage: "Failed to fetch",      // 에러 메시지
  pageName: "create",                   // 발생 페이지
  timestamp: Timestamp,                 // 발생 시간
  userAgent: "Mozilla/5.0...",         // 브라우저 정보
  url: "https://..."                    // 페이지 URL
}
```

---

## 🚀 사용 방법

### 1. 관리자 대시보드 접속

```bash
# 로컬에서 열기
open /Users/gimgwanho/Desktop/project/civil/web_admin/analytics.html

# 또는 웹 브라우저에서 직접 열기
```

### 2. 대시보드 기능

#### **📈 개요 탭**
- **통계 카드**: 총 방문자, 기능 실행, 다운로드, 인기 서비스
- **일자별 방문자 추세**: 라인 차트로 일별 방문 패턴 표시
- **인기 페이지 Top 10**: 가장 많이 방문한 페이지 순위
- **인기 기능 Top 10**: 가장 많이 사용된 기능 순위

#### **📄 페이지별 탭**
- 모든 페이지의 상세 통계
- 방문수, 고유 방문자, 평균 체류시간, 이탈률

#### **⚡ 기능별 탭**
- 각 기능의 사용 통계
- 실행수, 성공률, 평균 처리시간, 에러 발생
- 다운로드 통계 (파일 타입별 도넛 차트)

#### **📊 트렌드 탭**
- **시간대별 사용 패턴**: 0시~23시 시간대별 방문 분포
- **요일별 사용 패턴**: 월~일 요일별 방문 분포
- **카테고리별 성장 추세**: 서비스 카테고리별 시계열 추세

### 3. 기간 필터

대시보드 우측 상단에서 기간 선택:
- **오늘**: 오늘 하루 데이터
- **최근 7일**: 최근 일주일 데이터
- **최근 30일**: 최근 한 달 데이터 (기본값)
- **전체**: 모든 기간 데이터

---

## 🔧 추적 코드 사용법

### 자동 추적 (페이지 로드 시)

모든 페이지에 `analytics.js`가 포함되어 있으면 자동으로 페이지 방문이 추적됩니다.

```html
<head>
    <script src="analytics.js" type="module"></script>
</head>
```

### 수동 추적 (기능 실행 시)

특정 기능 실행 시 수동으로 추적하려면:

```javascript
// 기능 실행 추적
if (window.GogwanAnalytics) {
    window.GogwanAnalytics.trackFeatureUsage(
        'generate-press-release',  // 기능 이름
        'create',                   // 페이지 이름
        {                           // 메타데이터 (선택사항)
            category: '정책',
            organization: '서울시청'
        }
    );
}
```

### 다운로드 추적

```javascript
// 다운로드 추적
if (window.GogwanAnalytics) {
    window.GogwanAnalytics.trackDownload(
        'png',                      // 파일 타입
        'background-remover'        // 기능 이름
    );
}
```

### 에러 추적

```javascript
// 에러 추적
if (window.GogwanAnalytics) {
    window.GogwanAnalytics.trackError(
        'API_ERROR',                // 에러 타입
        error.message,              // 에러 메시지
        'create'                    // 페이지 이름
    );
}
```

---

## 📊 차트 라이브러리

대시보드는 **Chart.js 4.4.0**을 사용하여 그래프를 렌더링합니다.

- **라인 차트**: 일자별 추세, 카테고리별 성장
- **바 차트**: 시간대별 패턴, 요일별 패턴
- **도넛 차트**: 다운로드 파일 타입 분포

CDN:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
```

---

## 🔐 보안 고려사항

### Firestore 보안 규칙 (추천)

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Analytics 컬렉션: 읽기는 관리자만, 쓰기는 모두 허용
    match /analytics_page_views/{document=**} {
      allow read: if request.auth != null;  // 인증된 사용자만 읽기
      allow write: if true;                 // 모든 사용자 쓰기 가능
    }

    match /analytics_feature_usage/{document=**} {
      allow read: if request.auth != null;
      allow write: if true;
    }

    match /analytics_downloads/{document=**} {
      allow read: if request.auth != null;
      allow write: if true;
    }

    match /analytics_errors/{document=**} {
      allow read: if request.auth != null;
      allow write: if true;
    }
  }
}
```

### 개인정보 보호

현재 시스템은 다음 정보만 수집합니다:
- ✅ 페이지 이름 (개인정보 없음)
- ✅ 브라우저 정보 (User-Agent)
- ✅ 화면 해상도
- ✅ 리퍼러 URL
- ❌ IP 주소 (수집 안 함)
- ❌ 사용자 식별 정보 (수집 안 함)
- ❌ 개인 데이터 (수집 안 함)

---

## 🔍 데이터 분석 예시

### 1. 가장 인기 있는 서비스 찾기

**개요 탭 → 인기 페이지 Top 10** 확인
- 1위: AI 보도자료 작성 (500회)
- 2위: 배경 제거 (350회)
- 3위: MBTI 테스트 (280회)

### 2. 사용 패턴 분석

**트렌드 탭 → 시간대별 사용 패턴** 확인
- 피크 시간: 오전 10~11시, 오후 2~3시
- 저조 시간: 새벽 1~6시

**트렌드 탭 → 요일별 사용 패턴** 확인
- 평일(월~금): 높은 사용량
- 주말(토~일): 낮은 사용량

### 3. 기능별 성과 측정

**기능별 탭 → 기능별 사용 통계** 확인
- AI 보도자료 생성: 250회
- 배경 제거: 200회
- AI 문제 풀이: 180회

### 4. 성장 추세 확인

**개요 탭 → 일자별 방문자 추세** 그래프 확인
- 11월 1일: 150명
- 11월 2일: 180명
- 11월 3일: 220명
- 👉 **증가 추세!**

---

## 🛠️ 문제 해결

### 데이터가 표시되지 않음

1. **Firebase 연결 확인**
   - 브라우저 콘솔(F12) 확인
   - Firebase 프로젝트 ID 확인
   - Firestore Database 활성화 확인

2. **컬렉션 확인**
   - Firebase Console에서 `analytics_page_views` 컬렉션 존재 확인
   - 데이터가 실제로 기록되고 있는지 확인

3. **보안 규칙 확인**
   - Firestore 보안 규칙이 너무 제한적이지 않은지 확인

### 차트가 표시되지 않음

1. **Chart.js CDN 로드 확인**
   - 브라우저 콘솔에서 Chart.js 로드 에러 확인
   - 인터넷 연결 확인

2. **데이터 형식 확인**
   - 날짜 데이터가 올바른 형식인지 확인
   - 숫자 데이터가 올바르게 파싱되는지 확인

### 추적이 작동하지 않음

1. **analytics.js 로드 확인**
   - 브라우저 콘솔에서 `window.GogwanAnalytics` 객체 존재 확인
   - `console.log(window.GogwanAnalytics)` 실행

2. **Firebase SDK 로드 확인**
   - Firebase CDN 연결 확인
   - 네트워크 탭에서 Firebase 요청 확인

---

## 📈 향후 개선 계획

### Phase 1 (완료)
- ✅ 기본 추적 시스템 구축
- ✅ 대시보드 UI 개발
- ✅ 주요 페이지에 추적 코드 적용
- ✅ 차트 시각화

### Phase 2 (계획 중)
- ⏳ 사용자 세션 추적 (평균 체류시간, 이탈률)
- ⏳ 실시간 대시보드 (WebSocket 연동)
- ⏳ 알림 시스템 (일일 리포트 이메일)
- ⏳ A/B 테스트 기능

### Phase 3 (장기)
- 💡 AI 기반 추천 (사용 패턴 분석)
- 💡 예측 분석 (미래 트렌드 예측)
- 💡 비용 분석 (API 사용량 기반)
- 💡 사용자 피드백 연동

---

## 📞 문의 및 지원

### 문서
- **Firebase Console**: https://console.firebase.google.com/project/gogwan-e79bc
- **Chart.js 문서**: https://www.chartjs.org/docs/latest/
- **Firestore 문서**: https://firebase.google.com/docs/firestore

### 주요 파일
- `web_service/analytics.js`: 추적 라이브러리
- `web_admin/analytics.html`: 분석 대시보드
- `web_admin/index.html`: 보도자료 관리
- `web_service/SERVICE_MAP.md`: 전체 서비스 구조도

---

**버전**: 1.0.0
**최종 업데이트**: 2025-11-03
**작성자**: Claude Code (AI Assistant)
