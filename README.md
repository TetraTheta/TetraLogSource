# TetraLogSource

This is the source of my blog, [TetraLog](https://tetralog.onrender.com/), built with [Hugo](https://gohugo.io/) and the [HB Card Theme](https://github.com/hbstack/theme-cards).

## Requirements

* Hugo ≥ 0.145.0
* Node.js ≥ 22<br>
  (or) Bun ≥ 1.2.10 (Any version that is compatible with Node.js 22)
* Python ≥ 3.13

I use mixed environment(Node.js + Python) because I want to focus more on writing article, rather than spending time solving various problems in Javascript.

After cloning, run these commands in order:
```bash
# 1. Setup Node dependencies
npm ci
# (or) bun install --frozen-lockfile
# 2. Setup Python dependencies
python -m venv .venv
# 3. Activate Python virtual environment (Windows)
# for Linux: source .venv/bin/activate
call .venv\Scripts\activate.bat
# 4. Install Python dependencies in virtual environment
pip install -r requirements.txt
```

NPM script will run Python.

## Note

This is a note for myself for later use.

### Theme Overrides

For various reasons, I've overridden the files of Hugo and HB Card Theme. Here is a list of files that I've overridden and their original sources.

<pre><code>layouts
│ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/_default/rss.xml">rss.xml</a>
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
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/shortcodes/x.html">x.html</a>
  │ <a target="_blank" href="https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/shortcodes/x_simple.html">x.html</a>
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

* Very slow push speed<br>
  I tried to push repository to other machine in private network. Its uploading speed was ~250KB/s which is very unbearable. I couldn't find any way to speed up the uploading speed.

### Website Host Comparison

#### GitHub Pages

* Pros
  * Free of Charge<br>
    GitHub Pages is free unless the website is heavily used. This is OK for my blog.
  * Very Fast Response Time<br>
    Since GitHub Pages is on CDN, which ensures the fastest response time.
  * Very Big Bandwidth<br>
    I don't know about how much GitHub Pages allows, but it is big enough.
* Cons
  * Total Site Size Limit<br>
    GitHub Pages limits the total website size to 1 GB. My blog exceeds the limit (>= 2 GB).<br>
    My blog is still built and uploaded, but GitHub might stop my blog from being built someday.

#### Render

[Render](https://render.com/) allows me to host a static website.

* Pros
  * Free of Charge<br>
    If the website is static ― which Hugo produces ―, it doesn't cost for hosting the website.
  * Very Fast Response Time<br>
    Render hosts websites on CDN, which ensures the fastest response time.
* Cons
  * Limited build time<br>
    I can only use 500 minutes ― less than 1 day (1,440 minutes) ― per month for building sites in the free tier. It takes 10 minutes to build my blog, so I can only do 50 builds per month.
