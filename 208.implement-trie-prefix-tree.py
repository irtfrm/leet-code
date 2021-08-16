#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
    def addChild(self, key, child):
        self.children[key] = child

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = Tree(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.tree
        for ch in word:
            if not ch in node.children:
                node.addChild(ch, Tree(None))
            node = node.children[ch]
        node.val = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.tree
        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return node.val != None

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.tree
        for ch in prefix:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return node.val != None or len(node.children) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

