#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import deque

class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
    def addChild(self, key, child):
        self.children[key] = child

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = Tree(None)

    def addWord(self, word: str) -> None:
        node = self.tree
        for ch in word:
            if not ch in node.children:
                node.addChild(ch, Tree(None))
            node = node.children[ch]
        node.val = word

    def search(self, word: str) -> bool:
        return self.searchIn(self.tree, word)

    def searchIn(self, node: Tree, word):
        ch = word[0]
        if len(word) == 1:
            if ch == '.' and any([child.val != None for child in node.children.values()]):
                return True
            if ch in node.children and node.children[ch].val != None:
                return True
            return False
        if ch == '.':
            return any([self.searchIn(child, word[1:]) for child in node.children.values()])
        elif ch in node.children:
            return self.searchIn(node.children[ch], word[1:])
        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

