---
layout: post
title: "New in Low Baseline Support: Gradient interpolation"
tags: baseline-low gradients
---

[caniuse](https://caniuse.com/?search=gradient-interpolation) · [mdn](https://developer.mozilla.org/en-US/search?q=Gradient interpolation) · [spec](https://drafts.csswg.org/css-color-4/#interpolation-space)

Gradient interpolation controls how the colors between gradient stops are calculated in CSS. For example, `linear-gradient(to right in oklch longer hue, red, red);` calculates in the `oklch` color space, with the hue going all the way around the hue circle from red back to red.

### Source features

- ``css.types.image.gradient.conic-gradient.hue_interpolation_method`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.conic-gradient.hue_interpolation_method)
- ``css.types.image.gradient.conic-gradient.interpolation_color_space`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.conic-gradient.interpolation_color_space)
- ``css.types.image.gradient.linear-gradient.hue_interpolation_method`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.linear-gradient.hue_interpolation_method)
- ``css.types.image.gradient.linear-gradient.interpolation_color_space`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.linear-gradient.interpolation_color_space)
- ``css.types.image.gradient.radial-gradient.hue_interpolation_method`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.radial-gradient.hue_interpolation_method)
- ``css.types.image.gradient.radial-gradient.interpolation_color_space`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.radial-gradient.interpolation_color_space)
- ``css.types.image.gradient.repeating-conic-gradient.hue_interpolation_method`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.repeating-conic-gradient.hue_interpolation_method)
- ``css.types.image.gradient.repeating-conic-gradient.interpolation_color_space`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.repeating-conic-gradient.interpolation_color_space)
- ``css.types.image.gradient.repeating-linear-gradient.hue_interpolation_method`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.repeating-linear-gradient.hue_interpolation_method)
- ``css.types.image.gradient.repeating-linear-gradient.interpolation_color_space`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.repeating-linear-gradient.interpolation_color_space)
- ``css.types.image.gradient.repeating-radial-gradient.hue_interpolation_method`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.repeating-radial-gradient.hue_interpolation_method)
- ``css.types.image.gradient.repeating-radial-gradient.interpolation_color_space`` [[mdn]](https://developer.mozilla.org/en-US/search?q=css.types.image.gradient.repeating-radial-gradient.interpolation_color_space)
