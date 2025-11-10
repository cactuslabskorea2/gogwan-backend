// Firebase Authentication 기반 관리자 인증 체크
// 모든 관리자 페이지에서 include하여 사용

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js';
import { getAuth, onAuthStateChanged, signOut } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js';

// Firebase 설정
const firebaseConfig = {
    apiKey: "AIzaSyD-i5QR-MFeCLQtSMlIqXUhVuIzkJQBRhA",
    authDomain: "gogwan-e79bc.firebaseapp.com",
    projectId: "gogwan-e79bc",
    storageBucket: "gogwan-e79bc.firebasestorage.app",
    messagingSenderId: "241129624672",
    appId: "1:241129624672:web:920301c7f196322c761f05"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// 로그인 페이지가 아닌 경우에만 인증 체크
if (!window.location.pathname.includes('/login.html')) {
    onAuthStateChanged(auth, (user) => {
        if (!user) {
            // 로그인되지 않았으면 로그인 페이지로 리다이렉트 (현재 페이지 URL 저장)
            const currentPath = window.location.pathname + window.location.search;
            const returnUrl = encodeURIComponent(currentPath);
            window.location.href = `login.html?returnUrl=${returnUrl}`;
        } else {
            console.log('인증된 사용자:', user.email);
        }
    });
}

// 로그아웃 함수 전역으로 노출
window.adminLogout = async function() {
    if (confirm('로그아웃 하시겠습니까?')) {
        try {
            await signOut(auth);
            window.location.href = 'login.html';
        } catch (error) {
            console.error('로그아웃 실패:', error);
            alert('로그아웃에 실패했습니다: ' + error.message);
        }
    }
};

// 현재 사용자 정보 가져오기
window.getCurrentUser = function() {
    return auth.currentUser;
};

// Firebase Auth 객체 전역으로 노출
window.firebaseAuth = auth;
