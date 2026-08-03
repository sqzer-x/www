+++
title = "About"
description = "Who is behind sqzer.com, and what gets built here."
weight = 30
template = "about.html"

[extra]
portrait     = "images/profile.jpg"
portrait_alt = "sqzer-x"

# 개인적인 세부(이름, 소속, 사는 곳, 이력)는 일부러 비워 두었다. 지어내는 것보다
# 없는 편이 낫고, 채우는 건 본인만 할 수 있다.
+++

I write software that runs in a terminal, and tools that look at networks I have
permission to look at. This site collects both, plus notes about the problems
that made me build them.

## What gets built here

Two kinds of things, and they are not really separate.

The first is software I use every day and could not find in the shape I wanted.
[ommp](@/projects/ommp.md) plays music without asking me to start a daemon
first. [sqzass](@/projects/sqzass.md) builds this site, and refuses to publish a
link that goes nowhere. Both are Rust, both are one binary, and both exist
because the alternative had one assumption I did not share.

The second is reconnaissance tooling for internal networks — the kind that has
to work with no route to the internet. [uaf](@/projects/uaf.md) finds wireless
access points and says which ones are open. [udfx](@/projects/udfx.md) reads the
DNS zone straight out of Active Directory with a plain domain account.
[usfx](@/projects/usfx.md) enumerates subdomains with twelve techniques, none of
which call a service. They are named alike on purpose: same job, different layer.

## How I work

Small tools, one job each, and a strong preference for the version with fewer
moving parts. I would rather ship one binary than a client and a server. I would
rather a build fail loudly than a site publish quietly with a broken link — which
is a whole design philosophy in [sqzass](@/projects/sqzass.md), and the reason
this page cannot link to a file that is not there.

Rust for the things that have to be fast and stay installed. Python and
PowerShell for the things that run once, in someone else's environment, with
whatever is already on the box.

## Elsewhere

Longer and less technical writing lives on my personal blog at
[blog.sqzer.com](https://blog.sqzer.com). Everything I have published is on
[GitHub](https://github.com/sqzer-x).
