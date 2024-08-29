---
layout: post
title: "New in Low Baseline Support: String isWellFormed() and toWellFormed()"
tags: baseline-low string
---

[caniuse](https://caniuse.com/?search=string-wellformed) · [mdn](https://developer.mozilla.org/en-US/search?q=String isWellFormed() and toWellFormed()) · [spec](https://tc39.es/ecma262/multipage/text-processing.html#sec-string-objects)

The `isWellFormed()` method of strings returns a boolean indicating if the string contains any Unicode lone surrogates. The `toWellFormed()` method returns a new string where all lone surrogates are replaced by the Unicode replacement character.

### Source features

- ``javascript.builtins.String.isWellFormed`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.String.isWellFormed)
- ``javascript.builtins.String.toWellFormed`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.builtins.String.toWellFormed)
