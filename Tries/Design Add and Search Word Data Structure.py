

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            c = getCharIndex(c)
            if not cur.children[c]:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i,c in enumerate(word):
            c = getCharIndex(c)
            if c == 26: # c == "." wildcard character
                word_to_try = word
                for j in range(26):
                    word_to_try = word.replace(".",chr(ord("a")+j),1)
                    if self.search(word_to_try):
                        return True
                return False
            else:
                if not cur.children[c]:
                    return False
                cur = cur.children[c]
        return cur.is_end



def getCharIndex(char: chr) -> int:
    if char == ".":
        return 26
    else:
        return ord(char)-ord("a")
    

if __name__ == "__main__":
    trie = WordDictionary()
    trie.addWord("test")
    trie.addWord("day")
    trie.addWord("bay")
    trie.addWord("bday")
    print(trie.search("test"))
    print(trie.search("tes.."))
