// GOGWAN 웹 서비스 공통 JavaScript

// Firebase 설정 (공통)
export const firebaseConfig = {
    apiKey: "AIzaSyD-i5QR-MFeCLQtSMlIqXUhVuIzkJQBRhA",
    authDomain: "gogwan-e79bc.firebaseapp.com",
    projectId: "gogwan-e79bc",
    storageBucket: "gogwan-e79bc.firebasestorage.app",
    messagingSenderId: "241129624672",
    appId: "1:241129624672:web:920301c7f196322c761f05"
};

// Gemini API 키
export const GEMINI_API_KEY = 'AIzaSyAMPy1HPTW54Gs7G_wes6zFXOyyhiNaWuQ';

// 유틸리티 함수
export const utils = {
    // 날짜 포맷팅
    formatDate(date) {
        if (!date) return '';
        const d = date.toDate ? date.toDate() : new Date(date);
        return d.toLocaleDateString('ko-KR');
    },

    // 카테고리 색상
    getCategoryColor(category) {
        switch (category) {
            case '정책': return { bg: '#DCFCE7', text: '#16A34A' };
            case '행사': return { bg: '#FFEDD5', text: '#EA580C' };
            case '발표': return { bg: '#E0E7FF', text: '#4F46E5' };
            default: return { bg: '#F3F4F6', text: '#4B5563' };
        }
    },

    // 에러 처리
    handleError(error, context = '') {
        console.error(`Error in ${context}:`, error);
        alert(`오류가 발생했습니다: ${error.message}`);
    }
};

// 페이지 로딩 완료 표시
console.log('✅ GOGWAN 웹 서비스 로드 완료');
