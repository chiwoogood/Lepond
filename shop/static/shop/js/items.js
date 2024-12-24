function selectCategory(selected) {
    const categories = document.querySelectorAll('.category-item');
    categories.forEach(category => category.classList.remove('active'));
    selected.classList.add('active');
}