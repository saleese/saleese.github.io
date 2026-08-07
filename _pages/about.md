---
layout: about
title: introduction
permalink: /
subtitle: Professor, <a href="https://www.gnu.ac.kr/">Gyeongsang National University</a> · Software Evolution and Architecture Lab

profile:
  align: left
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>601-810, Gyeongsang National University</p>
    <p>Jinjudaero 501, Jinju City</p>
    <p>South Gyeongsang Province, Korea, 52828</p>
    <p>Phone: (82) 055-772-1377</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

**Seonah Lee, Ph.D. (李宣我)**

I am a Professor at Gyeongsang National University, where I direct the **Software Evolution and Architecture Lab**.

- Department of Software Engineering (Undergraduate)
- Department of Aerospace and Software Engineering (Undergraduate)
- Head, BK21 Phase 4 — AI Convergence Research & Education Center for Industrial Intelligence in Gyeongsang Province
- Adjunct Professor, Department of Management of Technology (Graduate)
- Adjunct Professor, Department of Smart Manufacturing ICT (Undergraduate, USG University)

<style>
  /* Keep the portrait near its native 140x180 so it is not upscaled and blurry,
     which also keeps the right-hand profile column short. */
  @media (min-width: 769px) {
    .profile img {
      max-width: 190px;
    }
  }

  /* The theme sets the address block in a monospace face; use the body font. */
  .profile .more-info {
    font-family: inherit;
  }

  /* Research-interests block: diagram floated left, text wrapping to its right,
     mirroring the layout of the original site. Stacks on narrow screens. */
  .ri-block {
    /* start below the floated profile photo, as the original site does */
    clear: both;
  }
  .ri-block::after {
    content: "";
    display: table;
    clear: both;
  }
  .ri-figure {
    float: left;
    width: 36%;
    max-width: 320px;
    margin: 0.25rem 1.75rem 0.75rem 0;
  }
  @media (max-width: 768px) {
    .ri-figure {
      float: none;
      width: 100%;
      max-width: 320px;
      margin: 0 auto 1.25rem;
    }
  }
</style>

<div class="ri-block" markdown="1">

<div class="ri-figure">
  {% include figure.liquid loading="eager" path="assets/img/research_interests.png" class="img-fluid rounded" alt="Research interests: Software Engineering, Artificial Intelligence, and Drone Systems" %}
</div>

## Research Interests

My research interests are in **Software Engineering**, **Artificial Intelligence**, and **Drone Systems**.

- **Software Engineering.** I am interested in software evolution. In this area, I am working on requirement traceability, software architecture, documentation updates, code recommendations, and program comprehension.
- **Artificial Intelligence.** I am applying AI techniques such as LLMs, summarization, and classification techniques. I am also applying reinforcement learning techniques. I am interested in the trustworthiness of AI outcomes.
- **Drone Systems.** I am interested in autonomous drone flights. In this area, I am working on safety analysis techniques such as SACs, STPA, FTA, FMEA, etc.

Overall, I am interested in **intelligent software engineering**. I am also interested in improving the productivity of software developers. However, the problem is entangled with the quality of software products. I want to develop the tools and data to improve the status quo. For that, I consider a contextual overview of a software system, using keywords: _task relevance_, _entry points_, and _design evolution_. For a practical application, I am working on drone systems.

</div>

## Tools Developed

- **NavClus** — <a href="http://github.com/saleese/navclus">github.com/saleese/navclus</a>
- **NavMine** — <a href="http://www.navmine.com">navmine.com</a> (disabled for a while)
- **MI** — <a href="https://bitbucket.org/saleese/mi-ve">bitbucket.org/saleese/mi-ve</a>

## Histories

- Dr. Seonah Lee has been appointed to the assistant professor of Gyeongsang University, Mar. 21, 2016
- Little Red Team, Mar. 5, 2005
