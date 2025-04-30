var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    loop: true,
    effect: "fade",
    fadeEffect: {
        crossFade: true
    },
    autoplay: {
        delay: 6000,
        disableOnInteraction: false
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    allowTouchMove: true
});
document.addEventListener("DOMContentLoaded", function () {
    const productQuantities = JSON.parse(
        document.getElementById("productQuantities").textContent
    );

    const colorSelect = document.getElementById("color");
    const sizeSelect = document.getElementById("size");
    const buyBtn = document.getElementById("buyBtn");
    const cartBtn = document.getElementById("cartBtn");
    const stockStatus = document.getElementById("stockStatus");
    const colorIdInput = document.getElementById("color_id");
    const sizeIdInput = document.getElementById("size_id");

    function checkStock() {
        const selectedColor = colorSelect.value;
        const selectedSize = sizeSelect.value;

        colorIdInput.value = selectedColor;
        sizeIdInput.value = selectedSize;

        if (selectedColor && selectedSize) {
            const match = productQuantities.find(q => q.color === selectedColor && q.size === selectedSize);
            if (match && match.stock > 0) {
                buyBtn.disabled = false;
                cartBtn.disabled = false;
                buyBtn.textContent = "Buy";
                cartBtn.textContent = "Cart 🛒";
            } else {
                buyBtn.disabled = true;
                cartBtn.disabled = true;
                buyBtn.textContent = "Sold Out";
                cartBtn.textContent = "Cart 🛒";
            }
        } else {
            buyBtn.disabled = true;
            cartBtn.disabled = true;
            buyBtn.textContent = "Buy";
            cartBtn.textContent = "Cart 🛒";
        }
    }

    colorSelect.addEventListener("change", checkStock);
    sizeSelect.addEventListener("change", checkStock);
});
