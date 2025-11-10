# 🔐 GOGWAN 관리자 로그인 및 분석 대시보드 가이드

> 웹사이트 메인 홈에 통합된 관리자 기능 사용 가이드

---

## 📋 개요

GOGWAN 웹서비스 메인 홈(index.html)에 관리자 로그인 기능과 분석 대시보드가 완전히 통합되었습니다. 별도의 관리자 페이지 없이 메인 사이트에서 직접 로그인하여 실시간 통계를 확인할 수 있습니다.

---

## 🚀 사용 방법

### 1. 메인 홈 접속

```bash
# 웹 브라우저로 메인 홈 열기
open /Users/gimgwanho/Desktop/project/civil/web_service/index.html

# 또는 배포된 사이트 접속
# https://your-domain.com
```

### 2. 관리자 로그인

#### Step 1: Admin 버튼 클릭
- 상단 네비게이션 바 우측의 **🔐 Admin** 버튼 클릭
- 로그인 모달이 나타납니다

#### Step 2: 인증 정보 입력
```
이메일: [관리자 이메일]
비밀번호: [관리자 비밀번호]
```

#### Step 3: 로그인
- **로그인** 버튼 클릭
- 인증 성공 시:
  - ✅ "관리자 로그인 성공!" 알림
  - Admin 버튼 → Logout 버튼으로 변경
  - 페이지 하단에 Analytics Dashboard 자동 표시
  - 대시보드로 부드럽게 스크롤

---

## 📊 Analytics Dashboard 기능

로그인 후 자동으로 표시되는 대시보드 섹션입니다.

### **통계 카드** (상단 4개)

1. **👥 총 방문자**: 선택한 기간의 전체 페이지 방문 수
2. **⚡ 기능 실행**: AI 기능 사용 횟수 (보도자료 생성, 배경제거 등)
3. **📥 다운로드**: 파일 다운로드 횟수
4. **⭐ 인기 서비스**: 가장 많이 방문한 페이지

### **기간 필터** (우측 상단)

통계 기간을 선택할 수 있습니다:
- **오늘**: 오늘 하루 데이터
- **최근 7일**: 일주일 데이터
- **최근 30일**: 한 달 데이터 (기본값)
- **전체**: 모든 기간 데이터

기간을 변경하면 모든 통계와 차트가 자동으로 업데이트됩니다.

### **📈 일자별 방문자 추세**

- **타입**: 라인 차트
- **내용**: 날짜별 방문자 수 변화
- **활용**:
  - 성장 추세 확인
  - 특정 날짜 트래픽 급증/감소 분석
  - 이벤트/마케팅 효과 측정

### **🏆 인기 페이지 Top 10**

- **타입**: 순위 리스트
- **내용**: 가장 많이 방문한 페이지 순위
- **표시 정보**:
  - 순위 (1~10위)
  - 페이지 이름 (한글)
  - 방문 횟수

### **📊 시간대별 사용 패턴**

- **타입**: 바 차트
- **내용**: 0시~23시 시간대별 방문 분포
- **활용**:
  - 피크 시간대 파악
  - 서버 리소스 최적화 시간 결정
  - 마케팅 캠페인 최적 시간 선정

### **📅 요일별 사용 패턴**

- **타입**: 바 차트
- **내용**: 월~일 요일별 방문 분포
- **활용**:
  - 평일/주말 사용 패턴 분석
  - 콘텐츠 발행 최적 요일 결정
  - 유지보수 스케줄 계획

---

## 🔓 로그아웃

로그인 상태에서:

1. 상단 네비게이션 바의 **🚪 Logout** 버튼 클릭
2. "로그아웃 되었습니다" 알림
3. Logout 버튼 → Admin 버튼으로 변경
4. Analytics Dashboard 자동 숨김

---

## 🔐 Firebase Authentication 설정

### 관리자 계정 생성 방법

#### 방법 1: Firebase Console에서 직접 생성

