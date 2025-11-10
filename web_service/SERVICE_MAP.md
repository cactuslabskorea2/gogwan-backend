# 🗺️ Cactus Labs 웹서비스 전체 맵

> 마지막 업데이트: 2025-01-06
> 총 서비스: 25개 페이지

---

## 📊 서비스 통계

| 항목 | 수량 |
|------|------|
| 총 페이지 | 25개 |
| AI 사용 페이지 | 14개 |
| Analytics 연동 | 23개 |
| 파일 업로드 지원 | 11개 |
| 파일 다운로드 지원 | 11개 |

---

## 🏠 1. 랜딩 & 허브 페이지 (4개)

### index.html - 메인 홈페이지
- **URL**: `/`
- **목적**: 서비스 전체 소개 및 진입점
- **기능**:
  - 관리자 로그인 버튼
  - 주요 서비스 카테고리 소개
  - Analytics 실시간 통계

### gogwan.html - 공무중이상무 소개
- **URL**: `/gogwan.html`
- **목적**: 공무원 업무 지원 플랫폼 소개
- **연결**:
  - Smart Work (업무도구)
  - AI Image (이미지 도구)
  - Lounge (라운지)

### jamssam.html - 잠쌤 학습 플랫폼
- **URL**: `/jamssam.html`
- **목적**: AI 학습 도구 허브
- **연결**:
  - AI Problem Solver (문제풀이)
  - Summary Notes (예정)
  - Concept Explanation (예정)

### fast-rabbit.html - 패스트 래빗
- **URL**: `/fast-rabbit.html`
- **목적**: 한글 타자 자격증 대비 플랫폼
- **상태**: Coming Soon (준비 중)

---

## 💼 2. AI 업무도구 (6개)

### smart-work.html - 업무도구 허브
- **URL**: `/smart-work.html`
- **목적**: AI 업무 자동화 도구 모음
- **연결**:
  - AI 보도자료 작성
  - PDF→PPT 변환
  - 배너 디자이너

### create.html - AI 보도자료 작성기
- **URL**: `/create.html`
- **AI**: Gemini 2.0 Flash
- **기능**:
  - 카테고리 선택 (정책/행사/공고)
  - AI 보도자료 자동 생성
  - 필수 필드 검증
  - Firebase 저장

### press-release.html - 보도자료 목록
- **URL**: `/press-release.html`
- **기능**:
  - Firestore 데이터 조회
  - 보도자료 목록 표시
  - 클립보드 복사
  - 소셜 공유 (카카오톡, SMS)

### press-release-result.html - 보도자료 결과
- **URL**: `/press-release-result.html`
- **기능**: 생성된 보도자료 상세 보기

### banner-maker.html - 배너 디자이너
- **URL**: `/banner-maker.html`
- **AI**: Gemini 2.5 Flash Image
- **기능**:
  - AI 배너 디자인 생성
  - 크기 설정 (미터 단위)
  - 텍스트 커스터마이징
  - PNG/SVG 다운로드

### pdf-to-ppt.html - PDF→PPT 변환기
- **URL**: `/pdf-to-ppt.html`
- **AI**: Gemini 2.0 Flash
- **기능**:
  - PDF 파일 업로드 (드래그앤드롭)
  - PPT 변환 (1-2분)
  - 슬라이드 개수 표시

---

## 🎨 3. AI 이미지 도구 (7개)

### ai-image.html - 이미지 도구 허브
- **URL**: `/ai-image.html`
- **목적**: AI 이미지 처리 도구 모음
- **연결**:
  - 배경 제거
  - 증명사진 생성
  - AI 포토 메이커

### background-remover.html - 배경 제거
- **URL**: `/background-remover.html`
- **AI**: Gemini 2.5 Flash Image
- **기능**:
  - AI 자동 배경 제거
  - 이미지 회전
  - Before/After 비교
  - PNG 다운로드

### id-photo.html - 증명사진 생성기
- **URL**: `/id-photo.html`
- **AI**: Gemini 2.5 Flash Image
- **기능**:
  - AI 증명사진 생성
  - 배경색 선택 (흰색/파란색/회색)
  - 자동 프레이밍

### style-select.html - 스타일 선택
- **URL**: `/style-select.html`
- **상태**: 유지보수 중 (현재 비활성)
- **목적**: AI 이미지 스타일 선택

### style-transfer.html - 스타일 전환
- **URL**: `/style-transfer.html`
- **AI**: Gemini 2.5 Flash Image
- **기능**:
  - 예술 스타일 변환
  - 드래그앤드롭 지원
  - Before/After 비교

