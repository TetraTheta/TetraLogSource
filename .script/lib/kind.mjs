import as from 'ansi-styles';

export class Kind {
  /**
   * Create new Kind object
   * @param {string} name Name of Kind
   * @param {Array} alias Aliases of Kind
   * @param {string} kind Kind name to be used with Hugo command
   * @param {string} path Path of new article
   */
  constructor(name, alias, kind, path) {
    if (typeof name !== 'string') { throw new Error('Name must be a string') }
    if (!Array.isArray(alias) || !alias.every(a => typeof a === 'string')) { throw new Error('Alias must be an array of strings') }
    if (typeof kind !== 'string') { throw new Error('Kind must be a string') }
    if (typeof path !== 'string') { throw new Error('Path must be a string') }
    this.name = name
    this.alias = alias
    this.kind = kind
    this.path = path
  }
}

export class KindList {
  constructor() { this.kinds = [] }
  add(newKind) {
    if (newKind instanceof Kind) { this.kinds.push(newKind) }
    else { throw new Error('Only instance of Kind is accepted.') }
  }
  get(needle) {
    for (let kind of this.kinds) {
      if (kind.alias.includes(needle)) {
        return kind
      }
    }
    return null
  }
  show() {
    let result = ''
    for (let kind of this.kinds) {
      result += `${as.green.open}${kind.name}${as.green.close}: ${kind.alias.join(', ')}\n`
    }
    return result
  }
}

export default { Kind, KindList }
