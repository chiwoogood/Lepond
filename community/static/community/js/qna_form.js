document.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("category");
    const productSelect = document.getElementById("product");
    const titleInput = document.getElementById("title");
    const contentTextarea = document.getElementById("content");
    const productLabel = document.querySelector("label[for='product']");
    const titleLabel = document.querySelector("label[for='title']");
    const contentLabel = document.querySelector("label[for='content']");
    
    // 초기 상태에서 제목과 내용 숨기기
    productSelect.style.display = "none";
    productLabel.style.display = "none";
    titleInput.style.display = "none";
    titleLabel.style.display = "none";
    contentTextarea.style.display = "none";
    contentLabel.style.display = "none";
    
    categorySelect.addEventListener("change", function () {
        const selectedValue = categorySelect.value;
        
        if (selectedValue === "product") {
            // 제품 관련 선택 시: 제품 select와 내용 표시, 제목은 숨김
            productSelect.style.display = "block";
            productLabel.style.display = "block";
            titleInput.style.display = "none";
            titleLabel.style.display = "none";
            contentTextarea.style.display = "block";
            contentLabel.style.display = "block";
        } else if (selectedValue === "shipping" || selectedValue === "payment" || selectedValue === "other") {
            // 배송, 결제/환불, 기타 선택 시: 제목과 내용 표시, 제품 select는 숨김
            productSelect.style.display = "none";
            productLabel.style.display = "none";
            titleInput.style.display = "block";
            titleLabel.style.display = "block";
            contentTextarea.style.display = "block";
            contentLabel.style.display = "block";
        } else {
            // 기본 상태: 모든 입력 필드 숨기기
            productSelect.style.display = "none";
            productLabel.style.display = "none";
            titleInput.style.display = "none";
            titleLabel.style.display = "none";
            contentTextarea.style.display = "none";
            contentLabel.style.display = "none";
        }
    });
});
