from typing import List

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []

        pair = {"(":")", "{":"}", "[":"]"}
        
        for c in s:
            if c in ("(","{","["):
                stack.append(c)
            else:
                if len(stack) == 0 or pair[stack.pop()] != c:
                    return False
        
        return len(stack) == 0


    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("[]"))
    print(solution.isValid("{[]}"))
    print(solution.isValid("([(]})"))

