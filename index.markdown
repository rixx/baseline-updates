---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: post_list
---

Updates to the Baseline collection indicating which browser features are widely available. Including RSS feeds (both for all updates and [individual tags]({{ site.baseurl }}/tags)): <a href="{{ site.baseurl }}/feed.xml" style="display: inline; margin-left: 4px"><img height=24 style="margin-bottom: -4px" src="{{ site.baseurl }}/assets/rss.png"></a>

The data source is the [repository](https://github.com/web-platform-dx/web-features/) owned by W3C WebDX (aka web developer experience) Community Group. The data is updated every 24 hours. See also their definition of [high vs low Baseline support](https://github.com/web-platform-dx/web-features/blob/main/docs/baseline.md#status-definition), but tl;dr:

- **Low Baseline**: Each current stable release of the core browsers has full support. Core browsers are Safari (iOS and macOS), Chrome (Android and desktop), Edge, and Firefox (Android and desktop).
- **High Baseline**: The feature has been in Low Baseline for 30 months.

Built by [rixx](https://rixx.de) ([fedi](https://chaos.social/@rixx), [github](https://github.com/rixx)) out of the frustration of web.dev of all places not providing RSS feeds, and there being no other source of updates that say "hey, web dev, use this cool feature now".
