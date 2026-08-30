---
layout: default
title: Podcast Intelligence
---

{% assign published_digests = site.pages | where: "digest", true | sort: "date" | reverse %}
{% assign latest_digest = published_digests | first %}
{{ latest_digest.content }}

## Previous digests

{% for digest in published_digests offset:1 %}
- [{{ digest.date | date: "%Y-%m-%d" }}]({{ digest.url | relative_url }})
{% endfor %}
