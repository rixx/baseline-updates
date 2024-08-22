---
layout: post
title: "New in Low Baseline Support: requestAnimationFrame() in workers"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=request-animation-frame-workers) · [spec](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#animation-frames)

The `requestAnimationFrame()` method in workers schedules a function that runs before the next repaint. Together with offscreen canvas, you can animate content from a worker.

### Source features

- ``api.DedicatedWorkerGlobalScope.cancelAnimationFrame`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.DedicatedWorkerGlobalScope.cancelAnimationFrame)
- ``api.DedicatedWorkerGlobalScope.requestAnimationFrame`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q=api.DedicatedWorkerGlobalScope.requestAnimationFrame)
