class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []

        def dfs(s: str, o: int, c: int):
            if o == c == n:
                res.append(s)
                return

            if o < n:
                s += "("
                dfs(s, o+1, c)
                s = s[:-1]

            if o > c:
                s += ")"
                dfs(s, o, c+1)
            
        dfs("",0,0)

        return res
