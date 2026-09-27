document.addEventListener("click", (event) => {
  const target = event.target.closest("a, button, label");
  if (!target || !window.dataLayer) {
    return;
  }

  window.gtag = window.gtag || function () {
    window.dataLayer.push(arguments);
  };

  const pagePath = window.location.pathname;

  if (target.matches(".md-clipboard")) {
    const code = target.closest(".highlight")?.querySelector("code");
    const language = [...(code?.classList ?? [])]
      .find((name) => name.startsWith("language-"))
      ?.replace("language-", "");

    window.gtag("event", "code_copy", {
      page_path: pagePath,
      code_language: language || "unknown",
    });
    return;
  }

  if (
    target.matches(".tabbed-labels > label") &&
    /\/models(?:\/advanced)?\/?$/.test(pagePath)
  ) {
    window.gtag("event", "model_tab_select", {
      page_path: pagePath,
      model_name: target.textContent.trim(),
    });
    return;
  }

  const languageLink = target.closest("a[hreflang]");
  if (languageLink) {
    window.gtag("event", "language_switch", {
      page_path: pagePath,
      language: languageLink.hreflang,
    });
  }
});
