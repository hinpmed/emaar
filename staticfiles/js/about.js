/* ================================================
   about.js
   – Animated counter for the stats banner
   – Tab switching for strategic objectives
   ================================================ */
   (function () {
    "use strict";

    /**
     * Animate a single element's textContent from 0 → target
     * @param {HTMLElement} el          – the <span> to update
     * @param {number}      target      – final numeric value
     * @param {number}      duration    – animation length in ms
     */
    function animateCount(el, target, duration) {
        var start   = performance.now();
        var prefix  = "";
        var suffix  = "";

        var raw = el.getAttribute("data-target") || el.textContent;
        var useCommas = raw.indexOf(",") > -1;

        function step(now) {
            var elapsed  = now - start;
            var progress = Math.min(elapsed / duration, 1);
            var eased    = 1 - Math.pow(1 - progress, 3);
            var current  = Math.round(eased * target);

            el.textContent = useCommas
                ? current.toLocaleString("ar-SA")
                : current.toString();

            if (progress < 1) {
                requestAnimationFrame(step);
            }
        }
        requestAnimationFrame(step);
    }

    /**
     * Parse the visible text of an element to extract the numeric target.
     */
    function parseTarget(el) {
        var txt = (el.getAttribute("data-target") || el.textContent).replace(/[^0-9]/g, "");
        return parseInt(txt, 10) || 0;
    }

    /**
     * Initialize stats counter animation
     */
    function initStatsCounter() {
        var statsSection = document.querySelector(".about-stats");
        if (!statsSection) return;

        var numberEls = statsSection.querySelectorAll(".about-stats__number");
        var animated  = false;

        numberEls.forEach(function (el) {
            if (!el.hasAttribute("data-target")) {
                el.setAttribute("data-target", el.textContent.trim());
            }
        });

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && !animated) {
                    animated = true;
                    numberEls.forEach(function (el, i) {
                        setTimeout(function () {
                            animateCount(el, parseTarget(el), 1800);
                        }, i * 150);
                    });
                    observer.disconnect();
                }
            });
        }, { threshold: 0.3 });

        observer.observe(statsSection);
    }

    /**
     * Initialize strategic objectives tabs
     */
    function initStrategicTabs() {
        var tabs = document.querySelectorAll('.about-strategic__tab');
        var contents = document.querySelectorAll('.about-strategic__content');

        if (tabs.length === 0 || contents.length === 0) return;

        tabs.forEach(function(tab) {
            tab.addEventListener('click', function() {
                var targetTab = this.getAttribute('data-tab');

                // Remove active class from all tabs
                tabs.forEach(function(t) {
                    t.classList.remove('active');
                });

                // Remove active class from all contents
                contents.forEach(function(c) {
                    c.classList.remove('active');
                });

                // Add active class to clicked tab
                this.classList.add('active');

                // Add active class to corresponding content
                var targetContent = document.getElementById(targetTab + '-tab');
                if (targetContent) {
                    targetContent.classList.add('active');
                }
            });
        });
    }

    /* ── boot ── */
    document.addEventListener("DOMContentLoaded", function () {
        initStatsCounter();
        initStrategicTabs();
    });

})();

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