/* ============================================================
   services.js
   Client-side filter (pills) + live search
   ============================================================ */

   document.addEventListener('DOMContentLoaded', function () {

    var pills      = document.querySelectorAll('.svc-pill');
    var searchBox  = document.getElementById('svcSearch');
    var cards      = document.querySelectorAll('.svc-card');
    var emptyState = document.getElementById('svcEmpty');

    var currentFilter = 'all';   // tracks the active pill value

    // ── helper: run filter + search together ──
    function applyFilters() {
        var query = searchBox.value.trim();
        var visibleCount = 0;

        cards.forEach(function (card) {
            var category = card.getAttribute('data-category');
            var title    = card.getAttribute('data-title');
            var desc     = card.getAttribute('data-desc');

            // pill match
            var pillMatch = (currentFilter === 'all') || (category === currentFilter);

            // search match (Arabic-safe, case-insensitive)
            var searchMatch = true;
            if (query.length > 0) {
                var haystack = (title + ' ' + desc).toLowerCase();
                searchMatch  = haystack.indexOf(query.toLowerCase()) !== -1;
            }

            if (pillMatch && searchMatch) {
                card.style.display = '';   // show
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        // toggle empty state
        if (visibleCount === 0) {
            emptyState.classList.add('svc-empty--visible');
        } else {
            emptyState.classList.remove('svc-empty--visible');
        }
    }

    // ── pill click handler ──
    pills.forEach(function (pill) {
        pill.addEventListener('click', function () {
            // update active pill style
            pills.forEach(function (p) { p.classList.remove('svc-pill--active'); });
            pill.classList.add('svc-pill--active');

            currentFilter = pill.getAttribute('data-filter');
            applyFilters();
        });
    });

    // ── live search handler ──
    searchBox.addEventListener('input', function () {
        applyFilters();
    });

});