function selectCategory(elem, categoryId) {
    document.querySelectorAll('.category-item').forEach(el => el.classList.remove('active'));
    elem.classList.add('active');

    fetch(`/shop/items/filter/?category=${categoryId}`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (!response.ok) throw new Error(`서버 응답 오류: ${response.status}`);
        return response.json();
    })
    .then(data => {
        const allItems = document.querySelectorAll('.product-item');

        allItems.forEach(item => {
            const productId = parseInt(item.dataset.productId);
            if (data.product_ids.includes(productId)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });

        const noProductsText = document.querySelector('.no-products');
        if (data.product_ids.length === 0) {
            if (!noProductsText) {
                const row = document.querySelector('.row');
                const msg = document.createElement('p');
                msg.classList.add('no-products');
                msg.innerText = '현재 등록된 상품이 없습니다.';
                row.appendChild(msg);
            }
        } else {
            if (noProductsText) noProductsText.remove();
        }
    })
    .catch(error => console.error('Error:', error));
}
