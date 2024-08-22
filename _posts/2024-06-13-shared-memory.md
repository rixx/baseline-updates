---
layout: post
title: "New in High Baseline Support: SharedArrayBuffer and Atomics"
tags: baseline-high javascript
---

[caniuse](https://caniuse.com/?search=shared-memory) · [mdn](https://developer.mozilla.org/en-US/search?q=SharedArrayBuffer and Atomics) · [spec](['https://tc39.es/ecma262/multipage/structured-data.html#sec-sharedarraybuffer-objects', 'https://tc39.es/ecma262/multipage/structured-data.html#sec-atomics-object'])

The `SharedArrayBuffer` object represents bytes shared between multiple workers and the main thread. The `Atomics` object safely accesses `SharedArrayBuffer` data to make sure predictable values are read and written and that operations are not interrupted.

### Source features

- ``javascript.builtins.Atomics`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics)
- ``javascript.builtins.Atomics.add`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.add)
- ``javascript.builtins.Atomics.and`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.and)
- ``javascript.builtins.Atomics.compareExchange`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.compareExchange)
- ``javascript.builtins.Atomics.exchange`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.exchange)
- ``javascript.builtins.Atomics.isLockFree`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.isLockFree)
- ``javascript.builtins.Atomics.load`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.load)
- ``javascript.builtins.Atomics.notify`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.notify)
- ``javascript.builtins.Atomics.or`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.or)
- ``javascript.builtins.Atomics.store`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.store)
- ``javascript.builtins.Atomics.sub`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.sub)
- ``javascript.builtins.Atomics.wait`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.wait)
- ``javascript.builtins.Atomics.xor`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.xor)
- ``javascript.builtins.DataView.DataView.sharedarraybuffer_support`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.DataView.DataView.sharedarraybuffer_support)
- ``javascript.builtins.SharedArrayBuffer`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.SharedArrayBuffer)
- ``javascript.builtins.SharedArrayBuffer.@@species`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.SharedArrayBuffer.@@species)
- ``javascript.builtins.SharedArrayBuffer.SharedArrayBuffer`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.SharedArrayBuffer.SharedArrayBuffer)
- ``javascript.builtins.SharedArrayBuffer.byteLength`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.SharedArrayBuffer.byteLength)
- ``javascript.builtins.SharedArrayBuffer.slice`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.SharedArrayBuffer.slice)
