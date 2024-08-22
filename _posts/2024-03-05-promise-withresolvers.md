---
layout: post
title: "New in Low Baseline Support: Promise.withResolvers()"
tags: baseline-low promises
---

[caniuse](https://caniuse.com/?search=promise-withresolvers) · [spec](https://tc39.es/proposal-promise-with-resolvers/#sec-promise.withResolvers)

The `Promise.withResolvers()` static method is an alternative to the `Promise()` constructor that returns both the promise and resolution functions. You can use this to access `resolve` and `reject` outside the scope of the executor function.

### Source features

- ``javascript.builtins.Promise.withResolvers`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.Promise.withResolvers)
