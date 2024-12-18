const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
});

document.addEventListener('DOMContentLoaded', () => {
    const body = document.querySelector('body');
    const loadingScreen = document.getElementById('loading-screen');

    // 페이지 로드 시 페이드 인 효과
    body.style.opacity = '0';
    setTimeout(() => {
        body.style.transition = 'opacity 0.5s ease';
        body.style.opacity = '1'; // 페이드 인 효과
    }, 100); // DOM이 완전히 로드된 후 시작

    // 모든 링크 클릭 이벤트 처리
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); 
            const href = link.getAttribute('href'); // 이동할 URL 가져오기

            // 페이드 아웃 효과 시작
            body.style.opacity = '0'; // 페이드 아웃 효과
            loadingScreen.classList.add('show'); // 로딩 화면 표시

            setTimeout(() => {
                window.location.href = href; // 페이지 이동
            }, 300); // 페이드 아웃과 동기화
        });
    });
});