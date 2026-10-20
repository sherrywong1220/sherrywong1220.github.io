---
layout: about
title: About
permalink: /
subtitle: Ph.D. candidate · University of California, Merced
profile:
  align: right
  image: xi-sherry-wang.jpg
  image_circular: false
selected_papers: false
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

{% if site.serve_schema_org %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": {{ '/' | absolute_url | append: '#person' | jsonify }},
  "name": "Xi (Sherry) Wang",
  "alternateName": ["Xi Wang", "Sherry Wang"],
  "url": {{ '/' | absolute_url | jsonify }}
}
</script>
{% endif %}

Hello! I am a Ph.D. candidate at the [UC Merced](https://www.ucmerced.edu/),
where I have been working with [Prof. Dong Li](https://faculty.ucmerced.edu/dong-li/) in the
[PASA Lab](https://www.pasalabs.org/) since 2023.

My research focuses on optimizing **LLM systems and operating systems** with **emerging memory technologies** (e.g., CXL memory).

Outside of research, I enjoy snowboarding 🏂, working out 🏋️‍♀️, tennis 🎾, climbing 🧗‍♀️, and surfing 🏄‍♀️.
When I’m away from campus and the office, you might find me hanging out in the snowy mountains, on a tennis court, or at a climbing gym.

<div class="research-overview" markdown="1">

## Research Interests

- **Memory systems:** CXL memory, memory tiering, and programmable OS memory management.
- **AI/ML infrastructure:** optimizing LLM training and inference with emerging memory technologies.
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
{% bibliography %}
</div>