1. [Firebase Console](https://console.firebase.google.com/project/gogwan-e79bc) 접속
2. **Authentication** 메뉴 클릭
3. **Users** 탭 → **Add user** 버튼
4. 이메일/비밀번호 입력 후 **Add user**

#### 방법 2: 코드로 생성 (일회성)

```javascript
// 브라우저 콘솔에서 실행 (index.html 열린 상태에서)
import { getAuth, createUserWithEmailAndPassword } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js';

const auth = getAuth();
createUserWithEmailAndPassword(auth, 'admin@example.com', 'your-secure-password')
  .then((userCredential) => {
    console.log('관리자 계정 생성 완료:', userCredential.user);
  })
  .catch((error) => {
    console.error('생성 실패:', error);
  });
```

### 보안 규칙 (권장)

Firebase Console → Authentication → Settings:

```
이메일/비밀번호 인증: 활성화
이메일 열거 방지: 활성화 (보안 강화)
```

Firestore 보안 규칙:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Analytics: 인증된 사용자만 읽기 가능, 모두 쓰기 가능
    match /analytics_page_views/{document=**} {
      allow read: if request.auth != null;
      allow write: if true;
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

    // 보도자료: 인증된 사용자만 수정/삭제, 모두 읽기 가능
    match /press_releases/{document=**} {
      allow read: if true;
      allow write: if request.auth != null;
    }
  }
}
```

---

## 📊 데이터 분석 예시

### 예시 1: 서비스 성과 측정

**목표**: 가장 인기 있는 서비스 파악

1. 로그인 후 대시보드 확인
2. **⭐ 인기 서비스** 카드 확인
   - 예: "AI 보도자료 작성" (500회)
3. **🏆 인기 페이지 Top 10** 리스트 확인
   - 1위: AI 보도자료 작성 (500회)
   - 2위: 배경 제거 (350회)
   - 3위: MBTI 테스트 (280회)

**인사이트**:
- AI 보도자료 작성이 가장 인기
- 이미지 도구(배경제거)도 높은 사용률
- 엔터테인먼트(MBTI)도 상위권

### 예시 2: 사용 시간대 분석

**목표**: 서버 유지보수 최적 시간 찾기

1. **📊 시간대별 사용 패턴** 차트 확인
2. 낮은 사용 시간대 파악
   - 예: 새벽 2~5시

**활용**:
- 서버 유지보수를 새벽 3시에 스케줄
- 사용자 영향 최소화

### 예시 3: 주간 트렌드 분석

**목표**: 마케팅 캠페인 효과 측정

1. **기간 필터**를 "최근 7일"로 설정
2. **📈 일자별 방문자 추세** 확인
   - 월요일: 150명
   - 화요일: 200명 (캠페인 시작)
   - 수요일: 280명
   - 목요일: 320명
   - 금요일: 350명

**인사이트**:
- 캠페인 효과로 화요일부터 급증
- 주말로 갈수록 증가 추세
- 성공적인 캠페인!

---

## 🛠️ 문제 해결

### Q1: "로그인 실패" 에러

**원인**: 잘못된 이메일/비밀번호 또는 계정 미생성

**해결**:
1. Firebase Console → Authentication → Users 확인
2. 계정이 없으면 새로 생성
3. 이메일/비밀번호 재확인

### Q2: 대시보드가 표시되지 않음

**원인**: 인증 상태 확인 중 또는 JavaScript 에러

**해결**:
1. 브라우저 콘솔(F12) 열기
2. 에러 메시지 확인
3. 페이지 새로고침 (Ctrl/Cmd + R)
4. 캐시 삭제 후 재시도

### Q3: 차트가 표시되지 않음

**원인**: Chart.js 로드 실패 또는 데이터 없음

**해결**:
1. 인터넷 연결 확인 (Chart.js CDN 필요)
2. Firebase에 분석 데이터 있는지 확인
3. 콘솔에서 Chart.js 로드 확인

### Q4: 통계 수치가 "-"로 표시됨

**원인**: Firestore에 데이터 없음

**해결**:
1. 실제 서비스 페이지 방문 (데이터 생성)
2. Firebase Console에서 analytics 컬렉션 확인
3. 기간 필터 변경 ("전체"로 설정)

---

## 🎯 관리자 활용 팁

### Tip 1: 정기 모니터링

매주 월요일 오전:
1. 로그인하여 지난 주 통계 확인
2. "최근 7일" 필터로 주간 리포트 확인
3. 전주 대비 증감률 분석

### Tip 2: 월간 리포트

매월 1일:
1. "최근 30일" 필터로 월간 데이터 확인
2. 차트 스크린샷 캡처 (리포트 자료)
3. 인기 페이지 변화 추적

### Tip 3: 실시간 모니터링

이벤트/마케팅 기간 중:
1. "오늘" 필터로 실시간 효과 측정
2. 시간대별 차트로 피크 시간 파악
3. 즉각적인 대응 가능

### Tip 4: 모바일에서 확인

스마트폰/태블릿에서도 접속 가능:
- 반응형 디자인으로 모바일 최적화
- 외출 중에도 대시보드 확인
- 터치 제스처로 차트 인터랙션

---

## 🔗 관련 문서

- **서비스 구조도**: `/web_service/SERVICE_MAP.md`
- **분석 시스템 상세**: `/web_admin/ANALYTICS_README.md`
- **Firebase Console**: https://console.firebase.google.com/project/gogwan-e79bc
- **Chart.js 문서**: https://www.chartjs.org/docs/latest/

---

## 📝 변경 이력

| 날짜 | 변경 내용 |
|------|-----------|
| 2025-11-03 | 관리자 기능 메인 홈 통합 완료 |
| 2025-11-03 | Firebase Authentication 연동 |
| 2025-11-03 | 분석 대시보드 UI 구현 |
| 2025-11-03 | Chart.js 통계 시각화 추가 |
| 2025-11-03 | ADMIN_GUIDE.md 문서 작성 |

---

**작성자**: Claude Code (AI Assistant)
**프로젝트**: GOGWAN Web Service
**버전**: 2.0.0 (통합 버전)
