# TetraLogSource

This is the source of my blog, [TetraLog](https://tetralog.haipa.xyz/), built with [Hugo](https://gohugo.io/) and the [HB Card Theme](https://github.com/hbstack/theme-cards).

## Requirements

* Hugo >= 0.127.0
* Node.js >= 20
* Python >= 3.12

I use mixed environment(Node.js + Python) because I want to focus more on writing article, rather than spending time solving various problems in Javascript.

After cloning, run these commands in order:
```bash
# Setup Node dependencies
npm ci
# Setup Python dependencies
python -m venv .venv
# Activate Python virtual environment (Windows)
# for Linux: source .venv/bin/activate
call .venv\Scripts\activate.bat
# Install Python dependencies in virtual environment
pip install -r requirements.txt
```

NPM script will run Python.

## Note

This is a note for myself for later use.

### Theme Overrides

For various reasons, I've overridden the files of Hugo and HB Card Theme. Here is a list of files that I've overridden and their original sources.

<pre><code>layouts
├─partials
│ │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/opengraph.html">opengraph.html</a> (Summary Fix)
│ │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/schema.html">schema.html</a> (Summary Fix)
│ │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/twitter_cards.html">twitter_cards.html</a> (Summary Fix)
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
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/shortcodes/twitter.html">twitter.html</a>
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/shortcodes/twitter_simple.html">twitter_simple.html</a>
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/shortcodes/youtube.html"></a>youtube.html</a>
  └─gallery
      image.html
      video.html
</code></pre>

### Image Icon Format

I can use a PNG image as a menu icon instead of an SVG image, but it must follow these rules:

1. Image Size: 16x16 (32x32 for sub-menu)
2. Image Round Radius:
  * 256x256: 55px
  * 400x400: 85px
  * 512x512: 109px

#### How to make a rounded square image in Photoshop

1. Put a rounded rectangle layer below the image layer
2. Right-click the image layer and set it as a clipping mask

### No Git LFS

I tried Git LFS to see if it is really efficient. Now I despise Git LFS.

* Very slow push speed  
  I tried to push repository to other machine in private network. Its uploading speed was ~250KB/s which is very unbearable. I couldn't find any way to speed up the uploading speed.
