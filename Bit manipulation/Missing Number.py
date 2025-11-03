from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0

        for n in nums:
            sum += n        

        n = len(nums)
        return int( ( (n*(n+1))/2) - sum)

# 
# 
# 
# 
# 
# 

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber([1,2,3]))
    print(solution.missingNumber([0,2]))
    