---
layout: post
title: "New in Low Baseline Support: X-Frame-Options"
tags: baseline-low security
---

[caniuse](https://caniuse.com/?search=x-frame-options) · [mdn](https://developer.mozilla.org/en-US/search?q=X-Frame-Options) · [spec](https://html.spec.whatwg.org/multipage/speculative-loading.html#the-x-frame-options-header)

The `X-Frame-Options` HTTP header limits where a document may be embedded in an iframe. The `X-Frame-Options: SAMEORIGIN` header disallows embedding in another origin. The `X-Frame-Options: DENY` header disallows embedding in any context, regardless of origin.


### Source features

- ``http.headers.X-Frame-Options`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.headers.X-Frame-Options)
- ``http.headers.X-Frame-Options.DENY`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.headers.X-Frame-Options.DENY)
- ``http.headers.X-Frame-Options.SAMEORIGIN`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.headers.X-Frame-Options.SAMEORIGIN)
