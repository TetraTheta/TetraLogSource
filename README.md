# TetraLogSource

This is the source of my blog, [TetraLog](https://tetralog.haipa.xyz/), built with [Hugo](https://gohugo.io/) and the [HB Card Theme](https://github.com/hbstack/theme-cards).

## Note

This is a note for myself for later use.

### Theme Overrides

For various reasons, I've overridden the Hugo and HB Card Themes' files. Here is a list of files that I've overridden and their original sources.

<pre><code>layouts
├─partials
│ ├─base
│ │   <a target="_blank" href="https://github.com/hugomods/base/blob/main/layouts/partials/base/title.html">title.html</a>
│ └─hb/modules
│   ├─breadcrumb
│   │   <a target="_blank" href="https://github.com/hbstack/breadcrumb/blob/main/layouts/partials/hb/modules/breadcrumb/index.html">index.html</a>
│   └─footer
│       <a target="_blank" href="https://github.com/hbstack/footer/blob/main/layouts/partials/hb/modules/footer/powered-by.html">powered-by.html</a>
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
