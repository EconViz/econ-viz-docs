(() => {
  const activeClass = "ev-api__parameter--highlight";
  let active;

  function highlight() {
    let id;
    try {
      id = decodeURIComponent(window.location.hash.slice(1));
    } catch {
      return;
    }
    const target = document.getElementById(id);
    active?.classList.remove(activeClass);
    active = null;
    if (!target?.matches(".ev-api__parameter")) return;
    // Restart the animation even when the same parameter is clicked again.
    void target.offsetWidth;
    target.classList.add(activeClass);
    active = target;
  }

  window.addEventListener("hashchange", highlight);
  document.addEventListener("click", (event) => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey ||
        event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest("a[href]");
    if (!link || link.target === "_blank") return;
    const url = new URL(link.href, window.location.href);
    if (url.origin === location.origin && url.pathname === location.pathname &&
        url.search === location.search && url.hash === location.hash) {
      highlight();
    }
  });
  document.addEventListener("animationend", (event) => {
    if (event.animationName === "ev-parameter-highlight") {
      event.target.classList.remove(activeClass);
      if (active === event.target) active = null;
    }
  });
  if (typeof document$ !== "undefined") {
    document$.subscribe(highlight);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", highlight);
  } else {
    highlight();
  }
})();
