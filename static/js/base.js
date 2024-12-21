const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
});


document.addEventListener("DOMContentLoaded", function () {
    // 페이지가 로드되면 body에 부드러운 전환을 적용
    document.body.style.transition = "opacity 1s ease-in-out"; 
    document.body.style.opacity = "1"; // 보이게 설정
});