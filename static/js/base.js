document.addEventListener("DOMContentLoaded", function () {
    document.body.style.transition = "opacity 1s ease-in-out"; 
    document.body.style.opacity = "1"; 

    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
        var toast = new bootstrap.Toast(toastEl);
        toast.show();
    });

    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav');

    if (hamburger && nav) {
        hamburger.addEventListener('click', (event) => {
            nav.classList.toggle('active');
            event.stopPropagation(); //
        });

        nav.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', (event) => {
                event.stopPropagation(); 
            });
        });

        nav.addEventListener('click', (event) => {
            if (!event.target.closest('a')) {
                nav.classList.remove('active');
            }
        });
    }
});
