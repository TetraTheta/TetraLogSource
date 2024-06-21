#!/usr/bin/env node

import { mkdtempSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { rimrafSync } from 'rimraf'
import { deslash } from './deslash.mjs'
import { projectRoot, run } from './lib/common.mjs'
import env from './lib/environment.mjs'

const args = process.argv.slice(2)
const localIndex = args.indexOf('--local')
if (localIndex !== -1) {
  const localValue = args[localIndex + 1]
  let isLocal = false
  if (localValue !== '0' && localValue !== 'false') {
    isLocal = true
  }
  publish(isLocal)
}

function publish(isLocal) {
  const myRoot = isLocal ? projectRoot() : mkdtempSync(join(tmpdir(), 'hugo-build-'))
  process.chdir(myRoot)

  if (!isLocal) {
    // !local: Create temp directory
    info('Creating temporary directory...') // tempdir is already created
    info(myRoot, 'TEMP-DIR', 'yellow')
    // !local: Clone repository
    info('Fetching latest commit to temporary directory...')
    run(`git clone --progress --depth 1 ${env.GIT_PULL_URL} ${myRoot}`)
  }

  // Build site (locally)
  info('Building site...')
  run('npm ci && npm run clean && npm run build')

  // Deslash files
  deslash('./public')

  // Sync files with RSync
  run(`rsync -vrmzh --progress --del --force -e "ssh -o StrictHostKeyChecking=no -i ${env.PUBLISH_SSH_KEY}" ./public/ ${env.PUBLISH_USER_IP}:${env.PUBLISH_DIR}`)

  // Clean directories
  rimrafSync('public')
  rimrafSync('resources')

  // !local: Go parent directory and delete temp directory
  if (!isLocal) {
    process.chdir('..')
    rimrafSync(myRoot)
  }

  info('done')
}
