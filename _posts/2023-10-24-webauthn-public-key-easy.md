---
layout: post
title: "New in Low Baseline Support: Web authentication easy public key access"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=webauthn-public-key-easy) · [mdn](https://developer.mozilla.org/en-US/search?q=Web authentication easy public key access) · [spec](https://w3c.github.io/webauthn/#sctn-public-key-easy)

The `getAuthenticatorData()`, `getPublicKey()`, and `getPublicKeyAlgorithm()` methods of `AuthenticatorAttestationResponse` access credential data inside `attestationObject` without the need to parse it.

### Source features

- ``api.AuthenticatorAttestationResponse.getAuthenticatorData`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getAuthenticatorData)
- ``api.AuthenticatorAttestationResponse.getPublicKey`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKey)
- ``api.AuthenticatorAttestationResponse.getPublicKeyAlgorithm`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKeyAlgorithm)
