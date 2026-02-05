/* governance_rating.js
   ─────────────────────
   Animates the progress-bar fills once each card scrolls into view.
   Reads the target width from  data-width  on .gsub-bar-card__fill
   and sets it via style.width after a short stagger delay.
*/
(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {

        var fills = document.querySelectorAll('.gsub-bar-card__fill');
        if (!fills.length) return;

        /* use IntersectionObserver so bars animate when they enter the viewport */
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;

                var fill  = entry.target;
                var pct   = fill.getAttribute('data-width');
                if (pct === null) return;

                /* tiny delay so the browser has painted width:0 first */
                requestAnimationFrame(function () {
                    fill.style.width = pct + '%';
                });

                /* only animate once */
                observer.unobserve(fill);
            });
        }, { threshold: 0.15 });

        fills.forEach(function (el) {
            /* make sure width starts at 0 */
            el.style.width = '0';
            observer.observe(el);
        });
    });
})();