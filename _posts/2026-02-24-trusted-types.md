---
layout: post
title: "New in Low Baseline Support: Trusted types"
tags: baseline-low security
---

[caniuse](https://caniuse.com/?search=trusted-types) · [mdn](https://developer.mozilla.org/en-US/search?q=Trusted types) · [spec](https://w3c.github.io/trusted-types/dist/spec/)

Trusted types allow you to lock down insecure parts of the DOM API and prevent client-side cross-site scripting (XSS) attacks.

### Source features

- ``api.Element.innerHTML.enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Element.innerHTML.enforces_trusted_types)
- ``api.HTMLScriptElement.innerText.enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLScriptElement.innerText.enforces_trusted_types)
- ``api.HTMLScriptElement.src.enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLScriptElement.src.enforces_trusted_types)
- ``api.HTMLScriptElement.text.enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLScriptElement.text.enforces_trusted_types)
- ``api.HTMLScriptElement.textContent.enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.HTMLScriptElement.textContent.enforces_trusted_types)
- ``api.ShadowRoot.innerHTML.enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.ShadowRoot.innerHTML.enforces_trusted_types)
- ``api.TrustedHTML`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedHTML)
- ``api.TrustedHTML.toString`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedHTML.toString)
- ``api.TrustedScript`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedScript)
- ``api.TrustedScript.toString`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedScript.toString)
- ``api.TrustedScriptURL`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedScriptURL)
- ``api.TrustedScriptURL.toString`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedScriptURL.toString)
- ``api.TrustedTypePolicy`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicy)
- ``api.TrustedTypePolicy.createHTML`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicy.createHTML)
- ``api.TrustedTypePolicy.createScript`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicy.createScript)
- ``api.TrustedTypePolicy.createScriptURL`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicy.createScriptURL)
- ``api.TrustedTypePolicy.name`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicy.name)
- ``api.TrustedTypePolicyFactory`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory)
- ``api.TrustedTypePolicyFactory.createPolicy`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.createPolicy)
- ``api.TrustedTypePolicyFactory.defaultPolicy`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.defaultPolicy)
- ``api.TrustedTypePolicyFactory.emptyHTML`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.emptyHTML)
- ``api.TrustedTypePolicyFactory.emptyScript`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.emptyScript)
- ``api.TrustedTypePolicyFactory.getAttributeType`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.getAttributeType)
- ``api.TrustedTypePolicyFactory.getPropertyType`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.getPropertyType)
- ``api.TrustedTypePolicyFactory.isHTML`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.isHTML)
- ``api.TrustedTypePolicyFactory.isScript`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.isScript)
- ``api.TrustedTypePolicyFactory.isScriptURL`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedTypePolicyFactory.isScriptURL)
- ``api.setInterval.code_param_enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.setInterval.code_param_enforces_trusted_types)
- ``api.setTimeout.code_param_enforces_trusted_types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.setTimeout.code_param_enforces_trusted_types)
- ``api.trustedTypes`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.trustedTypes)
- ``http.headers.Content-Security-Policy.require-trusted-types-for`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.headers.Content-Security-Policy.require-trusted-types-for)
- ``http.headers.Content-Security-Policy.trusted-types`` [[mdn]](https://developer.mozilla.org/en-US/search?q=http.headers.Content-Security-Policy.trusted-types)
- ``api.TrustedHTML.toJSON`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedHTML.toJSON)
- ``api.TrustedScript.toJSON`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedScript.toJSON)
- ``api.TrustedScriptURL.toJSON`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.TrustedScriptURL.toJSON)
