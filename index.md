---
layout: default
title: Podcast Intelligence
---

# Podcast Intelligence

{% assign published_digests = site.pages | where: "digest", true | sort: "date" | reverse %}
{% for digest in published_digests %}
## [{{ digest.date | date: "%Y-%m-%d" }}]({{ digest.url | relative_url }})

<ul>
{% for episode_title in digest.episode_titles %}
  <li>{{ episode_title | escape }}</li>
{% endfor %}
</ul>

{% endfor %}
