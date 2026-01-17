---
layout: post
title: "New in Low Baseline Support: JavaScript modules in service workers"
tags: baseline-low js-modules workers
---

[caniuse](https://caniuse.com/?search=js-modules-service-workers) · [mdn](https://developer.mozilla.org/en-US/search?q=JavaScript modules in service workers) · [spec](https://w3c.github.io/ServiceWorker/#dom-registrationoptions-type)

The `navigator.serviceWorker.register()` method accepts `{ type: "module" }` to load scripts that use `import` and `export`. Also known as ECMAScript modules or ESM in service workers.

### Source features

- ``api.ServiceWorker.ecmascript_modules`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ServiceWorker.ecmascript_modules)
- ``javascript.statements.import.service_worker_support`` [[mdn]](https://developer.mozilla.org/en-US/search?q=javascript.statements.import.service_worker_support)