### ghibli-style.html - 지브리 스타일 변환
- **URL**: `/ghibli-style.html`
- **AI**: Gemini 2.5 Flash Image
- **기능**:
  - 지브리 애니메이션 스타일 변환
  - 원클릭 변환
  - Before/After 비교

---

## 🎮 4. 라운지 (엔터테인먼트) (4개)

### lounge.html - 라운지 허브
- **URL**: `/lounge.html`
- **목적**: 재미 콘텐츠 모음
- **연결**:
  - MBTI 테스트
  - 평생운 (사주)
  - 신년운세 (사주)

### mbti-test.html - MBTI 성격 테스트
- **URL**: `/mbti-test.html`
- **기능**: 16가지 성격 유형 테스트
- **파일 크기**: 40,055 tokens (대용량)

### saju-lifetime.html - 평생운 사주
- **URL**: `/saju-lifetime.html`
- **AI**: Gemini 2.0 Flash
- **기능**:
  - 생년월일시 입력
  - 음력/양력 선택
  - 사주 4기둥 표시
  - 평생 운세 AI 해석

### saju-yearly.html - 신년운세 사주
- **URL**: `/saju-yearly.html`
- **AI**: Gemini 2.0 Flash
- **기능**:
  - 생년월일시 입력
  - 연도 선택 (올해/내년)
  - 사주 4기둥 표시
  - 연간 운세 AI 해석

---

## 📚 5. 학습 도구 (4개)

### ai-problem-solver.html - AI 문제풀이
- **URL**: `/ai-problem-solver.html`
- **AI**: Gemini 2.5 Pro
- **기능**:
  - 사진 기반 문제 인식
  - 단계별 풀이 설명
  - 개념 설명
  - 일일 사용 제한 (3회 무료)
  - PNG 다운로드

### gemsem.html - 젬셈 AI 교육 (MVP)
- **URL**: `/gemsem.html`
- **AI**: Gemini 2.0 Flash
- **기능**:
  - PDF 교재 업로드
  - AI 개념 추출
  - 개념 검증 워크플로우
  - 상태 추적 (업로드됨/처리중/완료)

### gemsem-full.html - 젬셈 AI 교육 (Full)
- **URL**: `/gemsem-full.html`
- **AI**: Gemini 2.0 Flash
- **기능**:
  - 교재 + 문제집 관리
  - AI 개념 추출
  - AI 문제 추출
  - 유사 문제 생성 (AI 파생)
  - 문제 해설 생성
  - 템플릿/파생 문제 추적
  - 드래그앤드롭 업로드

### lecture-generator.html - AIVOCA 강의 생성기 🆕
- **URL**: `/lecture-generator.html`
- **AI**: Gemini 2.0 Flash + TTS
- **접근**: 관리자 전용 (Firebase Auth)
- **기능**:
  - CSV 배치 처리
  - 강의 JSON 생성
  - 한국어 TTS 음성 생성
  - 진행률 추적 (ETA)
  - PCM→WAV 변환
  - ZIP 다운로드
  - Rate Limiting (1초 지연)

---

## 🔐 6. 관리자 페이지 (6개)

### admin/login.html - 관리자 로그인
- **URL**: `/admin/login.html`
- **기능**:
  - Firebase Authentication
  - returnUrl 지원
  - 자동 리다이렉트

### admin/index.html - 관리자 대시보드
- **URL**: `/admin/index.html`
- **기능**:
  - 실시간 통계 (30일)
  - 서비스 바로가기
  - Firebase 데이터 조회

### admin/analytics.html - 분석 대시보드
- **URL**: `/admin/analytics.html`
- **기능**:
  - 페이지별 방문자
  - 기능별 사용 현황
  - 시간대/요일별 트렌드
  - 차트 시각화

### admin/api-console.html - API & 콘솔 관리
- **URL**: `/admin/api-console.html`
- **기능**:
  - Gemini API 키 관리
  - Firebase 콘솔 링크
  - Google Cloud 관리
  - 배포 관리

### admin/content.html - 콘텐츠 관리
- **URL**: `/admin/content.html`
- **기능**:
  - 서비스 계층 구조 표시
  - 페이지별 정보 관리
  - API 사용 현황
  - 카테고리별 분류

### admin/press-release.html - 보도자료 관리
- **URL**: `/admin/press-release.html`
- **기능**:
  - 보도자료 작성/수정
  - 카테고리 분류
  - 조회수 통계

### admin/users.html - 사용자 관리
- **URL**: `/admin/users.html`
- **기능**:
  - 사용자 활동 목록
  - UserAgent 분석
  - 접속 기기 통계

### admin/settings.html - 시스템 설정
- **URL**: `/admin/settings.html`
- **기능**:
  - 환경 변수 확인
  - Firebase 연결 상태
  - 에러 로그 조회

