// ===== БУРГЕР-МЕНЮ =====
document.querySelector('.menu-toggle').addEventListener('click', function() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('open');
    
    // Анимация иконки бургера
    const icon = this.querySelector('i');
    if (navLinks.classList.contains('open')) {
        icon.className = 'fas fa-times';
    } else {
        icon.className = 'fas fa-bars';
    }
});

// ===== ПЛАВНАЯ ПРОКРУ