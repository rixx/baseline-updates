---
layout: post
title: "New in Low Baseline Support: dialog.requestClose()"
tags: baseline-low html-elements
---

[caniuse](https://caniuse.com/?search=requestclose) · [mdn](https://developer.mozilla.org/en-US/search?q=dialog.requestClose()) · [spec](https://html.spec.whatwg.org/multipage/interactive-elements.html#dom-dialog-requestclose)

The `requestClose()` method of a `<dialog>` HTML element closes the dialog, firing a `cancel` event first, which listeners can use to prevent the dialog from closing. This differs from the `close()` method, which only fires the non-cancelable `close` event.

### Source features

- ``api.HTMLDialogElement.requestClose`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLDialogElement.requestClose)
