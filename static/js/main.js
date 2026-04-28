// Navbar scroll effect
window.addEventListener('scroll', function() {
    const nav = document.querySelector('#main-nav');
    if (window.scrollY > 50) {
        nav.style.padding = '0.5rem 0';
        nav.style.backgroundColor = 'rgba(15, 23, 42, 0.95)';
    } else {
        nav.style.padding = '1rem 0';
        nav.style.backgroundColor = 'rgba(15, 23, 42, 0.9)';
    }
});

// Initialize tooltips if any
document.addEventListener('DOMContentLoaded', function() {
    console.log('AeroTravels JS Loaded');
});
