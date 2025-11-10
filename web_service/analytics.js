/**
 * GOGWAN Analytics Tracking Library
 * 모든 서비스 페이지에서 사용할 분석 추적 라이브러리
 */

// Firebase 설정
const firebaseConfig = {
    apiKey: "AIzaSyD-i5QR-MFeCLQtSMlIqXUhVuIzkJQBRhA",
    authDomain: "gogwan-e79bc.firebaseapp.com",
    projectId: "gogwan-e79bc",
    storageBucket: "gogwan-e79bc.firebasestorage.app",
    messagingSenderId: "241129624672",
    appId: "1:241129624672:web:920301c7f196322c761f05"
};

let db = null;

// Firebase 초기화 (동적 import 사용)
async function initFirebase() {
    if (db) return db;

    try {
        const { initializeApp } = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js');
        const { getFirestore, collection, addDoc, serverTimestamp } = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js');

        const app = initializeApp(firebaseConfig);
        db = getFirestore(app);

        window.firestoreModules = { collection, addDoc, serverTimestamp };

        return db;
    } catch (error) {
        console.error('Firebase 초기화 실패:', error);
        return null;
    }
}

/**
 * 페이지 방문 추적
 * @param {string} pageName - 페이지 이름 (예: 'create', 'ai-image', 'saju-yearly')
 * @param {string} category - 카테고리 (예: 'smart-work', 'ai-image', 'lounge', 'learning')
 */
async function trackPageView(pageName, category) {
    try {
        const db = await initFirebase();
        if (!db) return;

        const { collection, addDoc, serverTimestamp } = window.firestoreModules;

        await addDoc(collection(db, 'analytics_page_views'), {
            pageName,
            category,
            timestamp: serverTimestamp(),
            userAgent: navigator.userAgent,
            referrer: document.referrer || 'direct',
            screenWidth: window.screen.width,
            screenHeight: window.screen.height
        });

        console.log(`📊 Page view tracked: ${pageName}`);
    } catch (error) {
        console.error('페이지 추적 실패:', error);
    }
}

/**
 * 기능 실행 추적
 * @param {string} featureName - 기능 이름 (예: 'generate-press-release', 'remove-background')
 * @param {string} pageName - 페이지 이름
 * @param {object} metadata - 추가 메타데이터 (선택사항)
 */
async function trackFeatureUsage(featureName, pageName, metadata = {}) {
    try {
        const db = await initFirebase();
        if (!db) return;

        const { collection, addDoc, serverTimestamp } = window.firestoreModules;

        await addDoc(collection(db, 'analytics_feature_usage'), {
            featureName,
            pageName,
            timestamp: serverTimestamp(),
            metadata,
            userAgent: navigator.userAgent
        });

        console.log(`📊 Feature usage tracked: ${featureName}`);
    } catch (error) {
        console.error('기능 추적 실패:', error);
    }
}

/**
 * 에러 추적
 * @param {string} errorType - 에러 타입
 * @param {string} errorMessage - 에러 메시지
 * @param {string} pageName - 페이지 이름
 */
async function trackError(errorType, errorMessage, pageName) {
    try {
        const db = await initFirebase();
        if (!db) return;

        const { collection, addDoc, serverTimestamp } = window.firestoreModules;

        await addDoc(collection(db, 'analytics_errors'), {
            errorType,
            errorMessage,
            pageName,
            timestamp: serverTimestamp(),
            userAgent: navigator.userAgent,
            url: window.location.href
        });

        console.log(`📊 Error tracked: ${errorType}`);
    } catch (error) {
        console.error('에러 추적 실패:', error);
    }
}

/**
 * 다운로드 추적
 * @param {string} fileType - 파일 타입 (예: 'word', 'png', 'pptx')
 * @param {string} featureName - 기능 이름
 */
async function trackDownload(fileType, featureName) {
    try {
        const db = await initFirebase();
        if (!db) return;

        const { collection, addDoc, serverTimestamp } = window.firestoreModules;

        await addDoc(collection(db, 'analytics_downloads'), {
            fileType,
            featureName,
            timestamp: serverTimestamp()
        });

        console.log(`📊 Download tracked: ${fileType}`);
    } catch (error) {
        console.error('다운로드 추적 실패:', error);
    }
}

// 전역 객체로 노출
window.GogwanAnalytics = {
    trackPageView,
    trackFeatureUsage,
    trackError,
    trackDownload
};

// 페이지 로드 시 자동으로 현재 페이지 추적
window.addEventListener('load', () => {
    // 현재 파일명에서 페이지 이름 추출
    const pagePath = window.location.pathname;
    const pageName = pagePath.split('/').pop().replace('.html', '') || 'index';

    // 카테고리 매핑
    const categoryMap = {
        'create': 'smart-work',
        'press-release': 'smart-work',
        'press-release-result': 'smart-work',
        'banner-maker': 'smart-work',
        'pdf-to-ppt': 'smart-work',
        'background-remover': 'ai-image',
        'id-photo': 'ai-image',
        'style-transfer': 'ai-image',
        'style-select': 'ai-image',
        'ghibli-style': 'ai-image',
        'mbti-test': 'lounge',
        'saju-lifetime': 'lounge',
        'saju-yearly': 'lounge',
        'ai-problem-solver': 'learning',
        'gogwan': 'landing',
        'jamssam': 'landing',
        'fast-rabbit': 'landing',
        'index': 'main'
    };

    const category = categoryMap[pageName] || 'other';

    // 페이지 뷰 자동 추적 (100ms 지연)
    setTimeout(() => {
        trackPageView(pageName, category);
    }, 100);
});
