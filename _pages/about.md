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

- [Department of Software Engineering](https://www.gnu.ac.kr/soft/main.do) (Undergraduate)
- [Department of AI Convergence Engineering](https://www.gnu.ac.kr/soft/cm/cntnts/cntntsView.do?mi=13878&cntntsId=6487) (Graduate)
- Head, BK21 Phase 4 — [AI Convergence Research & Education Center for Industrial Intelligence in Gyeongsang Province](https://abc.gnu.ac.kr/)
- Adjunct Professor, [Department of Management of Technology](https://mot.gnu.ac.kr/) (Graduate)
- Adjunct Professor, [Department of Smart Manufacturing ICT](https://usg.ac.kr/) (Undergraduate, USG University)

<p class="contact-block">
  601-810, Gyeongsang National University<br />
  Jinjudaero 501, Jinju City<br />
  South Gyeongsang Province, Korea, 52828<br />
  Email: saleese at gnu dot ac dot kr<br />
  Phone: (82) 055-772-1377
</p>

<style>
  /* The page heading is built by the theme from site.first_name/last_name, and
     the body used to repeat the name to add the degree and the hanja. Appending
     them to the heading instead drops the repetition without touching the config
     values, which also drive the footer, the SEO metadata and the citation
     blocks. Scoped to this page: the style block only ships with about.md. */
  .post-title::after {
    content: ", Ph.D. (李宣我)";
    font-weight: 400;
    /* The layout puts a newline after the surname, which collapses to a space
       and would otherwise show up as "Lee , Ph.D." */
    margin-left: -0.26em;
  }

  /* The theme hardcodes this heading as lowercase "news" in its own layout, a
     file this repo must not own. Capitalising it here matches the other headings
     on the page — Research Interests, Tools Developed, Histories. */
  .post article h2:has(> a[href$="/news/"]) {
    text-transform: capitalize;
  }

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
  /* The diagram takes the left half of the block and the text the right. The
     content column is 900px, so half is 450px — which is also the previous 410px
     cap plus 10%, the two sizings landing on the same number. The source image is
     965x929, so 450px is still a downscale, not an upscale. The gutter comes out
     of the text's side, leaving it a little under half. */
  .ri-figure {
    float: left;
    width: 50%;
    max-width: 450px;
    margin: 0.25rem 1.75rem 0.25rem 0;
  }

  /* What sits under the diagram is the sum of two margins, not one: this
     wrapper's, and the 16px the theme puts on the <figure> the include emits.
     The closing paragraph clears the float, so clearance replaces that
     paragraph's own top margin and these two are the whole gap. Dropping the
     inner one leaves the wrapper's 0.25rem, so the text sits just under the
     image rather than 20px below it. */
  .ri-figure figure {
    margin-bottom: 0;
  }
  /* The closing paragraph used to begin alongside the diagram and then step back
     to the left margin partway through, so it read as two differently indented
     blocks. Clearing the float starts it below the diagram, flush left, as one
     block. Only the closing paragraph clears — the heading, the opening line and
     the three bullets are what the diagram is meant to sit beside. */
  .ri-block > p:last-of-type {
    clear: left;
  }

  /* The three areas ran tight against each other and ended 79px above the
     diagram, leaving a blank strip beside its lower edge. Opening them up gives
     each area its own block and closes most of that strip, stopping short of the
     diagram's lower edge rather than reaching it. The spacing is split three ways
     — before the list and between the items — rather than piled into the two
     gaps, which would read as three separate lists.

     These are fixed lengths against a reflowing column, so they hold only at full
     width; narrower and the text runs a little past the diagram, which the
     closing paragraph already clears. */
  .ri-block > ul {
    margin-top: 1.25rem;
  }

  .ri-block > ul > li + li {
    margin-top: 0.9rem;
  }

  @media (max-width: 768px) {
    .ri-figure {
      float: none;
      width: 100%;
      max-width: 450px;
      margin: 0 auto 1.25rem;
    }
  }
</style>

<div class="ri-block" markdown="1">

<!-- A plain <img> rather than figure.liquid: that include exists to generate
     responsive raster variants, which an SVG neither needs nor can produce.
     The cloud is built from the 138 publications and their abstracts, with each
     word placed in the area whose papers use it disproportionately. -->
<div class="ri-figure">
  <a href="{{ '/assets/img/research_interests_wordcloud.svg' | relative_url }}">
    <img
      src="{{ '/assets/img/research_interests_wordcloud.svg' | relative_url }}"
      class="img-fluid rounded"
      loading="eager"
      alt="Word cloud of the words used across these publications, grouped into Software Engineering, Artificial Intelligence and Drone Systems"
    />
  </a>
</div>

## Research Interests

My research interests are in **Software Engineering**, **Artificial Intelligence**, and **Drone Systems**.

- **Software Engineering.** I am interested in software evolution. In this area, I am working on requirement traceability, software architecture, documentation updates, code recommendations, and program comprehension.
- **Artificial Intelligence.** I am applying AI techniques such as LLMs, summarization, and classification techniques. I am also applying reinforcement learning techniques. I am interested in the trustworthiness of AI outcomes.
- **Drone Systems.** I am interested in autonomous drone flights. In this area, I am working on safety analysis techniques such as SACs, STPA, FTA, FMEA, etc.

Overall, I am interested in **intelligent software engineering**. I am also interested in improving the productivity of software developers. However, the problem is entangled with the quality of software products. I want to develop the tools and data to improve the status quo. For that, I consider a contextual overview of a software system, using keywords: _task relevance_, _entry points_, and _design evolution_. For a practical application, I am working on drone systems.

</div>

## Histories

- <a href="https://cs.kaist.ac.kr/board/view?bbs_id=news&amp;bbs_sn=6998&amp;menu=83">Dr. Seonah Lee has been appointed to the assistant professor of Gyeongsang University</a>, Mar. 21, 2016
- <a href="http://www.contrib.andrew.cmu.edu/org/littleredteam/">Little Red Team</a>, Mar. 5, 2005

## Tools Developed

- **NavClus** — <a href="http://github.com/saleese/navclus">github.com/saleese/navclus</a> (<a href="https://www.youtube.com/watch?v=rbrc5ERyWjQ">demo</a>)
- **NavMine** — <a href="http://www.navmine.com">navmine.com</a> (disabled for a while)
- **MI** — <a href="https://bitbucket.org/saleese/mi-ve">bitbucket.org/saleese/mi-ve</a>

<script>
  // The theme prints the news list after the whole page body. It belongs
  // directly under Research Interests, where it reads as what is currently
  // happening in those areas rather than as an afterthought at the end.
  //
  // Moved rather than reordered: the news block is a sibling of the content, not
  // a child, so `order` would need <article> to become a flex container — and
  // that would take the floated portrait out of the layout the page depends on.
  //
  // On DOMContentLoaded because this script is inline in the content, which the
  // theme renders before the news markup exists.
  document.addEventListener("DOMContentLoaded", function () {
    const news = document.querySelector("article .news");
    const anchor = document.querySelector(".ri-block");
    if (!news || !anchor) return;
    const heading = news.previousElementSibling;
    anchor.after(news);
    if (heading && heading.tagName === "H2") anchor.after(heading);
  });
</script>
