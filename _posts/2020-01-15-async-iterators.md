---
layout: post
title: "New in Low Baseline Support: Async iterators and the for await..of loop"
tags: baseline-low iterators
---

[caniuse](https://caniuse.com/?search=async-iterators) · [mdn](https://developer.mozilla.org/en-US/search?q=Async iterators and the for await..of loop) · [spec](['https://tc39.es/ecma262/multipage/control-abstraction-objects.html#sec-asynciteratorprototype', 'https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-for-in-and-for-of-statements'])

Asynchronous iterator objects, such as those returned by promises or generator functions, are iterable with the `for await .. of` loop.

### Source features

- ``javascript.statements.for_of.async_iterators`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.statements.for_of.async_iterators)
- ``javascript.builtins.AsyncIterator`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.AsyncIterator)
- ``javascript.builtins.AsyncIterator.@@asyncIterator`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.AsyncIterator.@@asyncIterator)
- ``javascript.builtins.Symbol.asyncIterator`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Symbol.asyncIterator)
- ``javascript.statements.for_await_of`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.statements.for_await_of)
