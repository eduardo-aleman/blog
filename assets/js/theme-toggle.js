// ====== THEME TOGGLE SCRIPT ======

(function() {
  const STORAGE_KEY = 'theme-preference';
  const HTML_TAG = document.documentElement;
  const THEME_TOGGLE_SELECTOR = '.theme-toggle';

  // Get saved theme preference or system preference
  function getThemePreference() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      return saved;
    }

    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }

    return 'light';
  }

  // Set theme and update DOM
  function setTheme(theme) {
    // Prevent FOUC (Flash of Unstyled Content)
    HTML_TAG.classList.remove('instant-load');
    
    if (theme === 'dark') {
      HTML_TAG.setAttribute('data-theme', 'dark');
      localStorage.setItem(STORAGE_KEY, 'dark');
    } else {
      HTML_TAG.removeAttribute('data-theme');
      localStorage.setItem(STORAGE_KEY, 'light');
    }

    // Update toggle button state
    updateToggleButton(theme);

    // Dispatch custom event for other scripts to listen
    const event = new CustomEvent('theme-changed', { detail: { theme } });
    document.dispatchEvent(event);
  }

  // Update toggle button appearance
  function updateToggleButton(theme) {
    const toggles = document.querySelectorAll(THEME_TOGGLE_SELECTOR);
    toggles.forEach(toggle => {
      toggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      toggle.setAttribute('aria-pressed', theme === 'dark');
    });
  }

  // Initialize theme on page load
  function init() {
    const preference = getThemePreference();
    setTheme(preference);

    // Add click handlers to toggle buttons
    const toggles = document.querySelectorAll(THEME_TOGGLE_SELECTOR);
    toggles.forEach(toggle => {
      toggle.addEventListener('click', handleToggleClick);
      toggle.addEventListener('keypress', handleToggleKeypress);
    });

    // Listen for system preference changes
    if (window.matchMedia) {
      const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
      darkModeQuery.addEventListener('change', (e) => {
        if (!localStorage.getItem(STORAGE_KEY)) {
          setTheme(e.matches ? 'dark' : 'light');
        }
      });
    }
  }

  // Handle toggle click
  function handleToggleClick(e) {
    e.preventDefault();
    const current = HTML_TAG.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    setTheme(next);
  }

  // Handle toggle keyboard interaction
  function handleToggleKeypress(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleToggleClick(e);
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose public API if needed
  window.themeToggle = {
    get current() {
      return HTML_TAG.getAttribute('data-theme') || 'light';
    },
    set(theme) {
      setTheme(theme);
    },
    toggle() {
      const current = window.themeToggle.current;
      window.themeToggle.set(current === 'dark' ? 'light' : 'dark');
    },
  };
})();

// ====== SMOOTH THEME TRANSITION ======
// Ensure smooth color transitions when theme changes

document.addEventListener('DOMContentLoaded', function() {
  // Add instant-load class to prevent transitions on initial load
  document.documentElement.classList.add('instant-load');
  
  // Remove it after a brief delay to allow styles to settle
  setTimeout(() => {
    document.documentElement.classList.remove('instant-load');
  }, 100);
});
