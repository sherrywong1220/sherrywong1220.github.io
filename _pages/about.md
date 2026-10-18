---
layout: about
title: About
permalink: /
subtitle: Ph.D. student · Computer Science · University of California, Merced
profile:
  align: right
  image: xi-sherry-wang.jpg
  image_circular: false
  more_info: >
    <p>PASA Lab · UC Merced</p>
    <p>Merced, California</p>
selected_papers: false
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

I am **Xi (Sherry) Wang**, a Ph.D. student at the [University of California, Merced](https://www.ucmerced.edu/),
where I work with [Prof. Dong Li](https://faculty.ucmerced.edu/dong-li/) in the
[Parallel Architecture, System, and Algorithm (PASA) Lab](https://www.pasalabs.org/).
I joined the lab in Fall 2023.

My research focuses on **LLM systems, operating systems, and emerging memory technologies**,
including Compute Express Link (CXL). I study how software can make effective use of heterogeneous
memory, from memory management in the operating system to communication and inference runtimes.

<div class="profile-links">
  <a class="email" href="mailto:swang166@ucmerced.edu">swang166@ucmerced.edu</a>
  <a href="https://scholar.google.com/citations?user=JHXk0gcAAAAJ">Google Scholar</a>
  <a href="https://www.linkedin.com/in/xi-sherry-wang/">LinkedIn</a>
</div>

<div class="research-overview" markdown="1">

## Research Interests

- **Memory systems:** CXL memory, memory tiering, and programmable OS memory management.
- **LLM infrastructure:** inference across heterogeneous processors and memory tiers.
- **Parallel computing:** shared-memory communication and scalable scientific workloads.

[Explore my research →]({{ '/research/' | relative_url }})

</div>

## [Publications]({{ '/publications/' | relative_url }})

<div class="publications">
{% bibliography --query @inproceedings %}
</div>

### Preprints

<div class="publications">
{% bibliography --query @misc %}
</div>
