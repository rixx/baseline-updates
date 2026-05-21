---
layout: post
title: "New in High Baseline Support: Web authentication easy public key access"
tags: baseline-high webauthn
---

[caniuse](https://caniuse.com/?search=webauthn-public-key-easy) · [mdn](https://developer.mozilla.org/en-US/search?q=Web authentication easy public key access) · [spec](https://w3c.github.io/webauthn/#sctn-public-key-easy)

The `getAuthenticatorData()`, `getPublicKey()`, and `getPublicKeyAlgorithm()` methods of `AuthenticatorAttestationResponse` access credential data inside `attestationObject` without the need to parse it.

### Source features

- ``api.AuthenticatorAttestationResponse.getAuthenticatorData`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getAuthenticatorData)
- ``api.AuthenticatorAttestationResponse.getPublicKey`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKey)
- ``api.AuthenticatorAttestationResponse.getPublicKey.algorithm_es256`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKey.algorithm_es256)
- ``api.AuthenticatorAttestationResponse.getPublicKeyAlgorithm`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKeyAlgorithm)
- ``api.AuthenticatorAttestationResponse.getPublicKey.algorithm_eddsa`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKey.algorithm_eddsa)
- ``api.AuthenticatorAttestationResponse.getPublicKey.algorithm_rs256`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.AuthenticatorAttestationResponse.getPublicKey.algorithm_rs256)
