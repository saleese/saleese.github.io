---
layout: post
title: Testing the research-area label on blog posts
date: 2026-08-10 10:00:00 +0900
description: A test post that checks the AI badge renders beside a post title on the blog index.
area: ai
tags: test
categories: notes
---

This post exists to check one thing: that a post can declare a research area in
its front matter and have that area show up as a badge next to its title on the
[blog index](/blog/).

## How a post declares its area

Add an `area` key to the front matter. It takes the same three values the rest of
the site uses:

```yaml
---
layout: post
title: Your title
date: 2026-08-10 10:00:00 +0900
area: ai # se | ai | aero
---
```

`se` is software engineering, `ai` is artificial intelligence, and `aero` is
aerospace engineering. This post is `ai`, so its badge is the pale blue one.

The colours are the ones from the Venn diagram on the introduction page, and they
are defined in a single place, so the badge here, the group headings on the
courses page and the labels on the publications page all agree.

A post that leaves `area` out simply renders its title with no badge, so nothing
has to be backfilled.
