class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = set()

        def dfs(arr: list[int]) -> None:
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for i in nums:
                if i not in used:
                    used.add(i)
                    arr.append(i)
                    dfs(arr)
                    used.remove(i)
                    arr.pop()

        dfs([])

        return res