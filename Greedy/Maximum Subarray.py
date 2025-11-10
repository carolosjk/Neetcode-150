import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_sum = -math.inf
        curr_sum = 0
        i = 0

        while i < len(nums):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum,curr_sum)
            i +=1
        return max_sum
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([2,-3,4,-2,2,1,-1,4]))
    print(sol.maxSubArray([-1]))
            
            