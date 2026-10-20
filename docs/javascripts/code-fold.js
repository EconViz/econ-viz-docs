/*
 * Line numbers and folding for code blocks longer than 15 lines.
 *
 * Click the number of a line that opens a block (a header with an indented body, a comment
 * above a chunk of code, a TOML section) to fold the block away. The number of a folded block
 * stays highlighted; hover it to see what the block does. Copying a block always copies all of it.
 */
(() => {
  const MIN_LINES = 15; // blocks with more lines than this get numbers and folding
  const MIN_HIDDEN = 3; // a fold must hide at least this many lines
  const MIN_HIDDEN_TOML = 2;

  const COUNT = {
    en: (n) => `${n} lines`,
    "zh-TW": (n) => `${n} 行`,
    "zh-CN": (n) => `${n} 行`,
  };
  const lang = () => {
    const value = document.documentElement.lang || "en";
    return COUNT[value] ? value : value.startsWith("zh") ? "zh-TW" : "en";
  };

  // ---------------------------------------------------------------- lines

  /** Split highlighted markup at newlines, closing and reopening tags so that each line stands alone. */
  const splitLines = (html) => {
    const lines = [];
    const open = [];
    let current = "";
    for (const [, tag, text] of html.matchAll(/(<[^>]+>)|([^<]+)/g)) {
      if (tag) {
        if (tag.startsWith("</")) open.pop();
        else if (!tag.endsWith("/>")) open.push(tag);
        current += tag;
        continue;
      }
      const parts = text.split("\n");
      parts.forEach((part, index) => {
        current += part;
        if (index < parts.length - 1) {
          lines.push(current + closing(open));
          current = open.join("");
        }
      });
    }
    if (current.replace(/<[^>]+>/g, "") !== "") lines.push(current + closing(open));
    return lines;
  };

  const closing = (open) =>
    open
      .slice()
      .reverse()
      .map((tag) => `</${/^<(\w+)/.exec(tag)[1]}>`)
      .join("");

  const plain = (html) => {
    const holder = document.createElement("div");
    holder.innerHTML = html;
    return holder.textContent;
  };

  // -------------------------------------------------------------- regions

  const indent = (line) => /^ */.exec(line)[0].length;
  const blank = (line) => !line.trim();
  const comment = (line) => line.trim().startsWith("#");
  const uncomment = (line) => line.trim().replace(/^#+\s?/, "").trim();

  /** The comment lines directly above `index`, as one sentence. */
  const commentAbove = (lines, index) => {
    const found = [];
    for (let k = index - 1; k >= 0 && comment(lines[k]) && indent(lines[k]) === indent(lines[index]); k--) {
      found.unshift(uncomment(lines[k]));
    }
    return found.join(" ");
  };

  /** A one-line docstring right under a header, if there is one. */
  const docstring = (lines, index) => {
    const next = lines[index + 1] || "";
    const match = /^\s*(?:"""|''')(.+?)(?:"""|''')\s*$/.exec(next);
    return match ? match[1].trim() : "";
  };

  const trailingComment = (line) => {
    const match = /\s#\s(.+?)\s*$/.exec(line);
    return match ? match[1] : "";
  };

  const headerText = (line) => line.trim().replace(/[(\[{:,]\s*$/, "") + (/[(\[{]\s*$/.test(line) ? "(…)" : "");

  const lastVisible = (lines, from, to) => {
    let end = to;
    while (end > from && blank(lines[end])) end--;
    return end;
  };

  /** start -> {end, text}: folding `start` hides start+1 .. end. */
  const pythonRegions = (lines) => {
    const regions = new Map();
    const count = lines.length;
    for (let i = 0; i < count; i++) {
      if (blank(lines[i])) continue;
      const base = indent(lines[i]);
      let next = i + 1;
      while (next < count && blank(lines[next])) next++;
      if (comment(lines[i])) {
        // a comment group followed by code: fold the code up to the next group
        if (i + 1 < count && comment(lines[i + 1]) && indent(lines[i + 1]) === base) continue;
        let end = i;
        for (let k = i + 1; k < count; k++) {
          if (blank(lines[k])) continue;
          if (indent(lines[k]) < base || (comment(lines[k]) && indent(lines[k]) === base)) break;
          end = k;
        }
        end = lastVisible(lines, i, end);
        if (end - i >= MIN_HIDDEN) regions.set(i, { end, text: commentAbove(lines, i + 1) || uncomment(lines[i]) });
        continue;
      }
      if (next < count && indent(lines[next]) > base) {
        let end = next;
        for (let k = next + 1; k < count; k++) {
          if (blank(lines[k])) continue;
          if (indent(lines[k]) <= base) break;
          end = k;
        }
        end = lastVisible(lines, i, end);
        if (end - i >= MIN_HIDDEN) {
          const text =
            docstring(lines, i) || commentAbove(lines, i) || trailingComment(lines[i]) || headerText(lines[i]);
          if (!regions.has(i)) regions.set(i, { end, text });
        }
      }
    }
    return regions;
  };

  const tomlRegions = (lines) => {
    const regions = new Map();
    const starts = lines.map((line, i) => (/^\s*\[.+\]/.test(line) ? i : -1)).filter((i) => i >= 0);
    starts.forEach((start, n) => {
      let end = (starts[n + 1] ?? lines.length) - 1;
      while (end > start && (blank(lines[end]) || comment(lines[end]))) end--; // the next section's comments
      if (end - start >= MIN_HIDDEN_TOML) {
        regions.set(start, {
          end,
          text: commentAbove(lines, start) || trailingComment(lines[start]) || lines[start].trim().replace(/\s+#.*$/, ""),
        });
      }
    });
    return regions;
  };

  // ------------------------------------------------------------ the block

  const tip = (() => {
    let element = null;
    return {
      show(text, x, y) {
        if (!element) {
          element = document.createElement("div");
          element.className = "ev-fold-tip";
          document.body.appendChild(element);
        }
        element.textContent = text;
        element.style.left = `${x}px`;
        element.style.top = `${y}px`;
        element.dataset.visible = "";
      },
      hide() {
        if (element) delete element.dataset.visible;
      },
    };
  })();

  const enhance = (code) => {
    const htmlLines = splitLines(code.innerHTML);
    if (htmlLines.length <= MIN_LINES) return;
    const texts = htmlLines.map(plain);
    // the highlighter does not record the language, so tell TOML from Python by its section headers
    const isToml = texts.some((line) => /^\[[\w.-]+\]\s*(#.*)?$/.test(line)) && texts.some((line) => /^\w+ = /.test(line));
    const regions = isToml ? tomlRegions(texts) : pythonRegions(texts);

    code.classList.add("ev-numbered");
    code.style.setProperty("--ev-digits", String(Math.max(2, String(htmlLines.length).length)));
    code.innerHTML = htmlLines
      .map((html, i) => {
        const region = regions.get(i);
        const attrs = `class="ev-line" data-n="${i + 1}"${region ? ' data-fold="" data-m="▾ "' : ""}`;
        return `<span ${attrs}>${html}${region ? '<span class="ev-dots"></span>' : ""}\n</span>`;
      })
      .join("");

    const lineElements = [...code.querySelectorAll(".ev-line")];
    const folded = new Set();

    const render = () => {
      const hidden = new Set();
      for (const start of folded) {
        for (let k = start + 1; k <= regions.get(start).end; k++) hidden.add(k);
      }
      lineElements.forEach((element, i) => {
        element.toggleAttribute("data-hidden", hidden.has(i));
        const isFolded = folded.has(i);
        element.toggleAttribute("data-folded", isFolded);
        if (regions.has(i)) element.dataset.m = isFolded ? "▸ " : "▾ ";
      });
    };

    const gutter = (element, event) => {
      const style = getComputedStyle(element, "::before");
      const rect = element.getClientRects()[0];
      const width = parseFloat(style.width) + parseFloat(style.marginRight) || 0;
      return rect && event.clientX >= rect.left && event.clientX <= rect.left + width ? rect : null;
    };

    code.addEventListener("click", (event) => {
      const element = event.target.closest(".ev-line");
      if (!element || !element.hasAttribute("data-fold") || !gutter(element, event)) return;
      const index = lineElements.indexOf(element);
      if (folded.has(index)) folded.delete(index);
      else folded.add(index);
      render();
      moved(event);
    });

    const moved = (event) => {
      const element = event.target.closest && event.target.closest(".ev-line");
      const rect = element && element.hasAttribute("data-folded") && gutter(element, event);
      if (!rect) return tip.hide();
      const index = lineElements.indexOf(element);
      const region = regions.get(index);
      const hiddenCount = region.end - index;
      tip.show(`${region.text} · ${COUNT[lang()](hiddenCount)}`, rect.left, rect.top);
    };
    code.addEventListener("mousemove", moved);
    code.addEventListener("mouseleave", () => tip.hide());
    code.addEventListener("scroll", () => tip.hide());
  };

  const run = () => {
    document
      .querySelectorAll(".md-typeset .highlight pre > code")
      .forEach((code) => {
        if (!code.classList.contains("ev-numbered")) enhance(code);
      });
  };

  if (window.document$ && window.document$.subscribe) window.document$.subscribe(run);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
