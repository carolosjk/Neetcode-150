from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring = 0
        l = 0
        charsFound = {}
        
        for r in range(len(s)):
            if s[r] in charsFound:
                l = max(charsFound[s[r]]+1,l)
            
            charsFound[s[r]] = r
            maxSubstring = max(maxSubstring,r-l+1)

        
        return maxSubstring


# l = 0, r = 0, c = z, cf = {"z":0}
# l = 0, r = 1, c = x, cf = {"z":0,"x":1}
# l = 0, r = 2, c = y, cf = {"z":0,"x":1,"y":2}
# l = 2, r = 3, c = x, cf = {"z":0,"x":3,"y":2}
# l = 2, r = 4, c = z, cf = {"z":4,"x":3,"y":2}




if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("zxyzxyz"))
    print(solution.lengthOfLongestSubstring("zxyxzyz"))
    print(solution.lengthOfLongestSubstring("xxxx"))