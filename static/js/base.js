document.addEventListener("DOMContentLoaded", function () {
    // 페이지 페이드 인 효과 추가
    document.body.style.transition = "opacity 1s ease-in-out"; 
    document.body.style.opacity = "1"; 

    // Bootstrap Toast 메시지 자동 표시
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
        var toast = new bootstrap.Toast(toastEl);
        toast.show();
    });

    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav');

    if (hamburger && nav) {
        // 햄버거 버튼 클릭 시 메뉴 토글
        hamburger.addEventListener('click', (event) => {
            nav.classList.toggle('active');
            event.stopPropagation(); // body 이벤트로 전파되지 않도록 방지
        });

        // nav 내부 클릭 시 이벤트 차단 (a 태그 클릭은 허용)
        nav.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', (event) => {
                event.stopPropagation(); // a 태그 클릭 시 메뉴 닫히지 않도록 방지
            });
        });

        // nav 배경을 클릭했을 때 nav 닫기
        nav.addEventListener('click', (event) => {
            // 클릭된 부분이 a 태그가 아니라면 nav를 닫음
            if (!event.target.closest('a')) {
                nav.classList.remove('active');
            }
        });
    }
});
