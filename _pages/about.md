---
layout: about
title: About
permalink: /
subtitle: Ph.D. candidate · University of California, Merced
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

I am **Xi (Sherry) Wang**, a Ph.D. candidate at the [University of California, Merced](https://www.ucmerced.edu/),
where I work with [Prof. Dong Li](https://faculty.ucmerced.edu/dong-li/) in the
[Parallel Architecture, System, and Algorithm (PASA) Lab](https://www.pasalabs.org/).
I joined the lab in Fall 2023.

My research focuses on **LLM systems, operating systems, and emerging memory technologies**,
including Compute Express Link (CXL). I study how software can make effective use of heterogeneous
memory, from memory management in the operating system to communication and inference runtimes.

Outside of research, I enjoy snowboarding 🏂, working out 🏋️‍♀️, tennis 🎾, climbing 🧗‍♀️, and surfing 🏄‍♀️.
When I’m away from campus and the office, you might find me hanging out on snowy slopes, on a tennis court, or at a climbing gym.

<div class="research-overview" markdown="1">

## Research Interests

- **Memory systems:** CXL memory, memory tiering, and programmable OS memory management.
- **LLM infrastructure:** inference across heterogeneous processors and memory tiers.
- **Parallel computing:** shared-memory communication and scalable scientific workloads.

[Explore my research →]({{ '/research/' | relative_url }})

</div>

<section class="industry-experience" aria-labelledby="industry-experience">
  <h2 id="industry-experience">Industry Experience</h2>
  <ul class="experience-list">
    {% for experience in site.data.experience %}
      <li>
        <div class="experience-heading">
          <h3>{{ experience.company }}</h3>
          {% if experience.period %}<span class="experience-period">{{ experience.period }}</span>{% endif %}
        </div>
        <p class="experience-role">{{ experience.role }}</p>
        {% if experience.description or experience.project %}
          <p class="experience-description">
            {{ experience.description }}
            {% if experience.project and experience.project_url %}<a href="{{ experience.project_url }}">{{ experience.project }}</a>.{% endif %}
          </p>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
</section>

## [Publications]({{ '/publications/' | relative_url }})

<div class="publications">
{% bibliography --query @inproceedings %}
</div>

### Preprints

<div class="publications">
{% bibliography --query @misc %}
</div>
