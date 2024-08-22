---
layout: post
title: "New in High Baseline Support: Promise.any()"
tags: baseline-high promises
---

[caniuse](https://caniuse.com/?search=promise-any) · [mdn](https://developer.mozilla.org/en-US/search?q=Promise.any()) · [spec](https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-promise.any)

The `Promise.any()` static method returns a promise that fulfills as soon as the first of an iterable of promises fulfills, with that promise's value. Otherwise, it rejects with an `AggregateError` when all of the promises have rejected.

### Source features

- ``javascript.builtins.AggregateError`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.AggregateError)
- ``javascript.builtins.AggregateError.AggregateError`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.AggregateError.AggregateError)
- ``javascript.builtins.AggregateError.errors`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.AggregateError.errors)
- ``javascript.builtins.Promise.any`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Promise.any)
