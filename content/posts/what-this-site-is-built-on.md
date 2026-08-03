+++
title = "What this site is built on"
description = "One binary, one stylesheet, two scripts, and no build step that is not the generator."
date = 2026-08-02
toc = false
+++

This site is built by [sqzass](@/projects/sqzass.md), which I wrote, and
deployed to GitHub Pages from a workflow that installs the binary and runs it.
There is no bundler, no package manager, and no `node_modules`.

That is not asceticism. It is that every one of those would be a thing that can
break between me writing a sentence and the sentence appearing.

## The whole stack

**One stylesheet.** Not twenty. The reference I looked at while designing this
ships twenty separate render-blocking stylesheets, which is twenty requests
before the first paint on a cold cache. One file, content-hashed by the
generator, invalidates only when it changes.

**Two scripts, both optional.** One runs the search palette, one handles the
theme toggle and the scroll reveals. Turn JavaScript off and you lose the
palette and get every section already revealed. Nothing you came here to read
depends on either.

**No web font for Korean.** A Hangul webfont with real coverage is around two
megabytes. The system stack — Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic —
is already on the machine and already correct. The only font this site downloads
is JetBrains Mono, which is Latin-only and 21 KB, and it earns that by being the
second voice: dates, badges, commands, the wordmark.

## The part that took the longest

Not the layout. The dates — see
[the other post](@/posts/listings-that-cannot-show-their-own-dates.md).

## Reproducible, and checked

Two builds of the same input produce identical bytes, and CI verifies it by
building twice and diffing. It sounds like a purity exercise until the first
time a deploy produces a diff you cannot explain, and you find out whether your
generator is deterministic at the moment you most need it to be.
