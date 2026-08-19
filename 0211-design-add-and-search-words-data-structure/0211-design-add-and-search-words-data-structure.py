class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end

            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if c not in node.children:
                return False
            return dfs(node.children[c], i + 1)

        return dfs(self.root, 0)