# TetraLogSource

This is the source of my blog, [TetraLog](https://tetralog.onrender.com/), built with [Hugo](https://gohugo.io/) and the [HB Card Theme](https://github.com/hbstack/theme-cards).

## Requirements

* Hugo ≥ 0.145.0
* Bun ≥ 1.2.10

After cloning, run this command:
```bash
bun install
```

Check out `package.json` for scripts that can be used with `bun run <script name>`.

## Note

This is a note for myself for later use. Some are separated into [NOTE](NOTE.md).

### Theme Overrides

For various reasons, I've overridden the files of Hugo and HB Card Theme. Here is a list of files that I've overridden and their original sources.

<details>
<summary>Override List</summary>
<pre><code>layouts
│ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/rss.xml">rss.xml</a>
├─partials
│ │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_partials/opengraph.html">opengraph.html</a> (Summary Fix)
│ │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_partials/schema.html">schema.html</a> (Summary Fix)
│ │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_partials/twitter_cards.html">twitter_cards.html</a> (Summary Fix)
│ ├─base
│ │   <a target="_blank" href="https://github.com/hugomods/base/blob/main/layouts/partials/base/title.html">title.html</a> (Custom Title Style)
│ ├─hb/modules
│ │ ├─blog/post
│ │ │   <a target="_blank" href="https://github.com/hbstack/blog/blob/main/layouts/partials/hb/modules/blog/post/summary.html">summary.html</a> (Summary Fix)
│ │ ├─breadcrumb
│ │ │   <a target="_blank" href="https://github.com/hbstack/breadcrumb/blob/main/layouts/partials/hb/modules/breadcrumb/index.html">index.html</a> (Hide 'Blog' from Breadcrumb)
│ │ └─footer
│ │     <a target="_blank" href="https://github.com/hbstack/footer/blob/main/layouts/partials/hb/modules/footer/powered-by.html">powered-by.html</a> (Custom Footer Text)
│ └─seo/modules
│   ├─base
│   │   <a target="_blank" href="https://github.com/hugomods/seo/blob/main/modules/base/layouts/partials/seo/modules/base/index.html">index.html</a> (Summary Fix)
│   ├─favicons
│   │   <a target="_blank" href="https://github.com/hugomods/seo/blob/main/modules/favicons/layouts/partials/seo/modules/favicons/index.html">index.html</a> (Remove 'mask-icon.svg')
│   ├─open-graph
│   │   <a target="_blank" href="https://github.com/hugomods/seo/blob/main/modules/open-graph/layouts/partials/seo/modules/open-graph/index.html">index.html</a> (Summary Fix)
│   ├─schema
│   │   <a target="_blank" href="https://github.com/hugomods/seo/blob/main/modules/schema/layouts/partials/seo/modules/schema/index.html">index.html</a> (Summary Fix)
│   └─twitter-cards
│       <a target="_blank" href="https://github.com/hugomods/seo/blob/main/modules/twitter-cards/layouts/partials/seo/modules/twitter-cards/index.html">index.html</a> (Summary Fix)
└─shortcodes
  │ <a target="_blank" href="https://github.com/hugomods/bootstrap/blob/main/layouts/partials/bootstrap/collapse.html">collapse.html</a>
  │ imgref.html
  │ <a target="_blank" href="https://github.com/hbstack/shortcodes/blob/main/layouts/shortcodes/spoiler-tag.html">spoiler.html</a>
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_shortcodes/x.html">x.html</a>
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_shortcodes/x_simple.html">x_simple.html</a>
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_shortcodes/youtube.html"></a>youtube.html</a>
  └─gallery
      image.html
      video.html
</code></pre>
</details>

### Useful commands

Here are some commands that I don't want to put in `package.json`.

<details>
<summary>Sort <code>package.json</code></summary>
<pre><code>bun x sort-package-json package.json</code></pre>
</details>

<details>
<summary>See dependency graph</summary>
Bun doesn't have <code>ls</code> feature yet.
<pre><code>npm ls --all</code></pre>
</details>

<details>
<summary>Remove unnecessary dependencies</summary>
Bun doesn't have <code>prune</code> feature yet.
<pre><code>npm prune
rm package-lock.json
rm bun.lock
rm -r node_modules
bun install</code></pre>
</details>
