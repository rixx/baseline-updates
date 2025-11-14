---
layout: post
title: "New in Low Baseline Support: Atomics.waitAsync"
tags: baseline-low javascript
---

[caniuse](https://caniuse.com/?search=atomics-wait-async) · [mdn](https://developer.mozilla.org/en-US/search?q=Atomics.waitAsync) · [spec](https://tc39.es/ecma262/multipage/structured-data.html#sec-atomics.waitasync)

The `Atomics.waitAsync()` static method waits for a value in a shared memory location, providing a promise when the expected value is not yet in memory. The `waitAsync()` method is a non-blocking alternative to `Atomics.wait()`.

### Source features

- ``javascript.builtins.Atomics.waitAsync`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.waitAsync)
