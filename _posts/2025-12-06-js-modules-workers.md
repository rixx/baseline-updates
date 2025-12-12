---
layout: post
title: "New in High Baseline Support: JavaScript modules in workers"
tags: baseline-high js-modules workers
---

[caniuse](https://caniuse.com/?search=js-modules-workers) · [mdn](https://developer.mozilla.org/en-US/search?q=JavaScript modules in workers) · [spec](https://html.spec.whatwg.org/multipage/workers.html#dom-worker-dev)

The `Worker()` constructor accepts `{ type: "module" }` to load scripts that use `import` and `export`. Also known as ECMAScript modules or ESM in workers.

### Source features

- ``api.Worker.Worker.ecmascript_modules`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Worker.Worker.ecmascript_modules)
- ``api.Worker.Worker.options_type_parameter`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Worker.Worker.options_type_parameter)
- ``javascript.operators.import.worker_support`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.operators.import.worker_support)
- ``javascript.statements.import.worker_support`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.statements.import.worker_support)
