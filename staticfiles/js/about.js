/* ================================================
   about.js
   – Animated counter for the stats banner
     (fires once when the banner scrolls into view)
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
        var prefix  = "";               // e.g. "" or could be used for currency
        var suffix  = "";

        // Detect if the original text had a comma-formatted number
        var raw = el.getAttribute("data-target") || el.textContent;
        var useCommas = raw.indexOf(",") > -1;

        function step(now) {
            var elapsed  = now - start;
            var progress = Math.min(elapsed / duration, 1);
            // ease-out cubic
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
     * Strips commas, spaces, and any non-digit chars.
     */
    function parseTarget(el) {
        var txt = (el.getAttribute("data-target") || el.textContent).replace(/[^0-9]/g, "");
        return parseInt(txt, 10) || 0;
    }

    /* ── boot ── */
    document.addEventListener("DOMContentLoaded", function () {
        var statsSection = document.querySelector(".about-stats");
        if (!statsSection) return;

        var numberEls = statsSection.querySelectorAll(".about-stats__number");
        var animated  = false;

        // Store targets as data attributes so we can re-read after first animation
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
                        // stagger each card by 150 ms
                        setTimeout(function () {
                            animateCount(el, parseTarget(el), 1800);
                        }, i * 150);
                    });
                    observer.disconnect(); // fire only once
                }
            });
        }, { threshold: 0.3 });

        observer.observe(statsSection);
    });

})();