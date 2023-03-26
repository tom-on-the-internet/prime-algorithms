from __future__ import annotations
import string


class TrieNode:
    end_of_word: bool = False
    letters = {}


class Trie:
    root = TrieNode()

    def insert(self: Trie, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.letters:
                curr = curr.letters[char]
                continue

            node = TrieNode()
            curr.letters[char] = node
            curr = node

        curr.end_of_word = True

    def contains(self: Trie, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.letters:
                return False

            curr = curr.letters[char]

        return curr.end_of_word

    def starts_with(self: Trie, word: str) -> list[str]:
        curr = self.root
        letters = []
        words = []

        for char in word:
            if char not in curr.letters:
                return []
            letters.append(char)

        def recurse(node: TrieNode):
            for letter in node.letters:
                recurse(node.letters[letter])

        # starting now, we need to do a search
        # depth first so it's alphabetical
        print(string.ascii_lowercase)
        print(letters)


trie = Trie()

trie.insert("hello")
print(trie.contains("dog"))
print(trie.contains("hell"))
print(trie.contains("hello"))
print(trie.contains("hellos"))
print(trie.starts_with("hel"))
print(trie.starts_with("bel"))
