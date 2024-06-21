import as from 'ansi-styles';
import { existsSync } from 'node:fs';
import { dirname, join, normalize } from 'node:path';

/**
 * Show error message with 'ERROR' prefix
 * @param {*} message 
 */
export function error(message) {
  console.error(`${as.red.open}ERROR${as.red.close} ${message}`)
}
/**
 * Show info message with 'INFO' prefix
 * @param {*} message 
 * @param {string} title
 * @param {string} color
 */
export function info(message, title = 'INFO', color = 'green') {
  switch (color) {
    case 'cyan':
      console.log(`${as.cyan.open}${title}${as.cyan.close} ${message}`)
      break
    case 'green':
      console.log(`${as.green.open}${title}${as.green.close} ${message}`)
      break
    case 'red':
      console.log(`${as.red.open}${title}${as.red.close} ${message}`)
      break
    case 'yellow':
      console.log(`${as.yellow.open}${title}${as.yellow.close} ${message}`)
      break
    default:
      console.log(`${as.green.open}${title}${as.green.close} ${message}`)
  }
}
/**
 * @returns Project root where 'package.json' is located
 */
export function projectRoot() {
  let currentDir = normalize(import.meta.dirname)
  while (true) {
    const jsonPath = join(currentDir, 'package.json')
    if (existsSync(jsonPath)) return currentDir
    const parentDir = dirname(currentDir)
    if (parentDir === currentDir) throw new Error(`package.json not found in any parent directories: ${parentDir}`)
    currentDir = parentDir
  }
}
/**
 * Run command on local machine
 * @param {string} command 
 */
export function run(command) {
  const cmd = spawn(command, { stdio: 'inherit' })
  cmd.stdout.on('data', function (data) {
    console.log(data)
  })
  cmd.stderr.on('data', function (data) {
    console.error(`${as.red.open}${data}${as.red.close}`)
  })
}
/**
 * Run command from remote server
 * @param {string} command 
 */
export function runRemote(command) {
  const sshCommand = `"${SSH_PATH}" -o StrictHostKeyChecking=no -i ${PUBLISH_SSH_KEY} ${PUBLISH_USER}@${PUBLISH_IP} "${command}"`
  run(sshCommand)
}
/**
 * Pauses script execution for given time
 * 
 * Javascript runs async, but I need synced sleep
 * @param {number} time 
 */
export function sleep(time) {
  const wakeUpTime = Date.now() + time
  while (Date.now() < wakeUpTime) { }
}
