class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        arr = []
        nums.sort()

        def dfs(i: int) -> None:
            if i == len(nums):
                res.append(arr.copy())
                return

            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1)


        dfs(0)

        return res
