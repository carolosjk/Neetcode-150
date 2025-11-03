from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1

        return -1






if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,2,4,6,8],4))
    print(solution.search([-1,0,2,4,6,8],3))
    print(solution.search([-1,0,2,4,6,8,10,12,13,14,15,16,22,27,29,42,324,456,500],29))