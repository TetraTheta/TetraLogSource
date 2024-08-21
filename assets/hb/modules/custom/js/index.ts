// This script will be compiled into the JS bundle automatically.
// Scroll to previous position when reloading
document.addEventListener('DOMContentLoaded', function() {
  const scrollPos = parseInt(sessionStorage.getItem('scrollPos'))
  const scrollUrl = sessionStorage.getItem('scrollUrl')
  if (scrollPos > 0 && scrollUrl == location.href) {
    window.scroll({top: scrollPos, left: 0, behavior: 'smooth'}) // 'instant'
  }
  sessionStorage.removeItem('scrollPos')
  sessionStorage.removeItem('scrollUrl')
})
window.addEventListener('beforeunload', function() {
  const scrollPos = window.scrollY > 0 ? window.scrollY : 0
  sessionStorage.setItem('scrollPos', scrollPos.toString())
  sessionStorage.setItem('scrollUrl', location.href)
})
// Add title to footnote link
document.addEventListener('DOMContentLoaded', function() {
  const tempTextArea = document.createElement('textarea')
  const fnRefs = document.querySelectorAll('.footnote-ref')
  fnRefs.forEach(function(ref) {
    const fnID = ref.getAttribute('href').substring(1).replace(/:/g, "\\:")
    let fnContent = document.querySelector('#' + fnID + ' p').innerHTML
    tempTextArea.innerHTML = fnContent
    fnContent = tempTextArea.value
    fnContent = fnContent.replace(/<[^>]+>/g, '').replace(/↩︎/g, '').trim()
    console.log(fnContent)
    ref.setAttribute('title', fnContent)
  })
})
