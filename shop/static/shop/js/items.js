function selectCategory(elem, categoryId) {
    document.querySelectorAll('.category-item').forEach(el => el.classList.remove('active'));
    elem.classList.add('active');

    fetch(`/shop/?category=${categoryId}`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const row = document.querySelector('.row');
        row.innerHTML = '';

        if (data.products.length > 0) {
            data.products.forEach(product => {
                row.innerHTML += `
                <div class="col">
                    <div class="swiper-slide">
                        <a href="/shop/details/${product.id}/">
                            <img src="${product.thumbnail || 'https://dummyimage.com/900x700/ccc/000&text=No+Image'}"
                                 class="card-img-top" alt="Thumbnail Image">
                        </a>
                        <a href="/shop/details/${product.id}/">
                            <div class="card-body">
                                <h5 class="card-title">${product.name}</h5>
                                <p class="card-price">${product.price}</p>
                                <p class="card-status">${product.status}</p>
                            </div>
                        </a>
                        <form method="POST" action="/shop/add_cart/${product.id}/">
                            <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
                            <button type="submit" class="add-to-cart-btn">장바구니 담기 🛒</button>
                        </form>
                    </div>
                </div>`;
            });
        } else {
            row.innerHTML = '<p class="no-products">현재 등록된 상품이 없습니다.</p>';
        }
    })
    .catch(error => console.error('Error:', error));
}
