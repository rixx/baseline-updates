---
layout: post
title: "New in Low Baseline Support: Unsanitized HTML parsing methods"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=parse-html-unsafe) · [spec](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#unsafe-html-parsing-methods)

The `Document.parseHTMLUnsafe()` static method parses HTML into a DOM tree, while the `setHTMLUnsafe()` method of `Element` and `ShadowRoot` parses and inserts HTML into an existing tree. No sanitization applies to these methods, so never call them with user-provided HTML strings.

### Source features

- ``api.Element.setHTMLUnsafe`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Element.setHTMLUnsafe)
- ``api.ShadowRoot.setHTMLUnsafe`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ShadowRoot.setHTMLUnsafe)
- ``api.Document.parseHTMLUnsafe_static`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Document.parseHTMLUnsafe_static)
