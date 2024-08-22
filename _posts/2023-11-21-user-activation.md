---
layout: post
title: "New in Low Baseline Support: User activation"
tags: baseline-low
---

[caniuse](https://caniuse.com/?search=user-activation) · [spec](https://html.spec.whatwg.org/multipage/interaction.html#the-useractivation-interface)

The `navigator.userActivation` API reveals whether the user has interacted with the page through an "activation" gesture such as a click, tap, or key press. User activation gated APIs (such as the fullscreen API) fail without user interaction, and this API allows you to predict such a failure.

### Source features

- ``api.Navigator.userActivation`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.Navigator.userActivation)
- ``api.UserActivation`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.UserActivation)
- ``api.UserActivation.hasBeenActive`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.UserActivation.hasBeenActive)
- ``api.UserActivation.isActive`` [[mdn]](https://developer.mozilla.org/en-US/search?q=api.UserActivation.isActive)
