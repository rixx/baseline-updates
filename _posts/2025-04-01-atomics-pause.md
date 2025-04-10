---
layout: post
title: "New in Low Baseline Support: Atomics.pause()"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=atomics-pause) · [mdn](https://developer.mozilla.org/en-US/search?q=Atomics.pause()) · [spec](https://tc39.es/proposal-atomics-microwait/)

The `Atomics.pause()` static method gives a hint to the CPU that the code calling the method is in a short-duration wait for shared memory, known as spinning or a spinlock.

### Source features

- ``javascript.builtins.Atomics.pause`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Atomics.pause)
