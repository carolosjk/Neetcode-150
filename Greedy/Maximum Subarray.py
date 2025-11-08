class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_index = 0
        max_sum = 0
        curr_index = 0
        curr_sum = 0
        i = 0

        while i < len(nums):
            
            