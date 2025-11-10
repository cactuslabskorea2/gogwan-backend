# GOGWAN 웹 서비스

Flutter 앱과 동일한 기능을 제공하는 웹 서비스입니다.

## 📋 기능

### ✅ 구현된 기능
- 홈 화면 (서비스 카드)
- 보도자료 목록 조회
- 보도자료 검색
- **AI 보도자료 작성** (Google Gemini API)
- 보도자료 상세보기
- 보도자료 삭제
- 실시간 Firestore 연동

## 🚀 사용 방법

### 1. 웹 브라우저로 열기

```bash
# 방법 1: 터미널에서
open /Users/gimgwanho/Desktop/project/civil/web_service/index.html

# 방법 2: 브라우저에서 직접
# Chrome, Safari, Firefox 등에서 index.html 파일을 드래그&드롭
```

### 2. 홈 화면

- **보도자료 작성** 카드 클릭 → 보도자료 목록으로 이동
- **증명사진 생성** (미구현)

### 3. 보도자료 목록

- 검색바에서 제목, 내용, 카테고리로 검색
- 보도자료 카드 클릭 → 상세보기
- 우측 하단 "AI로 작성하기" 버튼 → 작성 페이지

### 4. AI 보도자료 작성

#### 입력 항목:
1. **카테고리**: 정책 / 행사 / 발표
2. **주제** (필수): 보도자료의 핵심 주제
3. **핵심 내용** (필수): 반드시 포함되어야 할 정보
4. **추가 정보** (선택): 배경, 기대효과, 문의처 등

#### 작성 과정:
1. 필수 항목 입력
2. "AI로 보도자료 생성하기" 버튼 클릭
3. AI가 전문적인 보도자료 생성 (15-30초 소요)
4. 생성된 결과 확인
5. 필요시 수정 요청
6. 우측 상단 "저장" 버튼으로 Firestore에 저장

### 5. 보도자료 상세보기

- 보도자료 전체 내용 확인
- 카테고리, 작성일, 작성자, 조회수 표시
- AI 생성 여부 표시
- 하단 "삭제" 버튼으로 삭제 가능

## 🔧 기술 스택

### Frontend
- **HTML5** + **CSS3** + **Vanilla JavaScript**
- Material Design 3 디자인 시스템
- Tailwind CSS 컬러 팔레트

### Backend
- **Firebase Firestore**: 데이터베이스
- **Google Gemini API**: AI 보도자료 생성

### API
- Firebase SDK 10.7.1 (CDN)
- Gemini Pro API

## 🔒 Firebase 설정

### Firestore 컬렉션 구조

```
press_releases (컬렉션)
├── document_id (자동 생성)
    ├── title (string)
    ├── subtitle (string)
    ├── category (string)
    ├── content (string)
    ├── authorId (string)
    ├── authorName (string)
    ├── isAiGenerated (boolean)
    ├── views (number)
    ├── createdAt (timestamp)
    └── updatedAt (timestamp)
```

### 보안 규칙

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /press_releases/{document=**} {
      allow read, write: if request.time < timestamp.date(2026, 12, 31);
    }
  }
}
```

## 📱 Flutter 앱과의 차이점

### 동일한 기능
- ✅ AI 보도자료 생성 (Gemini API)
- ✅ 보도자료 목록/검색
- ✅ 보도자료 상세보기
- ✅ Firestore 연동

### 웹 전용 기능
- 🌐 웹 브라우저에서 즉시 사용 가능
- 🌐 설치 불필요
- 🌐 크로스 플랫폼 (Windows, Mac, Linux)

### 미구현 기능
- ❌ 증명사진 생성 (카메라 접근 필요)
- ❌ Google/Apple 로그인

## 🎨 디자인

Flutter 앱과 동일한 디자인:
- 그라디언트 배경 (blue-50 → white)
- Material Design 3 카드 스타일
- 반응형 레이아웃
- 부드러운 애니메이션

## 📂 파일 구조

```
web_service/
├── index.html              # 홈 화면
├── press-release.html      # 보도자료 목록
├── create.html             # AI 보도자료 작성
├── detail.html             # 보도자료 상세보기
├── styles.css              # 공통 스타일시트
└── README.md               # 이 파일
```

## 🔐 API 키 설정

### Gemini API
- `create.html` 파일의 `GEMINI_API_KEY` 변수
- 현재값: `AIzaSyAMPy1HPTW54Gs7G_wes6zFXOyyhiNaWuQ`

### Firebase
- 모든 HTML 파일의 `firebaseConfig` 객체
- 프로젝트 ID: `gogwan-e79bc`

## 🌐 배포 방법 (선택사항)

### Firebase Hosting으로 배포

```bash
# Firebase CLI 설치
npm install -g firebase-tools

# 로그인
firebase login

# 초기화
cd /Users/gimgwanho/Desktop/project/civil/web_service
firebase init hosting

# 배포
firebase deploy --only hosting
```

배포 후 `https://gogwan-e79bc.web.app`에서 접속 가능

## 📞 문제 해결

### AI 생성이 안 됨
- Gemini API 키 확인
- 인터넷 연결 확인
- 브라우저 콘솔(F12) 에러 확인

### Firebase 연결 오류
- Firebase 프로젝트 ID 확인
- Firestore Database 활성화 확인
- 보안 규칙 확인

### 데이터가 안 보임
- 브라우저 콘솔(F12) 확인
- Firestore 컬렉션 이름 확인 (`press_releases`)
- 네트워크 연결 확인

## 📖 참고

- Firebase Console: https://console.firebase.google.com/project/gogwan-e79bc
- Gemini API: https://ai.google.dev/
- Firestore 문서: https://firebase.google.com/docs/firestore

## 🔗 관련 프로젝트

- **Flutter 앱**: `/lib` 폴더
- **웹 관리 페이지**: `/web_admin` 폴더 (관리자 전용)
- **웹 서비스**: `/web_service` 폴더 (이 폴더)
