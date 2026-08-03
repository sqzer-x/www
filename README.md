# sqzer.com

Personal site — projects, technical posts, and an about page. English and Korean.

Built with [sqzass](https://github.com/sqzer-x/sqzass), deployed to GitHub Pages.
No bundler, no package manager, no `node_modules`.

## Working on it

```bash
sqzass serve -i .     # http://127.0.0.1:3000, live reload
sqzass build -i .     # writes ./public
python3 tools/check.py
```

`sqzass` currently needs the `feat/pageref-date` branch — the Posts ledger reads
`child.date`, which `PageRefCtx` did not carry before
([sqzer-x/sqzass#1](https://github.com/sqzer-x/sqzass/pull/1)). Once that merges,
drop `--branch` from `.github/workflows/pages.yml`.

```bash
cargo install --git https://github.com/sqzer-x/sqzass --branch feat/pageref-date --locked
```

## Layout

| | |
|---|---|
| `content/` | pages. `page.md` is English, `page.ko.md` is Korean |
| `templates/` | minijinja. `base.html` owns the chrome; each index names its own template |
| `static/` | one stylesheet, two scripts, one font, the images |
| `i18n/` | UI strings the templates supply. A key missing from one language is a build error |
| `tools/check.py` | the two things the build does not check for you |

## Adding things

**A post.** Drop a file in `content/posts/`. `title` and `date` in the front
matter is enough; the ledger picks up the rest, groups by year, and orders newest
first. Write `content/posts/<name>.ko.md` beside it for the Korean version — an
untranslated page is absent from the Korean navigation rather than duplicated.

**A project.** Two edits, and `tools/check.py` fails if you only make one:

1. `content/projects/<name>.md` — the page. Copy the schema from an existing one
   and keep **every** key: an omitted key is a build error, not a default. `tier`
   is `"landing"` (hero, facts, features, a terminal session, a call to action) or
   `"brief"` (hero and prose). There is no middle rung on purpose.
2. `content/projects/_index.md` — the catalogue entry, under a `[[extra.group]]`.
   Listings only carry title, description, url, weight and date, so the language
   badge and the links have to live here.

Inline tables must fit on one line — TOML 1.0 does not let them wrap. Use
`[[extra.features]]` blocks when the text is too long for that.

**An image.** Put it in `static/images/projects/` and set `logo` on the project.
Until then the hero and the card render the project's name as the artwork, at the
same size the image will take, so nothing moves when you add one.

## Deploying

Push to `main`. The workflow checks integrity, builds, builds a second time and
diffs the two, then deploys. A build that is not reproducible does not ship.

The domain is in `static/CNAME` and is copied to the output with its name intact,
so it survives every deploy without being set in the repository settings again.
