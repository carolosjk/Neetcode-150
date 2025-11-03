from typing import List
import heapq

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for n in nums:
            subsets += [a + [n] for a in subsets]

        return subsets

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1,2,3,4]))
    print(sol.subsets([]))
    print(sol.subsets([1,2]))
    print(sol.subsets([1]))