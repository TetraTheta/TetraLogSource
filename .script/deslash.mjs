#!/usr/bin/env node

import minifyHtml from '@minify-html/node'
import { load } from 'cheerio'
import { glob } from 'glob'
import { minify } from 'minify-xml'
import { Buffer } from 'node:buffer'
import { readFileSync, stat, writeFileSync } from 'node:fs'
import { error, info } from './lib/common.mjs'

const minifyHtmlOption = {
  do_not_minify_doctype: true,
  ensure_spec_compliant_unquoted_attribute_values: true,
  keep_html_and_head_opening_tags: true,
  keep_spaces_between_attributes: true,
  minify_css: true,
  minify_js: true,
  remove_bangs: true,
  remove_processing_instructions: true
}

const args = process.argv.slice(2)
if (args.length === 0) {
  error('No path is provided')
  process.exit(1)
}

const inputPath = args[0]
stat(inputPath, (err, stats) => {
  if (err) {
    error(`Failed to get stats for path: ${inputPath}`)
    throw err
  }
  if (stats.isFile()) {
    deslash(inputPath)
  } else if (stats.isDirectory()) {
    const searchPattern = path.join(inputPath, '**/*.{html,htm,xml}')
    glob.glob(searchPattern, (err, files) => {
      if (err) throw err
      files.forEach(deslash)
    })
  }
})

export function deslash(f) {
  let content = readFileSync(f, 'utf8')
  info(f, 'DESLASH', 'yellow')
  if (f.endsWith('.html') || f.endsWith('.htm')) {
    // Remove slash
    const $h = load(content)
    $h('a').each(() => {
      // I don't understand why I can't use 'element'
      const htmlAttr = $h(this).attr('href')
      if (htmlAttr) $h(this).attr('href', removeTrailingSlash(htmlAttr))
    })
    $h('meta').each(() => {
      const htmlProperty = $h(this).attr('property')
      if (htmlProperty === 'og:url') {
        $h(this).attr('content', removeTrailingSlash(htmlProperty))
      }
    })
    content = $h.html()
    // Minify HTML using @minify-html/node
    const result = minifyHtml.minify(Buffer.from(content), minifyHtmlOption)
    writeFileSync(f, result)
  } else if (f.endsWith('.xml')) {
    // Remove slash
    const $x = load(content, { xml: true })
    $x('link, guid, loc').each(() => {
      const xmlLink = $x(this).text()
      $x(this).text(removeTrailingSlash(xmlLink))
    })
    content = $x.xml()
    // Minify XML using minify-xml
    try {
      const result = minify(content)
      writeFileSync(f, result)
    } catch (err) {
      error(`Failed to minimize XML: ${f}`)
      writeFileSync(f, content)
      throw err
    }
  }
}

function removeTrailingSlash(url) {
  if (url.length > 2 && url.endsWith('/')) return url.slice(0, -1)
  else return url
}
