

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie():
    def __init__(self):
        self.head = TrieNode()

    def add(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True



class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res = set()

        trie = Trie()

        for word in words:
            trie.add(word)

        rows = len(board)
        cols = len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]



        def dfs(r,c,node,word):
            if r < 0 or r > rows -1 or c < 0 or c > cols-1:
                return
            letter = board[r][c]
            if letter == "*" or not node or letter not in node.children:
                return
            
            word += letter
            board[r][c] = "*"
            node = node.children[letter]
            if node.is_end:
                res.add(word)

            for i,j in directions:
                if 0 <= r+i < rows and 0 <= c+j < cols:
                    if board[r+i][c+j] != "*":
                        dfs(r+i, c+j, node, word)

            board[r][c] = letter


        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,trie.head,"")
                
        print(res)
        return list(res)

if __name__ == "__main__":
    sol = Solution()
    sol.findWords(
        [
        ["a","b","c","d"],
        ["s","a","a","t"],
        ["a","c","k","e"],
        ["a","c","d","n"]
        ],
        ["bat","cat","back","backend","stack"]
    )

    sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
