---
layout: post
title: "New in Low Baseline Support: JavaScript modules in shared workers"
tags: baseline-low js-modules workers
---

[caniuse](https://caniuse.com/?search=js-modules-shared-workers) · [mdn](https://developer.mozilla.org/en-US/search?q=JavaScript modules in shared workers) · [spec](https://html.spec.whatwg.org/multipage/workers.html#shared-workers-and-the-sharedworker-interface:dom-sharedworker-2)

The `SharedWorker()` constructor accepts `{ type: "module" }` to load scripts that use `import` and `export`. Also known as ECMAScript modules or ESM in shared workers.

### Source features

- ``api.SharedWorker.SharedWorker.ecmascript_modules`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.SharedWorker.SharedWorker.ecmascript_modules)
- ``api.SharedWorker.SharedWorker.options_type_parameter`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.SharedWorker.SharedWorker.options_type_parameter)
