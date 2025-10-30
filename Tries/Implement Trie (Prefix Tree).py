def getLetterIndex(letter: chr):
    return ord(letter)-ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str):
        if len(word) == 0:
            self.is_end = True
        else:
            li = getLetterIndex(word[0])
            if not self.children[li]:
                self.children[li] = TrieNode()
            self.children[li].insert(word[1:])

    def search(self, word: str, isWord: bool = True) -> bool:
        if len(word) == 0:
            return True if (self.is_end or not isWord) else False
        else:
            li = getLetterIndex(word[0])
            if not self.children[li]:
                return False
            return self.children[li].search(word[1:],isWord)


class PrefixTree:
   
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        self.root.insert(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)
    
    def startsWith(self, word: str) -> bool:
        return self.root.search(word, False)


if __name__ == "__main__":
    trie = PrefixTree()
    trie.insert("test")
    trie.insert("tester")
    trie.insert("word")
    print(trie.search("word"))
    print(trie.search("test"))
    print(trie.search("teste"))
    print(trie.search("tester"))
    print("---- starts with ----")
    print(trie.startsWith("tester"))
    print(trie.startsWith("ter"))
    print(trie.startsWith("wo"))