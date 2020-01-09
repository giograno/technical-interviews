import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.terminating = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def get_index(self, character):
        return ord(character) - ord('a')

    def addWord(self, word):
        start = self.root

        for ch in word:
            index = self.get_index(ch)

            if index not in start.children:
                start.children[index] = TrieNode()
            start = start.children.get(index)
        start.terminating = True

    def search(self, word):

        start = self.root
        self.res = False
        self.dfs_search(start, word)
        return self.res

    def dfs_search(self, root, word):
        for ch in word:
            if ch == '.':
                for children in root.children:
                    self.dfs_search(root.children[children], word[1:])
            else:
                index = self.get_index(ch)
                if index in root.children:
                    if len(word) == 1 and root.children[index].terminating:
                        self.res = True
                    self.dfs_search(root.children[index], word[1:])
                return
        return


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.addWord(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)


import unittest

class TestDictionary(unittest.TestCase):

    def test_solution(self):
        d = WordDictionary()
        d.addWord('hello')
        print('DONE search')
        ans = d.search('hello')
        self.assertTrue(ans)

    def test_missing(self):
        d = WordDictionary()
        d.addWord('hello')
        ans = d.search('hpllo')
        self.assertFalse(ans)

    def test_leetcode(self):
        d = WordDictionary()
        d.addWord('bad')
        d.addWord('mad')
        d.addWord('dad')
        self.assertTrue(d.search('bad'))
        self.assertFalse(d.search('pad'))

    def test_dot(self):
        d = WordDictionary()
        d.addWord('bad')
        d.addWord('mad')
        d.addWord('dad')
        self.assertTrue(d.search('.ad'))
