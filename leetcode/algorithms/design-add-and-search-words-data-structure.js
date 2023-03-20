class WordDictionary {
	static EOW = Symbol('EndOfWord')
	static WILDCARD = '.'

	words = {}

	addWord(word) {
		let current = this.words

		for (const char of word) {
			if (current[char] === undefined) {
				current[char] = {}
			}

			current = current[char]
		}

		current[WordDictionary.EOW] = true
	}

	search(word, startNode = this.words) {
		let current = startNode

		for (const [idx, char] of [...word].entries()) {
			if (char === WordDictionary.WILDCARD) {
				for (const node of Object.values(current)) {
					if (this.search(word.slice(idx+1), node)) {
						return true
					}
				}

				return false
			} else if (current[char]) {
				current = current[char]
			} else {
				return false
			}
		}

		return current[WordDictionary.EOW] === true
	}
}
