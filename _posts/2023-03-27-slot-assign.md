---
layout: post
title: "New in Low Baseline Support: Imperative slot assignment"
tags: baseline-low web-components
---

[caniuse](https://caniuse.com/?search=slot-assign) · [mdn](https://developer.mozilla.org/en-US/search?q=Imperative slot assignment) · [spec](https://html.spec.whatwg.org/multipage/scripting.html#dom-slot-assign)

The `assign()` method for `<slot>` elements assigns nodes to the slot, as an alternative to using the `slot` and `name` HTML attributes. The nodes must be children of a shadow host and the shadow root must be created with the `slotAssignment` set to "manual". Also known as manual slot assignment.

### Source features

- ``api.HTMLSlotElement.assign`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLSlotElement.assign)
- ``api.ShadowRoot.slotAssignment`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ShadowRoot.slotAssignment)
