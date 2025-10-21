from typing import List
import re

class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())

        print(s)

        length = len(s)
        for i in range(length//2):
            if s[i] != s[length-i-1]: return False       

        return True

        
    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("Was it a car or a cat I saw?"))
    print(solution.isPalindrome("tab a cat"))

