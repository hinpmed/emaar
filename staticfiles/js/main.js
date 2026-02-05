// Mobile Menu Toggle - Fixed
function toggleMobileMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    const menuBtn = document.querySelector('.mobile-menu-btn');
    
    if (mobileMenu) {
        const isHidden = mobileMenu.classList.contains('hidden');
        
        if (isHidden) {
            mobileMenu.classList.remove('hidden');
            mobileMenu.style.display = 'block';
            if (menuBtn) menuBtn.setAttribute('aria-expanded', 'true');
        } else {
            mobileMenu.classList.add('hidden');
            mobileMenu.style.display = 'none';
            if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
        }
    }
}

// Close mobile menu when clicking outside
document.addEventListener('click', function(event) {
    const mobileMenu = document.getElementById('mobileMenu');
    const menuBtn = document.querySelector('.mobile-menu-btn');
    
    if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
        const isClickInside = mobileMenu.contains(event.target) || menuBtn.contains(event.target);
        
        if (!isClickInside) {
            mobileMenu.classList.add('hidden');
            mobileMenu.style.display = 'none';
            if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
        }
    }
});

// Close mobile menu on link click
document.addEventListener('DOMContentLoaded', function() {
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');
    const mobileMenu = document.getElementById('mobileMenu');
    
    mobileLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (mobileMenu) {
                mobileMenu.classList.add('hidden');
                mobileMenu.style.display = 'none';
            }
        });
    });
});

// Dark Mode Toggle
function toggleDarkMode() {
    document.body.classList.toggle('dark');
    const isDark = document.body.classList.contains('dark');
    localStorage.setItem('darkMode', isDark);
    
    // Update icon
    const darkIcon = document.querySelector('.dark-icon');
    const lightIcon = document.querySelector('.light-icon');
    if (darkIcon && lightIcon) {
        if (isDark) {
            darkIcon.classList.add('hidden');
            lightIcon.classList.remove('hidden');
        } else {
            darkIcon.classList.remove('hidden');
            lightIcon.classList.add('hidden');
        }
    }
}

// Language Toggle
function toggleLanguage() {
    const currentLang = document.documentElement.lang;
    const newLang = currentLang === 'ar' ? 'en' : 'ar';
    const newDir = newLang === 'ar' ? 'rtl' : 'ltr';
    
    document.documentElement.lang = newLang;
    document.documentElement.dir = newDir;
    document.body.dir = newDir;
    
    localStorage.setItem('language', newLang);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Restore dark mode preference
    const darkMode = localStorage.getItem('darkMode') === 'true';
    if (darkMode) {
        document.body.classList.add('dark');
        const darkIcon = document.querySelector('.dark-icon');
        const lightIcon = document.querySelector('.light-icon');
        if (darkIcon && lightIcon) {
            darkIcon.classList.add('hidden');
            lightIcon.classList.remove('hidden');
        }
    }
    
    // Restore language preference
    const savedLang = localStorage.getItem('language');
    if (savedLang) {
        document.documentElement.lang = savedLang;
        const newDir = savedLang === 'ar' ? 'rtl' : 'ltr';
        document.documentElement.dir = newDir;
        document.body.dir = newDir;
    }
});