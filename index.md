---
layout: default
title: Podcast Intelligence
---

{% assign published_digests = site.pages | where: "digest", true | sort: "date" | reverse %}
{% assign latest_digest = published_digests | first %}
{{ latest_digest.content }}

## Previous digests

{% assign current_month = "" %}
{% for digest in published_digests offset:1 %}
  {% assign digest_month = digest.date | date: "%B %Y" %}
  {% if digest_month != current_month %}
    {% unless forloop.first %}
</ul>
    {% endunless %}
<h3>{{ digest_month }}</h3>
<ul>
    {% assign current_month = digest_month %}
  {% endif %}
  {% assign episode_count = digest.episode_titles | size %}
  {% assign additional_count = episode_count | minus: 1 %}
<li><a href="{{ digest.url | relative_url }}">{{ digest.date | date: "%Y-%m-%d" }}</a>{% if episode_count > 0 %} — {{ digest.episode_titles | first | escape }}{% endif %}{% if additional_count > 0 %} · +{{ additional_count }} more{% endif %}</li>
  {% if forloop.last %}
</ul>
  {% endif %}
{% endfor %}
