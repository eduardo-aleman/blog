/**
 * Back to top
 * Reveals the .back-to-top link once the user has scrolled past
 * SHOW_THRESHOLD pixels, and smooth-scrolls to the top on click
 * (respecting prefers-reduced-motion).
 */
(() => {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  const SHOW_THRESHOLD = 400;

  const toggle = () => {
    btn.classList.toggle('is-visible', window.scrollY > SHOW_THRESHOLD);
  };

  const scrollToTop = (e) => {
    e.preventDefault();
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({
      top: 0,
      behavior: reduceMotion ? 'auto' : 'smooth',
    });
  };

  // Initial state — handles page reloads at non-zero scroll
  toggle();

  window.addEventListener('scroll', toggle, { passive: true });
  btn.addEventListener('click', scrollToTop);
})();
