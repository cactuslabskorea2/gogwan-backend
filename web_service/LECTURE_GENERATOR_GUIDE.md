# 🎓 AIVOCA 강의 생성기 통합 가이드

## 📌 개요

AITUTOR 프로젝트의 강의 생성기가 **Cactus Labs Web Service**에 성공적으로 통합되었습니다!

### 통합 내용
- ✅ `lecture-generator.html` 페이지 생성
- ✅ 메인 네비게이션에 링크 추가
- ✅ Cactus Labs 디자인 시스템 적용
- ✅ 브라우저 기반 독립 실행 (서버 불필요)

---

## 🚀 빠른 시작

### 1. 웹 서비스 접속
```
http://localhost:8080/lecture-generator.html
```

또는 배포된 사이트:
```
https://your-site.netlify.app/lecture-generator.html
```

### 2. 메인 페이지에서 접근
- 메인 페이지(`index.html`)에서 **"강의 생성기"** 링크 클릭
- 네비게이션 바에서 쉽게 접근 가능

---

## 📖 사용 방법

### Step 1: API 키 입력
1. Gemini API 키를 입력 (기본값이 설정되어 있음)
2. API 키 발급: https://aistudio.google.com/apikey

### Step 2: CSV 파일 준비
CSV 파일 형식:
```csv
abandon,버리다,v
accept,받아들이다,v
achieve,성취하다,v
```

- **컬럼 구조**: `영어단어,한글뜻,품사`
- 품사는 선택사항 (v=동사, n=명사, adj=형용사 등)

### Step 3: CSV 파일 업로드
- 드래그 앤 드롭 또는 클릭하여 파일 선택
- 파일 로드 완료 시 단어 개수 표시

### Step 4: 범위 설정 (선택)
- **시작 인덱스**: 처리를 시작할 단어 번호 (기본: 0)
- **종료 인덱스**: 처리를 끝낼 단어 번호 (비워두면 끝까지)

예시:
- 0~10: 처음 10개만 테스트
- 100~200: 100번~200번 단어만 처리

### Step 5: 생성 시작
1. **"🚀 생성 시작"** 버튼 클릭
2. 실시간 진행 상황 확인
3. 로그에서 상세 정보 확인

### Step 6: 다운로드
- 생성 완료 후 **"📦 모든 파일 다운로드 (ZIP)"** 클릭
- ZIP 파일에 포함된 내용:
  - `lectures/` - JSON 강의 파일
  - `audio/` - WAV 음성 파일

---

## 📁 출력 파일 구조

```
aivoca-lectures-[timestamp].zip
├── lectures/
│   ├── abandon.json
│   ├── accept.json
│   └── achieve.json
└── audio/
    ├── abandon.wav
    ├── accept.wav
    └── achieve.wav
```

### JSON 강의 파일 예시
```json
{
  "word": "abandon",
  "korean": "버리다",
  "partOfSpeech": "v",
  "lecture": "abandon은 '버리다, 포기하다'라는 뜻입니다...",
  "generatedAt": "2025-01-03T12:34:56.789Z"
}
```

### 음성 파일 사양
- **형식**: WAV
- **샘플레이트**: 24kHz
- **비트**: 16-bit
- **채널**: Mono
- **음성**: Gemini TTS (Kore 보이스)

---

## ⚙️ 기술 사양

### 사용 기술
- **Frontend**: Pure HTML/CSS/JavaScript
- **AI Model**: Gemini 2.0 Flash Exp
- **TTS**: Gemini TTS API
- **파일 압축**: JSZip
- **실행 환경**: 브라우저 (Chrome, Safari, Firefox 등)

### API 엔드포인트
```
Text Generation:
https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent

TTS Generation:
https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent
(with responseModalities: ['AUDIO'])
```

### 강의 생성 프롬프트 구조
```
- 스타일: 경어체, 담백하고 흥미롭게
- 길이: 600자 이내
- 포함 내용:
  * 한글 뜻
  * 발음 (한글)
  * 어원
  * 동의어/유의어
  * 반의어
  * 예문 2개 (한글 번역)
  * 암기 팁
```

---

## ⏱️ 처리 시간

| 단어 수 | 예상 시간 |
|---------|-----------|
| 10개    | 약 20초   |
| 50개    | 약 1분 40초 |
| 100개   | 약 3분 20초 |
| 500개   | 약 16분   |
| 1200개  | 약 40분   |

**참고**: 단어당 약 2초 소요 (API 호출 + TTS 생성 + Rate Limit)

---

## 🔍 트러블슈팅

### API 오류 발생
**문제**: `API 오류: 429` 표시
**원인**: Rate Limit 초과
**해결**:
- 무료 API: 15 RPM (분당 15회)
- 유료 API로 업그레이드 또는 대기 시간 증가

### TTS 생성 실패
**문제**: `TTS API 오류: 400`
**원인**: 텍스트가 너무 길거나 부적절한 내용
**해결**:
- 강의 길이를 600자 이내로 유지
- 프롬프트 수정

### CSV 파싱 오류
**문제**: 단어가 제대로 로드되지 않음
**원인**: CSV 형식 불일치
**해결**:
```csv
올바른 형식:
abandon,버리다,v

잘못된 형식:
"abandon","버리다","v"  ← 따옴표 제거
```

### 다운로드가 안 됨
**문제**: ZIP 다운로드 버튼 클릭 시 반응 없음
**원인**: 브라우저 팝업 차단
**해결**:
- 브라우저 설정에서 팝업 허용
- 다운로드 권한 확인

---

## 💡 베스트 프랙티스

### 1. 소규모 테스트 먼저
```
처음: 10~20개 단어로 테스트
확인: 결과 품질 검증
전체: 모든 단어 생성
```

### 2. 배치 처리
```
1차: 0~300
2차: 300~600
3차: 600~900
4차: 900~1200
```

### 3. 백업
- 생성된 ZIP 파일은 즉시 백업
- 날짜별로 폴더 구분

### 4. API 키 관리
- API 키 노출 방지
- 환경변수 사용 권장 (프로덕션)
- 할당량 모니터링

---

## 🔗 관련 링크

- **Gemini API 문서**: https://ai.google.dev/docs
- **API 키 발급**: https://aistudio.google.com/apikey
- **할당량 확인**: Google Cloud Console

---

## 📞 지원

문제가 발생하면:
1. 브라우저 콘솔 로그 확인 (F12)
2. 로그 섹션의 오류 메시지 확인
3. cactuslabskorea2@gmail.com으로 문의

---

## 🎉 완료!

AIVOCA 강의 생성기가 성공적으로 통합되었습니다!
- ✅ 브라우저에서 바로 실행
- ✅ Cactus Labs 디자인 적용
- ✅ 메인 사이트와 통합
- ✅ 간편한 CSV → JSON + Audio 변환

**Happy Generating! 🚀**
