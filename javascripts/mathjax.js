window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// mkdocs-material exposes `document$` (an RxJS observable) only when
// instant navigation is enabled. Without it, MathJax auto-typesets on
// the initial page load and we do not need to re-typeset. Guard the
// subscription so this file does not throw a ReferenceError on themes
// or setups without `document$`.
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
}
