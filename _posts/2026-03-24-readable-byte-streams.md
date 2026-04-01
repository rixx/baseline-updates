---
layout: post
title: "New in Low Baseline Support: Readable byte streams"
tags: baseline-low streams
---

[caniuse](https://caniuse.com/?search=readable-byte-streams) · [mdn](https://developer.mozilla.org/en-US/search?q=Readable byte streams) · [spec](https://streams.spec.whatwg.org/)

A `ReadableStream` constructed with `{ type: "bytes" }` reads bytes from a stream without making extra copies, improving efficiency for streams of large chunks. Also known as BYOB or bring your own buffer.

### Source features

- ``api.ReadableByteStreamController`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableByteStreamController)
- ``api.ReadableByteStreamController.byobRequest`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableByteStreamController.byobRequest)
- ``api.ReadableByteStreamController.close`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableByteStreamController.close)
- ``api.ReadableByteStreamController.desiredSize`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableByteStreamController.desiredSize)
- ``api.ReadableByteStreamController.enqueue`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableByteStreamController.enqueue)
- ``api.ReadableByteStreamController.error`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableByteStreamController.error)
- ``api.ReadableStreamBYOBReader`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader)
- ``api.ReadableStreamBYOBReader.ReadableStreamBYOBReader`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.ReadableStreamBYOBReader)
- ``api.ReadableStreamBYOBReader.cancel`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.cancel)
- ``api.ReadableStreamBYOBReader.closed`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.closed)
- ``api.ReadableStreamBYOBReader.read`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.read)
- ``api.ReadableStreamBYOBReader.releaseLock`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.releaseLock)
- ``api.ReadableStreamBYOBRequest`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBRequest)
- ``api.ReadableStreamBYOBRequest.respond`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBRequest.respond)
- ``api.ReadableStreamBYOBRequest.respondWithNewView`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBRequest.respondWithNewView)
- ``api.ReadableStreamBYOBRequest.view`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBRequest.view)
- ``api.ReadableStreamBYOBReader.releaseLock.reject_pending_read_request`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.releaseLock.reject_pending_read_request)
- ``api.ReadableStreamBYOBReader.read.options_min_parameter`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ReadableStreamBYOBReader.read.options_min_parameter)
