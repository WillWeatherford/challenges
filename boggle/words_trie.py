"""Store all english words in a JSON Trie data structure."""
from __future__ import unicode_literals, division
from string import ascii_lowercase
import json

LOWERCASE = set(ascii_lowercase)
TERM_CHAR = '$'
UNIX_WORDS = '/usr/share/dict/american-english'
JSON_TRIE_WORDS = 'words.json'


class Trie(object):
    """Nested dictionaries to store every word in English."""

    def __init__(self, filename=None):
        """Initialize Trie from saved json file."""
        if filename is not None:
            with open(filename) as words_file:
                self._dict = json.load(words_file)
        else:
            self._dict = {}

    def is_valid_word(self, word):
        """Return boolean of whether this word is acceptable."""
        return set(word).issubset(LOWERCASE)

    def load_words(self, from_filename):
        """Load words from a linear file and save in a Trie structure file."""
        with open(from_filename, 'r') as from_file:
            for line in from_file:
                try:
                    self.insert(line.strip())
                except ValueError:
                    pass

    def save_words(self, to_filename):
        """Save words in Trie structure in json file."""
        with open(to_filename, 'w') as to_file:
            json.dump(self._dict, to_file)

    def insert(self, word):
        """Insert word into Trie."""
        if not self.is_valid_word(word):
            raise ValueError('Invalid word inserted: {}'.format(word))
        word += TERM_CHAR
        current_dict = self._dict
        for char in word:
            current_dict = current_dict.setdefault(char, {})

    def contains(self, word):
        """Return if word is in Trie."""
        current_dict = self._dict
        for char in word:
            try:
                current_dict = current_dict[char]
            except KeyError:
                return False
        return '$' in current_dict


if __name__ == '__main__':
    trie = Trie()
    trie.load_words(UNIX_WORDS)
    trie.save_words(JSON_TRIE_WORDS)
