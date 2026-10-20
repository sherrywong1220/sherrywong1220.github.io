---
layout: page
permalink: /research/
title: Research
description: Making emerging memory useful across the systems stack.
nav: true
nav_order: 1
---

My work connects memory hardware with the software that uses it: operating systems,
communication libraries, and LLM training and inference systems. I am interested in how these layers
can work together to improve performance with emerging memory technologies.

<section class="research-section" markdown="1">

<p class="topic-label">01 / MEMORY &amp; OPERATING SYSTEMS</p>

## Managing tiered memory

Adding a memory tier creates new decisions about where data should live and when it
should move. My work studies these decisions through real-device characterization,
adaptive tuning, and programmable memory management.

- **TierBPF** uses eBPF to control admission to page migration with policies informed by the memory architecture.
- **Hybrid Adaptive Tuning** combines offline profiling and online learning to tune memory-tiering parameters.
- **CXL characterization** measures real CXL devices and studies their use in HPC, LLM workloads, and memory placement.

[TierBPF · preprint](https://arxiv.org/abs/2604.12300) &nbsp; / &nbsp;
[Adaptive tuning · preprint](https://arxiv.org/abs/2604.12165) &nbsp; / &nbsp;
[Characterization · IPDPS 2025](https://doi.org/10.1109/IPDPS64566.2025.00097)

</section>

<section class="research-section" markdown="1">

<p class="topic-label">02 / AI/ML INFRASTRUCTURE</p>

## Optimizing LLM training and inference

I am interested in optimizing LLM training and inference with emerging memory technologies,
including CXL memory and heterogeneous memory tiers.

Long-context generation places pressure on both compute and memory. In **HybridGen**,
we study CPU–GPU collaborative attention for LLM inference with expanded tiered memory.
The work explores how to distribute computation across processors as the memory demands
of inference grow.

[HybridGen · preprint](https://arxiv.org/abs/2604.18529)

</section>

<section class="research-section" markdown="1">

<p class="topic-label">03 / PARALLEL &amp; DISTRIBUTED SYSTEMS</p>

## Communication and computation with shared memory

CXL memory sharing offers another way for machines to exchange data. **cMPI** explores
MPI one-sided and two-sided communication over shared CXL memory. I carried out this
research during an internship at **SK hynix**.

I also collaborate on **OCEAN**, a CXL emulation framework for studying multi-host memory
sharing and pooling, and **mLR**, which uses memoization and memory offloading for
scalable laminography reconstruction.

[cMPI · SC 2025](https://doi.org/10.1145/3712285.3759816) &nbsp; / &nbsp;
[OCEAN · SC 2026, accepted](https://sc26.conference-program.com/presentation/?id=pap148&sess=sess232) &nbsp; / &nbsp;
[mLR · SC 2025](https://doi.org/10.1145/3712285.3759805)

</section>

<div class="research-section" markdown="1">

The [full publication list]({{ '/publications/' | relative_url }}) includes papers, preprints, and available code.
For research conversations, reach me at [swang166@ucmerced.edu](mailto:swang166@ucmerced.edu).

</div>
