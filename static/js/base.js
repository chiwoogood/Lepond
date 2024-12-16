const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
    console.log('nav 상태:', nav.classList.contains('active')); // 상태 확인
});