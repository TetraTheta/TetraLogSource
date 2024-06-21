#!/usr/bin/env node

import as from 'ansi-styles'
import { exec } from 'child_process'
import { existsSync, mkdirSync, readdir } from 'fs'
import { join, normalize } from 'path'
import { info, error, projectRoot } from './lib/common.mjs'
import { Kind, KindList } from './lib/kind.mjs'

const Kinds = new KindList()
Kinds.add(new Kind('blue-archive', ['ba', 'blue-archive', 'bluearchive'], 'blue-archive', 'b/game/blue-archive')) // 블루 아카이브
Kinds.add(new Kind('chit-chat', ['cc', 'chat', 'chit-chat', 'chitchat'], 'chit-chat', 'b/chit-chat')) // 잡담
Kinds.add(new Kind('default', ['default'], 'default', 'b')) // 기본 (미사용)
Kinds.add(new Kind('game-misc', ['game-misc', 'gm'], 'game-misc', 'b/game/misc')) // 게임 기타
Kinds.add(new Kind('genshin-archon', ['ga', 'gaq', 'genshin-archon', 'genshin-archon-quest', 'genshin-archon-quests'], 'genshin-impact', 'b/game/genshin-impact/archon')) // 원신 마신 임무
Kinds.add(new Kind('genshin-event', ['ge', 'genshin-event', 'genshin-event-quest', 'genshin-event-quests', 'geq'], 'genshin-impact', 'b/game/genshin-impact/event')) // 원신 이벤트 임무
Kinds.add(new Kind('genshin-misc', ['genshin-misc'], 'genshin-impact', 'b/game/genshin-impact/misc')) // 원신 기타
Kinds.add(new Kind('genshin-story', ['genshin-story', 'genshin-story-quest', 'genshin-story-quests', 'gs', 'gsq'], 'genshin-impact', 'b/game/genshin-impact/story')) // 원신 전설 임무
Kinds.add(new Kind('genshin-world', ['genshin-world', 'genshin-world-quest', 'genshin-world-quests', 'gw', 'gwq'], 'genshin-impact', 'b/game/genshin-impact/world')) // 원신 월드 임무
Kinds.add(new Kind('honkai-star-rail', ['honkai', 'honkai-star-rail', 'hsr', 'sr'], 'honkai-star-rail', 'b/game/honkai-star-rail')) // 붕괴: 스타레일
Kinds.add(new Kind('minecraft', ['mc', 'minecraft'], 'minecraft', 'b/game/minecraft')) // 마인크래프트
Kinds.add(new Kind('music', ['music'], 'music', 'b/chit-chat/music')) // 음악
Kinds.add(new Kind('the-division', ['d', 'division', 'td', 'td2', 'the-division'], 'the-division', 'b/game/the-division')) // 더 디비전
Kinds.add(new Kind('tower-of-fantasy', ['tf', 'tof', 'tower-of-fantasy'], 'tower-of-fantasy', 'b/game/tower-of-fantasy')) // 타워 오브 판타지
Kinds.add(new Kind('wuthering-waves-companion', ['wc', 'wcq', 'wuthering-companion', 'wuthering-waves-companion', 'wuthering-waves-companion-quest', 'wuthering-waves-companion-quests', 'ww-companion', 'ww-companion-quest', 'ww-companion-quests', 'wwc', 'wwcq'], 'wuthering-waves', 'b/game/wuthering-waves/companion')) // 명조 얽힌 별 임무
Kinds.add(new Kind('wuthering-waves-exploration', ['we', 'weq', 'wuthering-exploration', 'wuthering-waves-exploration', 'wuthering-waves-exploration-quest', 'wuthering-waves-exploration-quests', 'ww-exploration', 'ww-exploration-quest', 'ww-exploration-quests', 'wwe', 'wweq'], 'wuthering-waves', 'b/game/wuthering-waves/exploration')) // 명조 위험한 임무
Kinds.add(new Kind('wuthering-waves-main', ['wm', 'wmq', 'wuthering-main', 'wuthering-waves-main', 'wuthering-waves-main-quest', 'wuthering-waves-main-quests', 'ww-main', 'ww-main-quest', 'ww-main-quests', 'wwm', 'wwmq'], 'wuthering-waves', 'b/game/wuthering-waves/main')) // 명조 조수 임무
Kinds.add(new Kind('wuthering-waves-misc', ['wuthering-misc', 'wuthering-waves-misc', 'ww-misc'], 'wuthering-waves', 'b/game/wuthering-waves/misc')) // 명조 기타

const args = process.argv.splice(2)
const _kindIndex = args.indexOf('--kind')
if (_kindIndex === -1 || _kindIndex === args.length - 1) {
  error('Invalid syntax')
  showHelp()
  process.exit(1)
}

const kind = Kinds.get(args[_kindIndex + 1])
const name = sanitizeString([...args.slice(0, _kindIndex), ...args.slice(_kindIndex + 2)].join(' '))

if (kind === null) {
  error('Invalid kind argument')
  showHelp()
  process.exit(1)
}

const contentPath = join(projectRoot(), 'content', kind.path)

info(`${as.yellow.open}-------- Input Information --------${as.yellow.close}`)
info(`Kind: ${kind.kind}`)
info(`Parent Path: ${contentPath}`)
info(`Name: ${name}`)
info(`${as.yellow.open}-----------------------------------${as.yellow.close}`)

// Create content path if necessary
if (!existsSync(contentPath)) {
  info(`Following path will be created: ${as.yellow.open}${contentPath}${as.yellow.close}`)
  mkdirSync(contentPath, { recursive: true })
}

readdir(contentPath, (err, files) => {
  if (err) {
    error(`Failed to read directory: ${as.yellow.open}${contentPath}${as.yellow.close}`)
    process.exit(1)
  }
  // Get next prefix number
  let nextNum = 1
  while (files.some((dir) => dir.startsWith(`${nextNum.toString().padStart(3, '0')}-`))) nextNum++
  // Get new path name
  const newDirName = `${nextNum.toString().padStart(3, '0')}-${name}`
  const finalPath = normalize(`${contentPath}/${newDirName}/index.md`)
  // Run hugo command
  process.chdir(projectRoot())
  const cmd = `hugo new content -k ${kind.kind} ${finalPath}`
  info(`Following post will be created: ${as.yellow.open}${newDirName}${as.yellow.close}`)
  exec(cmd, { stdio: 'inherit' }, (err, stdout, stderr) => {
    info(cmd, 'COMMAND', 'cyan')
    if (err) {
      error(err.message)
      return
    }
    if (stderr) {
      error(`Stderr: ${stderr}`)
      return
    }
    if (stdout) {
      if (stdout.startsWith('Error: ')) {
        error(stdout)
      } else {
        info(`Output: ${stdout}`)
      }
    }
  })
})

function sanitizeString(input) {
  // Strip korean characters
  let sanitized = input.replace(/[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/g, '')
  // Replace other characters
  sanitized = sanitized.replace(/`/g, '\'')
  // Replace space to single '-'
  sanitized = sanitized.replace(/\s+/g, '-')
  // Replace accented characters (this must be done in last)
  sanitized = sanitized.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase()

  return sanitized
}

function showHelp() {
  info('new.mjs --kind KIND TITLE', 'USAGE', 'red')
  info('new.mjs TITLE --kind KIND', 'USAGE', 'red')
  info('Valid kind and its alias: \n' + Kinds.show(), 'USAGE', 'red')
}
