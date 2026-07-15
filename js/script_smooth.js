document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('scroll');
    
    if (targetId) {
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            setTimeout(function() {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 500);
        }
    }
});