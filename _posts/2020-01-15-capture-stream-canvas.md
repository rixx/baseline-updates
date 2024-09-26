---
layout: post
title: "New in Low Baseline Support: captureStream() for <canvas>"
tags: baseline-low canvas
---

[caniuse](https://caniuse.com/?search=capture-stream-canvas) · [mdn](https://developer.mozilla.org/en-US/search?q=captureStream() for <canvas>) · [spec](https://w3c.github.io/mediacapture-fromelement/#html-canvas-element-media-capture-extensions)

The `captureStream()` method for `<canvas>` elements returns a `MediaStream` which includes a `CanvasCaptureMediaStreamTrack` representing real-time video of the canvas image. You can use this to record the canvas, or send it elsewhere, such as another canvas or WebRTC connection.

### Source features

- ``api.HTMLCanvasElement.captureStream`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLCanvasElement.captureStream)
- ``api.CanvasCaptureMediaStreamTrack`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.CanvasCaptureMediaStreamTrack)
- ``api.CanvasCaptureMediaStreamTrack.canvas`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.CanvasCaptureMediaStreamTrack.canvas)
- ``api.CanvasCaptureMediaStreamTrack.requestFrame`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.CanvasCaptureMediaStreamTrack.requestFrame)
