from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        maxFrequency = 0
        maxLength = 0
        l = 0

        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r],0) + 1
            if charCount[s[r]] > maxFrequency:
                maxFrequency = charCount[s[r]]
            
            while maxFrequency+k < r-l+1:
                charCount[s[l]] = charCount[s[l]] - 1
                l += 1
            maxLength = max(maxFrequency,r-l+1)

        return maxLength



# XYYX -> count = {"X":1}
# XYYX -> count = {"X":1, "Y":1}
# XYYX -> count = {"X":1, "Y":2}
# XYYX -> count = {"X":2, "Y":2}

if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement("XYYX", 2))
    print(solution.characterReplacement("AAABABB", 1))
