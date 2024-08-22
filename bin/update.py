from yaml import load, Loader
from pathlib import Path
import datetime as dt

BASE_DIR = Path(__file__).parent.parent.parent
FEATURE_PATH = BASE_DIR / "web-features" / "features"
POST_PATH = BASE_DIR / "baseline-updates" / "_posts"
TITLES = {
    "baseline-low": "New in Low Baseline Support",
    "baseline-high": "New in High Baseline Support",
}
NOW = dt.datetime.now().strftime("%Y-%m-%d")

feature_feed = []


def get_date(date_or_str):
    if isinstance(date_or_str, dt.date):
        return date_or_str
    date_or_str = date_or_str.strip("<>=≤")
    return dt.datetime.strptime(date_or_str, "%Y-%m-%d").date()


for dist_file in FEATURE_PATH.glob("*.yml.dist"):
    # can't use .stem because it will remove only the .dist
    feature_name = dist_file.name.split(".")[0]
    with open(dist_file) as f:
        feature = load(f, Loader=Loader)
        if not "status" in feature:
            continue
        with open(str(dist_file)[: -len(".dist")], "r") as f:
            details = load(f, Loader=Loader)
        if "baseline_low_date" in feature["status"]:
            feature_feed.append(
                {
                    "name": feature_name,
                    "sort_date": get_date(feature["status"]["baseline_low_date"]),
                    "event": "baseline-low",
                    "data": feature,
                    "details": details,
                }
            )
        if "baseline_high_date" in feature["status"]:
            feature_feed.append(
                {
                    "name": feature_name,
                    "sort_date": get_date(feature["status"]["baseline_high_date"]),
                    "event": "baseline-high",
                    "data": feature,
                    "details": details,
                }
            )


feature_feed.sort(key=lambda x: x["sort_date"], reverse=True)

for feature in feature_feed:
    md_path = (
        POST_PATH / f"{feature['sort_date'].strftime('%Y-%m-%d')}-{feature['name']}.md"
    )
    if md_path.exists():
        # TODO: we probably want a flag to still update the file in the future
        continue
    tags = [feature["event"]]
    if group := feature["details"].get("group"):
        if isinstance(group, list):
            tags.extend(group)
        else:
            tags.append(feature["details"]["group"])
    tags = " ".join(tags)
    title = f"{TITLES[feature['event']]}: {feature['details']['name']}"
    escaped_title = title.replace('"', '\\"')
    content = f"""---
layout: post
title: "{escaped_title}"
tags: {tags}
---

[caniuse](https://caniuse.com/?search={feature['name']})"""
    if "spec" in feature["details"]:
        content += f" · [spec]({feature['details']['spec']})"
    content += "\n\n"
    if "description" in feature["details"]:
        content += f"{feature['details']['description']}\n\n"
    if "support" in feature["data"]:
        content += f"### Support\n\n<small>At the time of writing this file, {NOW}.</small>\n\n"
        for browser, version in feature["data"]["status"]["support"].items():
            content += f"- {browser}: {version}\n"
    if "compat_features" in feature["data"]:
        content += f"### Source features\n\n"
        for compat_feature in feature["data"]["compat_features"]:
            content += f"- ``{compat_feature}`` [[mdn]](https://https://developer.mozilla.org/en-US/search?q={compat_feature})\n"
    with open(md_path, "w") as f:
        f.write(content)
