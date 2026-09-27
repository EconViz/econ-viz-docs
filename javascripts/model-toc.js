document.addEventListener("DOMContentLoaded", () => {
  const path = window.location.pathname.replace(/\/+$/, "");
  if (!/\/models(?:\/advanced)?(?:\/index\.html)?$/.test(path)) {
    return;
  }

  const article = document.querySelector(".md-content article");
  const tocs = document.querySelectorAll(
    ".md-sidebar--secondary .md-nav--secondary > .md-nav__list"
  );

  if (!article || !tocs.length || !article.querySelector(".tabbed-set")) {
    return;
  }

  const slugify = (value) =>
    value
      .trim()
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, "-")
      .replace(/^-|-$/g, "");

  const sections = new Map();

  const setExpandedSection = (activeHeading) => {
    for (const [heading, entries] of sections) {
      const expanded = heading === activeHeading;

      for (const { sectionLink, toggle, nested } of entries) {
        sectionLink.classList.toggle(
          "ev-model-toc__section--active",
          expanded
        );
        toggle.setAttribute("aria-expanded", String(expanded));
        nested.hidden = !expanded;
      }
    }
  };

  for (const toc of tocs) {
    for (const item of toc.children) {
      const sectionLink = item.querySelector(":scope > .md-nav__link");
      if (!sectionLink) {
        continue;
      }

      const heading = article.querySelector(sectionLink.hash);
      let tabs = heading?.nextElementSibling;

      while (tabs && tabs.tagName !== "H2" && !tabs.matches(".tabbed-set")) {
        tabs = tabs.nextElementSibling;
      }

      if (!tabs?.matches(".tabbed-set")) {
        continue;
      }

      const labels = [
        ...tabs.querySelectorAll(":scope > .tabbed-labels > label"),
      ];
      if (!labels.length) {
        continue;
      }

      item.classList.add("ev-model-toc__item");
      sectionLink.classList.add("ev-model-toc__section");

      const toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "ev-model-toc__toggle";
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", sectionLink.textContent.trim());

      const nested = document.createElement("nav");
      nested.className = "md-nav ev-model-toc__children";
      nested.hidden = true;

      const list = document.createElement("ul");
      list.className = "md-nav__list";

      if (!sections.has(heading)) {
        sections.set(heading, []);
      }
      sections.get(heading).push({ sectionLink, toggle, nested });

      labels.forEach((label) => {
        const name = label.textContent.trim();
        const anchor = `${heading.id}-${slugify(name)}`;
        label.id = anchor;

        const child = document.createElement("li");
        child.className = "md-nav__item";

        const link = document.createElement("a");
        link.className = "md-nav__link";
        link.href = `#${anchor}`;
        link.textContent = name;
        link.addEventListener("click", () => label.click());

        child.append(link);
        list.append(child);

        if (window.location.hash === `#${anchor}`) {
          label.click();
        }
      });

      toggle.addEventListener("click", () => {
        heading.scrollIntoView({ behavior: "smooth", block: "start" });
      });

      nested.append(list);
      sectionLink.after(toggle, nested);
    }
  }

  if (!sections.size) {
    return;
  }

  const headings = [...sections.keys()].sort(
    (a, b) => a.offsetTop - b.offsetTop
  );
  const articleHeadings = [...article.querySelectorAll("h2")];
  let scheduled = false;

  const updateExpandedSection = () => {
    scheduled = false;
    const marker = Math.min(window.innerHeight * 0.25, 160);
    let activeHeading = null;

    for (const heading of headings) {
      const nextHeading = articleHeadings.find(
        (candidate) => candidate.offsetTop > heading.offsetTop
      );
      const start = heading.getBoundingClientRect().top;
      const end = nextHeading
        ? nextHeading.getBoundingClientRect().top
        : article.getBoundingClientRect().bottom;

      if (start <= marker && end > marker) {
        activeHeading = heading;
        break;
      }
    }

    setExpandedSection(activeHeading);
  };

  const scheduleUpdate = () => {
    if (scheduled) {
      return;
    }

    scheduled = true;
    window.requestAnimationFrame(updateExpandedSection);
  };

  window.addEventListener("scroll", scheduleUpdate, { passive: true });
  window.addEventListener("resize", scheduleUpdate);
  window.addEventListener("hashchange", scheduleUpdate);
  scheduleUpdate();
});
