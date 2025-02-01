// This script will be compiled into the JS bundle automatically.
// Scroll to previous position when reloading
document.addEventListener('DOMContentLoaded', function () {
  const scrollPos = parseInt(sessionStorage.getItem('scrollPos'))
  const scrollUrl = sessionStorage.getItem('scrollUrl')
  if (scrollPos > 0 && scrollUrl == location.href) {
    window.scroll({ top: scrollPos, left: 0, behavior: 'smooth' }) // 'instant'
  }
  sessionStorage.removeItem('scrollPos')
  sessionStorage.removeItem('scrollUrl')
})
window.addEventListener('beforeunload', function () {
  const scrollPos = window.scrollY > 0 ? window.scrollY : 0
  sessionStorage.setItem('scrollPos', scrollPos.toString())
  sessionStorage.setItem('scrollUrl', location.href)
})
// Add title to footnote link
document.addEventListener('DOMContentLoaded', function () {
  const tempTextArea = document.createElement('textarea')
  const fnRefs = document.querySelectorAll('.footnote-ref')
  fnRefs.forEach(function (ref) {
    const fnID = ref.getAttribute('href').substring(1).replace(/:/g, "\\:")
    let fnContent = document.querySelector('#' + fnID + ' p').innerHTML
    tempTextArea.innerHTML = fnContent
    fnContent = tempTextArea.value
    fnContent = fnContent.replace(/<[^>]+>/g, '').replace(/↩︎/g, '').trim()
    console.log(fnContent)
    ref.setAttribute('title', fnContent)
  })
})
// <link-preview> HTML Tag
// @ts-ignore
class LinkPreviewElem extends HTMLElement {
  static get observedAttributes() {
    return ['url']
  }

  constructor() {
    super()
    //this.attachShadow({ mode: 'open' })
  }

  attributeChangedCallback(name: string, _oldValue: string, newValue: string) {
    if (name == 'url') {
      this.fetchOpenGraphData(newValue)
    }
  }

  // @ts-ignore
  async fetchOpenGraphData(url: string): Promise<void> {
    const cachedData = localStorage.getItem(url)
    if (cachedData) {
      this.render(JSON.parse(cachedData), url)
      return
    }

    try {
      const response = await fetch(`https://open-graph-api-coral.vercel.app/api/opengraph?url=${encodeURIComponent(url)}`)
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      localStorage.setItem(url, JSON.stringify(data))
      this.render(data, url)
    } catch (e) {
      console.error('Fetch error: ', e)
    }
  }

  render(data: object, url: string) {
    const {title, desc, image} = data as { title?: string; desc?: string; image?: string }
    //this.shadowRoot.innerHTML = `
    this.innerHTML = `
    <figure class="link-preview">
      <a class="lp-link" href="${url}" target="_blank" rel="noopener">
        ${image ? `<div class="lp-image" style="background-image: url('${image}');">&nbsp;</div>` : ""}
        <div class="lp-text">
          <p class="lp-title">${title}</p>
          <p class="lp-desc">${desc}</p>
          <p class="lp-host">${new URL(url).host}</p>
        </div>
      </a>
    </figure>
    `
  }
}

window.customElements.define('link-preview', LinkPreviewElem)
