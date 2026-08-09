---
layout: about
title: introduction
permalink: /
subtitle: Professor, <a href="https://www.gnu.ac.kr/">Gyeongsang National University</a> · <a href="http://selab.gnu.ac.kr/">Software Evolution and Architecture Lab</a>

profile:
  align: left
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p><a href="https://scholar.google.com/citations?user=4bEToL8AAAAJ">Google Scholar</a></p>
    <p><a href="https://dblp.org/pid/l/SeonahLee.html">DBLP</a></p>
    <p><a href="https://orcid.org/0000-0002-2004-2924">ORCID</a></p>

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

- [Department of Software Engineering](https://www.gnu.ac.kr/soft/main.do) (Undergraduate)
- Head, BK21 Phase 4 — [AI Convergence Research & Education Center for Industrial Intelligence in Gyeongsang Province](https://abc.gnu.ac.kr/)
- Adjunct Professor, [Department of Management of Technology](https://mot.gnu.ac.kr/) (Graduate)
- Adjunct Professor, [Department of Smart Manufacturing ICT](https://usg.ac.kr/) (Undergraduate, USG University)

<p class="contact-block">
  601-810, Gyeongsang National University<br />
  Jinjudaero 501, Jinju City<br />
  South Gyeongsang Province, Korea, 52828<br />
  Phone: (82) 055-772-1377
</p>

<style>
  /* prof_pic.jpg is 140x180, so capping at 140px shows it pixel-for-pixel — no
     scaling in either direction. The theme otherwise stretches it to the full
     profile column. Only applies from 769px up; below that the theme gives the
     portrait the full column, which is its intended responsive behaviour. */
  @media (min-width: 769px) {
    .profile img {
      max-width: 140px;
    }
  }

  /* The theme sets the block under the portrait in a monospace face; use the body font. */
  .profile .more-info {
    font-family: inherit;
  }

  /* The theme lays those entries out as inline-block, which runs the profile
     links together on one line. One per line instead. */
  .profile .more-info p {
    display: block;
    margin-bottom: 0.15rem;
  }

  /* Contact details sit beside the floated portrait, under the affiliation list.
     Without its own formatting context the text wraps around the portrait and
     the last line drops to the left margin below it. */
  .contact-block {
    overflow: hidden;
    margin-top: 1rem;
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
  /* Sized to match the original site, which renders this diagram at 409px wide.
     Its labels are small enough that the earlier 320px cap made them unreadable.
     The source image is 861x829, so 410px is still a downscale, not an upscale. */
  .ri-figure {
    float: left;
    width: 46%;
    max-width: 410px;
    margin: 0.25rem 1.75rem 0.75rem 0;
  }
  @media (max-width: 768px) {
    .ri-figure {
      float: none;
      width: 100%;
      max-width: 410px;
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

- **NavClus** — <a href="http://github.com/saleese/navclus">github.com/saleese/navclus</a> (<a href="https://www.youtube.com/watch?v=rbrc5ERyWjQ">demo</a>)
- **NavMine** — <a href="http://www.navmine.com">navmine.com</a> (disabled for a while)
- **MI** — <a href="https://bitbucket.org/saleese/mi-ve">bitbucket.org/saleese/mi-ve</a>

## Histories

- <a href="https://cs.kaist.ac.kr/board/view?bbs_id=news&amp;bbs_sn=6998&amp;menu=83">Dr. Seonah Lee has been appointed to the assistant professor of Gyeongsang University</a>, Mar. 21, 2016
- <a href="http://www.contrib.andrew.cmu.edu/org/littleredteam/">Little Red Team</a>, Mar. 5, 2005
