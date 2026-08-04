+++
title = "Listings that cannot show their own dates"
description = "A generator that sorts by date and then hides it. What the fix cost, and what I left out."
date = 2026-08-03
toc = true
+++

[sqzass](@/projects/sqzass.md) has always been able to sort a section by date.
Put `sort_by = "date"` on a section index and its pages come out newest first,
undated ones last. That part worked.

What it could not do was show the date.

Templates see a listing as `page.children`, and every entry in it was exactly
four fields — `title`, `description`, `url`, `weight`. So a blog index could be
in perfect chronological order and have no way to say so. The order was real and
invisible, which is the worst of both: the reader cannot tell whether the list is
sorted or just arranged.

## The workaround I did not take

The obvious escape hatch is `[extra]`, a free-form table that reaches templates
untouched. Write the dates there, key them by URL, match them back up in the
template:

```toml
[[extra.year]]
label = "2026"
posts = [{ url = "/posts/some-post/", date = "08.03" }]
```

It works. It also means every new post is two edits in two files, and the second
one is the one you forget. A mapping maintained by hand next to the thing it
describes is a mapping that drifts, and the first rename breaks it silently —
the entry just stops matching and the date quietly disappears.

## What it actually cost

One field on one struct, and six places that build it:

```rust
pub struct PageRefCtx {
    pub title: String,
    pub description: String,
    pub url: String,
    pub weight: i64,
    pub date: Option<PageDate>,
}
```

The value goes through a single helper, so a listing and the page it links to
cannot disagree about what day something was published. A section's date comes
from its own `_index.md`; a section with no index has none.

That is the whole change. It is smaller than the workaround it replaces.

## What I deliberately left out

The same struct is one field away from being genuinely useful for a projects
index — put `extra` on it and every listing could carry arbitrary metadata:
language badges, links, status.

I did not add it, and the reason is where `PageRefCtx` is used. It is not only
`page.children`. It is also what the whole `site.sections` navigation tree is
made of, and that tree is serialised once per language and shared by every page
on the site. Putting each page's `[extra]` in it would drag every feature list
and every code sample into the navigation snapshot — a per-page cost paid by
pages that never look at it.

A date is five small fields. An open table is however much you wrote today.

So the projects index on this site still keeps its catalogue in one place by
hand, and a CI step checks that every entry points at a page that exists. That
is a worse answer than the one I just rejected for dates, and it is the right
one here, because the thing that made the date fix cheap is exactly what makes
the `extra` version expensive.
