# GOGWAN 보도자료 관리 웹페이지

## 📋 기능

### ✅ 구현된 기능
- 보도자료 작성
- 보도자료 목록 조회
- 보도자료 수정
- 보도자료 삭제
- 실시간 Firestore 연동
- 카테고리 관리 (정책, 행사, 발표)
- 작성자 정보 관리
- 조회수 표시

## 🚀 사용 방법

### 1. 파일 열기
```bash
# 웹 브라우저로 파일 열기
open /Users/gimgwanho/Desktop/project/civil/web_admin/index.html

# 또는 브라우저에서 직접 열기
# Chrome, Safari, Firefox 등에서 index.html 파일을 드래그&드롭
```

### 2. 보도자료 작성
1. 왼쪽 폼에 정보 입력:
   - 제목
   - 부제목
   - 카테고리 선택 (정책/행사/발표)
   - 내용
   - 작성자 이름

2. "보도자료 등록" 버튼 클릭

3. 자동으로 Firestore에 저장됨

### 3. 보도자료 수정
1. 오른쪽 목록에서 수정할 보도자료의 "✏️ 수정" 버튼 클릭
2. 왼쪽 폼에 기존 데이터가 자동으로 채워짐
3. 내용 수정 후 "💾 수정 완료" 버튼 클릭

### 4. 보도자료 삭제
1. 오른쪽 목록에서 삭제할 보도자료의 "🗑️ 삭제" 버튼 클릭
2. 확인 메시지에서 "확인" 클릭

## 🔧 Firestore 설정

### Firestore 컬렉션 구조
```
press_releases (컬렉션)
├── document_id (자동 생성)
    ├── title (string)
    ├── subtitle (string)
    ├── category (string)
    ├── content (string)
    ├── authorName (string)
    ├── isAiGenerated (boolean)
    ├── views (number)
    ├── createdAt (timestamp)
    └── updatedAt (timestamp)
```

### 보안 규칙 설정 (개발용)
Firebase Console → Firestore Database → 규칙 탭

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /press_releases/{document=**} {
      allow read, write: if request.time < timestamp.date(2026, 1, 1);
    }
  }
}
```

## 📱 Flutter 앱 연동

이 웹페이지로 작성한 보도자료는 자동으로 Flutter 앱의 `PressReleaseProvider`에서 불러올 수 있습니다.

```dart
// lib/providers/press_release_provider.dart
await fetchReleases(); // Firestore에서 보도자료 목록 가져오기
```

## 🎨 디자인 특징

- 그라디언트 배경 (보라색 계열)
- 카드 기반 레이아웃
- 반응형 디자인 (모바일 지원)
- 부드러운 애니메이션
- 직관적인 UI/UX

## 🔒 보안 주의사항

**⚠️ 중요**: 현재 설정은 개발/테스트용입니다!

프로덕션 배포 시:
1. Firebase Authentication으로 관리자 로그인 추가
2. Firestore 보안 규칙 강화
3. HTTPS 호스팅 필요

## 🌐 배포 방법 (선택사항)

### Firebase Hosting으로 배포

```bash
# Firebase CLI 설치
npm install -g firebase-tools

# 로그인
firebase login

# 초기화
cd /Users/gimgwanho/Desktop/project/civil/web_admin
firebase init hosting

# 배포
firebase deploy --only hosting
```

배포 후 `https://your-project-id.web.app`에서 접속 가능

## 📞 문제 해결

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
- Firestore 문서: https://firebase.google.com/docs/firestore

## 🔐 인증 설정

이 프로젝트는 Google 로그인과 Apple 로그인을 지원합니다.
Firebase Console → Authentication에서 활성화됨.
