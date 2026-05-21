/**
 * Back to top
 *
 * Reveals the arrow once the user has scrolled past SHOW_THRESHOLD,
 * hides it again when scrolling back up or when the footer comes into
 * view (so the arrow doesn't overlap with footer content), and smooth-
 * scrolls to the top on click (respecting prefers-reduced-motion).
 *
 * Uses fixed positioning + IntersectionObserver instead of a sticky
 * rail. Sticky was fragile on mobile because of how flex ancestors and
 * body overflow interact to establish containing blocks — fixed has no
 * such dependencies.
 *
 * pageshow + visibilitychange handle bfcache restoration on iOS Safari
 * and tab returns on mobile, where scroll events don't always fire to
 * re-sync the visibility class.
 */
(() => {
  const btn = document.querySelector('.back-to-top');
  if (!btn) return;

  const SHOW_THRESHOLD = 400;

  let scrolledFarEnough = false;
  let footerInView = false;

  const sync = () => {
    btn.classList.toggle('is-visible', scrolledFarEnough && !footerInView);
  };

  const onScroll = () => {
    scrolledFarEnough = window.scrollY > SHOW_THRESHOLD;
    sync();
  };

  const scrollToTop = (e) => {
    e.preventDefault();
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({
      top: 0,
      behavior: reduceMotion ? 'auto' : 'smooth',
    });
    // Hide the arrow immediately. iOS Safari swallows scroll events
    // during programmatic smooth scrolling, so onScroll won't fire to
    // flip scrolledFarEnough back to false — the arrow would stay
    // visible at the top of the page until the user scrolled manually.
    scrolledFarEnough = false;
    sync();
  };

  // Initial sync — handles fresh loads and scroll-position restoration
  onScroll();

  window.addEventListener('scroll', onScroll, { passive: true });
  // scrollend fires once scrolling fully stops — useful belt-and-suspenders
  // for mobile where intermediate scroll events can be throttled during
  // momentum scrolling. Supported in Safari 18.2+, recent Chrome/Firefox.
  window.addEventListener('scrollend', onScroll);
  window.addEventListener('pageshow', onScroll);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) onScroll();
  });

  // Hide the arrow when the footer scrolls into view, so it doesn't
  // overlap with footer links. This recreates the "flows with content"
  // feel of the previous sticky design.
  const footer = document.querySelector('.site-footer');
  if (footer && 'IntersectionObserver' in window) {
    new IntersectionObserver((entries) => {
      footerInView = entries[0].isIntersecting;
      sync();
    }, { threshold: 0 }).observe(footer);
  }

  btn.addEventListener('click', scrollToTop);
})();
