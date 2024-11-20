---
layout: post
title: "New in High Baseline Support: Mixed content handling"
tags: baseline-high security
---

[caniuse](https://caniuse.com/?search=mixed-content) · [mdn](https://developer.mozilla.org/en-US/search?q=Mixed content handling) · [spec](https://w3c.github.io/webappsec-mixed-content/)

When a document is loaded over HTTPS, browsers ensure that none of the document's resources are loaded over an insecure protocol. Instead, resources that the document attempts to load over an insecure protocol are either loaded over HTTPS or are blocked.

### Source features

- ``http.mixed-content`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content)
- ``http.mixed-content.blockable_mixed_content`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.blockable_mixed_content)
- ``http.mixed-content.auto_upgrade_video_audio`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.auto_upgrade_video_audio)
- ``http.mixed-content.auto_upgrade_images`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.auto_upgrade_images)
- ``http.mixed-content.block_mixed_downloads`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.block_mixed_downloads)
- ``http.mixed-content.allow_loopback_url`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.allow_loopback_url)
- ``http.mixed-content.allow_localhost_url`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.allow_localhost_url)
- ``http.mixed-content.allow_file_urls`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.mixed-content.allow_file_urls)
