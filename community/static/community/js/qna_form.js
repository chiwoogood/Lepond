document.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("category");
    const productSelect = document.getElementById("product");
    const titleInput = document.getElementById("title");
    const contentTextarea = document.getElementById("content");
    const productLabel = document.querySelector("label[for='product']");
    const titleLabel = document.querySelector("label[for='title']");
    const contentLabel = document.querySelector("label[for='content']");
    
    productSelect.style.display = "none";
    productLabel.style.display = "none";
    titleInput.style.display = "none";
    titleLabel.style.display = "none";
    contentTextarea.style.display = "none";
    contentLabel.style.display = "none";
    
    categorySelect.addEventListener("change", function () {
        const selectedValue = categorySelect.value;
        
        if (selectedValue === "product") {
            productSelect.style.display = "block";
            productLabel.style.display = "block";
            titleInput.style.display = "block";  
            titleLabel.style.display = "block"; 
            contentTextarea.style.display = "block";
            contentLabel.style.display = "block";
        } else if (selectedValue === "shipping" || selectedValue === "payment" || selectedValue === "other") {

            productSelect.style.display = "none";
            productLabel.style.display = "none";
            titleInput.style.display = "block";
            titleLabel.style.display = "block";
            contentTextarea.style.display = "block";
            contentLabel.style.display = "block";
        } else {

            productSelect.style.display = "none";
            productLabel.style.display = "none";
            titleInput.style.display = "none";
            titleLabel.style.display = "none";
            contentTextarea.style.display = "none";
            contentLabel.style.display = "none";
        }
    });

    categorySelect.dispatchEvent(new Event("change"));
});