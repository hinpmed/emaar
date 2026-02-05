// Dark Mode Toggle Functionality
// Manages theme switching and persistence

(function() {
    'use strict';

    // Get theme from localStorage or default to light
    function getTheme() {
        return localStorage.getItem('theme') || 'light';
    }

    // Set theme and update UI
    function setTheme(theme) {
        const html = document.documentElement;
        const darkIcon = document.querySelector('.dark-icon');
        const lightIcon = document.querySelector('.light-icon');
        
        if (theme === 'dark') {
            html.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            
            if (darkIcon) darkIcon.classList.add('hidden');
            if (lightIcon) lightIcon.classList.remove('hidden');
        } else {
            html.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            
            if (darkIcon) darkIcon.classList.remove('hidden');
            if (lightIcon) lightIcon.classList.add('hidden');
        }
    }

    // Toggle between themes
    function toggleDarkMode() {
        const currentTheme = getTheme();
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    }

    // Initialize theme on page load
    function initializeTheme() {
        const savedTheme = getTheme();
        setTheme(savedTheme);
    }

    // Make functions globally available
    window.toggleDarkMode = toggleDarkMode;
    window.setTheme = setTheme;
    window.getTheme = getTheme;

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeTheme);
    } else {
        initializeTheme();
    }

})();