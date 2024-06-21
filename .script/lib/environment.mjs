function get(key, def = '') {
  return process.env[key] || def
}

const env = {
  GIT_PULL_URL: get('GIT_PULL_URL', get('GIT_PUSH_URL')),
  GIT_PUSH_URL: get('GIT_PUSH_URL'),
  PUBLISH_SSH_KEY: get('PUBLISH_SSH_KEY'),
  PUBLISH_USER_IP: get('PUBLISH_USER_IP', 'ubuntu@127.0.0.1'),
  PUBLISH_DIR: get('PUBLISH_DIR', '/var/www/html'),

  get(key) {
    return this[key]
  }
}

export default env
