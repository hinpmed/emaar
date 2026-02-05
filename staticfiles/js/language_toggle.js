// Language Toggle Function
function toggleLanguage() {
    // Get current URL
    const currentUrl = window.location.href;
    
    // Get current language from HTML tag
    const currentLang = document.documentElement.lang || 'ar';
    
    // Toggle language
    const newLang = currentLang === 'ar' ? 'en' : 'ar';
    
    // Set language via Django view
    const languageUrl = `/set-language/?lang=${newLang}`;
    
    // Redirect to set language (which will return to same page)
    window.location.href = languageUrl;
}

// Update language button label based on current language
document.addEventListener('DOMContentLoaded', function() {
    const currentLang = document.documentElement.lang || 'ar';
    const langButton = document.querySelector('button[onclick="toggleLanguage()"]');
    
    if (langButton && currentLang === 'ar') {
        langButton.setAttribute('title', 'Switch to English');
        langButton.setAttribute('aria-label', 'Switch to English');
    } else if (langButton) {
        langButton.setAttribute('title', 'التبديل إلى العربية');
        langButton.setAttribute('aria-label', 'التبديل إلى العربية');
    }
});