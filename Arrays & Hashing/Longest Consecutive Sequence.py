from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longset = 0

        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length +=1
                longset = max(length,longset)
        
        return longset

        
    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([2,20,4,10,3,4,5]))
    print(solution.longestConsecutive([0,3,2,5,4,6,1,1]))