---

## 🔗 서비스 계층 구조

```
index.html (메인)
├─ gogwan.html (공무중이상무)
│  ├─ smart-work.html (업무도구)
│  │  ├─ create.html (보도자료)
│  │  ├─ banner-maker.html (배너)
│  │  └─ pdf-to-ppt.html (PDF변환)
│  ├─ ai-image.html (이미지도구)
│  │  ├─ background-remover.html
│  │  ├─ id-photo.html
│  │  ├─ style-select.html
│  │  │  ├─ style-transfer.html
│  │  │  └─ ghibli-style.html
│  └─ lounge.html (라운지)
│     ├─ mbti-test.html
│     ├─ saju-lifetime.html
│     └─ saju-yearly.html
├─ jamssam.html (잠쌤)
│  └─ ai-problem-solver.html
├─ fast-rabbit.html
├─ gemsem.html (젬셈 MVP)
└─ gemsem-full.html (젬셈 Full)

admin/ (관리자 - 독립)
└─ lecture-generator.html (관리자 전용)
```

---

## 🎯 AI 모델 사용 현황

| AI 모델 | 사용 페이지 |
|---------|------------|
| **Gemini 2.0 Flash** | create, pdf-to-ppt, saju-lifetime, saju-yearly, gemsem, gemsem-full, lecture-generator |
| **Gemini 2.5 Flash Image** | banner-maker, background-remover, id-photo, style-transfer, ghibli-style |
| **Gemini 2.5 Pro** | ai-problem-solver |
| **TTS (Gemini)** | lecture-generator |

---

## 📱 주요 기능별 분류

### 파일 업로드 지원 (11개)
- ai-problem-solver, background-remover, id-photo, ghibli-style, style-transfer
- pdf-to-ppt, banner-maker
- gemsem, gemsem-full
- lecture-generator

### 파일 다운로드 지원 (11개)
- ai-problem-solver (PNG)
- background-remover, id-photo, ghibli-style, style-transfer (PNG)
- banner-maker (PNG, SVG)
- pdf-to-ppt (PPT)
- gemsem-full (문제/해설)
- lecture-generator (ZIP: JSON + WAV)

### 소셜 공유 지원 (2개)
- press-release (카카오톡, SMS, 링크)
- press-release-result (카카오톡, SMS, 링크)

### 일일 사용 제한 (1개)
- ai-problem-solver (3회/일)

---

## 🔧 백엔드 API

**주요 엔드포인트**: `https://gogwan-backend-818506848351.asia-northeast3.run.app/api/`

사용 페이지:
- background-remover
- id-photo
- ghibli-style
- style-transfer
- create
- banner-maker
- pdf-to-ppt
- ai-problem-solver
- saju-lifetime
- saju-yearly

---

## 📊 Analytics 통합

**모듈**: `analytics.js`

**추적 항목**:
- 페이지 뷰
- 기능 사용
- 다운로드
- 에러

**미연동 페이지** (2개):
- gemsem.html
- gemsem-full.html

---

## 🆕 최근 추가 (2025-01-06)

1. **lecture-generator.html** - AIVOCA 강의 생성기
   - CSV 배치 처리
   - Gemini AI + TTS 통합
   - 관리자 전용 (Firebase Auth)
   - admin/index.html에 메뉴 추가
   - admin/content.html에 서비스 정보 추가

2. **gemsem-full.html** 관리자 메뉴 추가
   - admin/index.html에 "젬셈 AI 교육 플랫폼" 카드 추가

---

## 📝 TODO / 예정 기능

### Coming Soon (표시만 되어 있음)
1. **fast-rabbit.html**
   - 타자 연습
   - 모의고사
   - 분석

2. **jamssam.html**
   - 요약 노트
   - 개념 설명

3. **smart-work.html**
   - 실시간 전사
   - 음성 파일 변환
   - 회의록 생성

4. **lounge.html**
   - 심리 테스트

### 개선 필요
1. **style-select.html** - 현재 유지보수 중
2. **gemsem.html / gemsem-full.html** - Analytics 추가 필요

---

## 🔐 보안 & 접근 제어

### 관리자 전용 페이지 (Firebase Auth)
- `/admin/*` - 모든 관리자 페이지
- `/lecture-generator.html` - 강의 생성기

### 공개 페이지
- 나머지 모든 페이지

---

## 🚀 배포 정보

- **호스팅**: Netlify
- **도메인**: https://cactuslabskorea.com
- **프로젝트**: gorgeous-cocada-91bd09
- **백엔드**: Google Cloud Run

---

**마지막 업데이트**: 2025-01-06
**총 페이지**: 25개
**AI 통합**: 14개
**관리자 도구**: 7개
