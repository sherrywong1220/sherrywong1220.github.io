---
layout: page
permalink: /publications/
title: Publications
description: Research on memory systems, LLM inference, and high-performance computing.
nav: true
nav_order: 2
---

For citation metrics and my Scholar profile, visit [Google Scholar](https://scholar.google.com/citations?user=JHXk0gcAAAAJ).
Preprints are listed separately from conference papers.

{% include bib_search.liquid %}

## Conference Papers

<div class="publications">
{% bibliography --query @inproceedings %}
</div>

## Preprints

<div class="publications">
{% bibliography --query @misc %}
</div>
