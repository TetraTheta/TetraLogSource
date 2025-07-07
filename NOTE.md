# Note

This is a note for myself for later use.

- [Menu Image Icon Format](#menu-image-icon-format)
  * [Making a Rounded Square Image](#making-a-rounded-square-image)
- [Storing Image Files](#storing-image-files)
  * [Git LFS](#git-lfs)
  * [DVC with Google Drive](#dvc-with-google-drive)
- [Website Host Comparison](#website-host-comparison)
  * [GitHub Pages](#github-pages)
  * [Render](#render)

***

## Menu Image Icon Format

I can use a PNG image as a menu icon instead of an SVG image. But the PNG image must follow these rules:

1. Image Size
   * Main Menu: 16x16
   * Sub Menu: 32x32
2. Image Round Radius
   * 256x256: 55px
   * 400x400: 85px
   * 512x512: 109px

### Making a Rounded Square Image

To make rounded square image in Photoshop, follow this.

1. Put a rounded rectangle layer below the image layer
2. Right-click the image layer and set it as a clipping mask

## Storing Image Files

My blog contains a lot of image files.
As in 25.07.07, this is the statistics of those image files.

* Count: ＞ 31,000
* Total Size: ＞ 2.25 GiB 

Putting these image files in Git repository will increase pull time. I need a way to store these image files in somewhere else.

### Git LFS

I must not use Git LFS, especially the Git LFS provided by GitHub.

* Very limited quota<br>
  GitHub provides 1 GiB free storage and 1 GiB bandwidth per month.<br>
  None of these can satisfy my situation.
* Very slow push speed<br>
  When I tried to push file to Git LFS server on local network, the push speed was ~250 KiB/s.<br>
  I can't bear with this speed, and I couldn't find out how to speed up the push speed.

### DVC with Google Drive

I also tried [DVC](https://dvc.org/) with Google Drive.
That sounded nice, but Google was the ball and chain.

* Very limited quota<br>
  Even though I used Service Account, initial push reached quota very quickly.<br>
  Since I must use DVC for uploading those 'cache' to Google Drive, I can't proceed.

## Website Host Comparison

I need to find out which host is the best choice.

### GitHub Pages

#### Pros

* Free of Charge<br>
  GitHub Pages is free unless the website is heavily used. This is OK for my blog.
* Very Fast Response Time<br>
  Since GitHub Pages is on CDN, which ensures the fastest response time.
* Very Big Bandwidth<br>
  I don't know about how much GitHub Pages allows, but it is big enough.

#### Cons

* Total Site Size Limit<br>
  GitHub Pages limits the total website size to 1 GB. My blog exceeds the limit (≥ 2 GB).<br>
  My blog is still built and uploaded, but GitHub might stop my blog from being built someday.
* No Git LFS Support<br>
  GitHub Pages doesn't support pulling data from Git LFS.

### Render

[Render](https://render.com/) allows me to host a static website.

#### Pros

* Free of Charge<br>
  If the website is static ― which Hugo produces ―, it doesn't cost for hosting the website.
* Very Fast Response Time<br>
  Render hosts websites on CDN, which ensures the fastest response time.

#### Cons

* Limited build time<br>
  I can only use 500 minutes ― less than 1 day (1,440 minutes) ― per month for building sites in the free tier.<br>
  It takes 10 minutes to build my blog, so I can only do 50 builds per month.
