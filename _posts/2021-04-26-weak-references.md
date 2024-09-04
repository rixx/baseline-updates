---
layout: post
title: "New in Low Baseline Support: Weak references"
tags: baseline-low javascript
---

[caniuse](https://caniuse.com/?search=weak-references) · [mdn](https://developer.mozilla.org/en-US/search?q=Weak references) · [spec](['https://tc39.es/ecma262/multipage/managing-memory.html#sec-managing-memory'])

The `WeakRef` and `FinalizationRegistry` objects hold references to garbage-collectable objects without creating strong references that prevent their garbage collection.

### Source features

- ``javascript.builtins.FinalizationRegistry`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.FinalizationRegistry)
- ``javascript.builtins.FinalizationRegistry.FinalizationRegistry`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.FinalizationRegistry.FinalizationRegistry)
- ``javascript.builtins.FinalizationRegistry.register`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.FinalizationRegistry.register)
- ``javascript.builtins.FinalizationRegistry.unregister`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.FinalizationRegistry.unregister)
- ``javascript.builtins.WeakRef`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.WeakRef)
- ``javascript.builtins.WeakRef.WeakRef`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.WeakRef.WeakRef)
- ``javascript.builtins.WeakRef.deref`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.WeakRef.deref)
