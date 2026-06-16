/*
  main.js — Members Club
  How to load this in Django templates:
    1. {% load static %}
    2. <script src="{% static 'members/js/main.js' %}"></script>
  Place the <script> tag at the bottom of <body> (after content renders).
*/

// ── Delete confirmation ────────────────────────────────────────────────────────
// Called by onsubmit="return confirmDelete('...')" on delete forms.
// Returning false cancels the form submission.
function confirmDelete(memberName) {
    return window.confirm(
        'Are you sure you want to delete "' + memberName + '"?\nThis action cannot be undone.'
    );
}

// ── DOM-ready logic ────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function () {

    // Populate avatar placeholder letters from data-name attribute.
    // The Django template already injects the first letter, but this
    // keeps the JS version as a backup example.
    var placeholders = document.querySelectorAll('[data-name]');
    placeholders.forEach(function (el) {
        if (el.textContent.trim() === '') {
            var name = el.getAttribute('data-name') || '?';
            el.textContent = name.charAt(0).toUpperCase();
        }
    });

    // Auto-dismiss flash / alert messages after 3 seconds.
    var flashes = document.querySelectorAll('.flash-message');
    flashes.forEach(function (msg) {
        setTimeout(function () {
            msg.style.transition = 'opacity 0.5s ease';
            msg.style.opacity = '0';
            setTimeout(function () { msg.remove(); }, 500);
        }, 3000);
    });

    // Highlight the active nav link.
    var currentPath = window.location.pathname;
    var navLinks = document.querySelectorAll('.navbar a');
    navLinks.forEach(function (link) {
        if (link.getAttribute('href') === currentPath) {
            link.style.fontWeight = '700';
            link.style.opacity = '1';
        }
    });

});
