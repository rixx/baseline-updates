---
layout: post
title: "New in Low Baseline Support: RegExp.escape()"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=regexp-escape) · [mdn](https://developer.mozilla.org/en-US/search?q=RegExp.escape()) · [spec](https://tc39.es/proposal-regex-escaping/)

The `RegExp.escape()` static method takes a string and replaces any characters that are potentially special characters of a regular expression with equivalent escape sequences. For example, `RegExp.escape("[abc]")` returns `"\\[abc\\]"`.

### Source features

- ``javascript.builtins.RegExp.escape`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.RegExp.escape)
