# Note

This is a note for myself for later use.

## Image Icon Format

I can use a PNG image as a menu icon instead of an SVG image, but it must follow these rules:

1. Image Size: 16x16 (32x32 for sub-menu)
2. Image Round Radius:
  * 256x256: 55px
  * 400x400: 85px
  * 512x512: 109px

### How to make a rounded square image in Photoshop

1. Put a rounded rectangle layer below the image layer
2. Right-click the image layer and set it as a clipping mask

## No Git LFS

I tried Git LFS to see if it is really efficient. Now I despise Git LFS.

* Very slow push speed<br>
  I tried to push repository to other machine in private network. Its uploading speed was ~250KB/s which is very unbearable. I couldn't find any way to speed up the uploading speed.

## Website Host Comparison

### GitHub Pages

<details>
<summary>GitHub Pages</summary>
<ul>
  <li>Pros
    <ul>
      <li>Free of Charge<br>GitHub Pages is free unless the website is heavily used. This is OK for my blog.</li>
      <li>Very Fast Response Time<br>Since GitHub Pages is on CDN, which ensures the fastest response time.</li>
      <li>Very Big Bandwidth<br>I don't know about how much GitHub Pages allows, but it is big enough.</li>
    </ul>
  </li>
  <li>Cons
    <ul>
      <li>Total Site Size Limit<br>GitHub Pages limits the total website size to 1 GB. My blog exceeds the limit (≥ 2 GB).<br>My blog is still built and uploaded, but GitHub might stop my blog from being built someday.</li>
    </ul>
  </li>
</ul>
</details>

### Render

[Render](https://render.com/) allows me to host a static website.

<details>
<summary>Render</summary>
<ul>
  <li>Pros
    <ul>
      <li>Free of Charge<br>If the website is static ― which Hugo produces ―, it doesn&#39;t cost for hosting the website.</li>
      <li>Very Fast Response Time<br>Render hosts websites on CDN, which ensures the fastest response time.</li>
    </ul>
  </li>
  <li>Cons
    <ul>
      <li>Limited build time<br>I can only use 500 minutes ― less than 1 day (1,440 minutes) ― per month for building sites in the free tier. It takes 10 minutes to build my blog, so I can only do 50 builds per month.</li>
    </ul>
  </li>
</ul>
</details>