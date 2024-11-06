---
layout: post
title: "New in Low Baseline Support: Threads and atomics (WebAssembly)"
tags: baseline-low webassembly
---

[caniuse](https://caniuse.com/?search=wasm-threads) · [mdn](https://developer.mozilla.org/en-US/search?q=Threads and atomics (WebAssembly)) · [spec](https://github.com/WebAssembly/threads/blob/main/proposals/threads/Overview.md)

Threads in WebAssembly run code in parallel, while atomic memory instructions can guarantee that no two threads can read or write to shared memory at the same time.

### Source features

- ``webassembly.api.Memory.Memory.shared`` [[mdn]](https://developer.mozilla.org/en-US/search?q=webassembly.api.Memory.Memory.shared)
- ``webassembly.threads-and-atomics`` [[mdn]](https://developer.mozilla.org/en-US/search?q=webassembly.threads-and-atomics)
