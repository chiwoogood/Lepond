var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    loop: true,
    autoHeight: true, 
    autoplay: {
        delay: 6000,
        disableOnInteraction: false
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    allowTouchMove: true,
    speed: 800
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

function bindCustomSelect(realSelectId, customSelectId) {
    const realSelect = document.getElementById(realSelectId);
    const customSelect = document.getElementById(customSelectId);
    const selected = customSelect.querySelector('.selected');
    const optionsContainer = customSelect.querySelector('.options-container');
    const options = optionsContainer.querySelectorAll('.option');

    selected.addEventListener('click', (e) => {
        e.stopPropagation();
        customSelect.classList.toggle('active');
        optionsContainer.classList.toggle('d-none');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            const value = option.getAttribute('data-value');
            const text = option.textContent;
            selected.textContent = text;
            realSelect.value = value;
            realSelect.dispatchEvent(new Event('change')); // ✅ change 트리거
            customSelect.classList.remove('active');
            optionsContainer.classList.add('d-none');
        });
    });

    document.addEventListener('click', (e) => {
        if (!customSelect.contains(e.target)) {
            customSelect.classList.remove('active');
            optionsContainer.classList.add('d-none');
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    bindCustomSelect('color', 'custom-color-select');
    bindCustomSelect('size', 'custom-size-select');

    const productQuantities = JSON.parse(
        document.getElementById("productQuantities").textContent
    );

    const colorSelect = document.getElementById("color");
    const sizeSelect = document.getElementById("size");
    const buyBtn = document.getElementById("buyBtn");
    const cartBtn = document.getElementById("cartBtn");
    const colorIdInput = document.getElementById("color_id");
    const sizeIdInput = document.getElementById("size_id");

    function checkStock() {
        const selectedColor = colorSelect.value;
        const selectedSize = sizeSelect.value;

        colorIdInput.value = selectedColor;
        sizeIdInput.value = selectedSize;

        if (selectedColor && selectedSize) {
            const match = productQuantities.find(q => q.color == selectedColor && q.size == selectedSize);
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