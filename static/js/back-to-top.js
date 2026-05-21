/**
 * Back to top
 * Reveals the .back-to-top link once the user has scrolled past
 * SHOW_THRESHOLD pixels, and smooth-scrolls to the top on click
 * (respecting prefers-reduced-motion).
 *
 * pageshow handles bfcache restoration on iOS Safari and Firefox —
 * without it, the class can be stuck out of sync with scroll position
 * after a back/forward navigation. visibilitychange covers the case
 * of switching back to the tab on mobile.
 */
(() => {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  const SHOW_THRESHOLD = 400;

  const update = () => {
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

  // Initial state — handles fresh loads and scroll-position restoration
  update();

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('pageshow', update);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) update();
  });

  btn.addEventListener('click', scrollToTop);
})();
