from typing import List

class Solution:

    def calculateLoot(self, nums: List[int], current: int, cache: dict) -> int:
        if current >= len(nums):
            return 0
        
        if current in cache:
            return cache[current]

        cache[current] = nums[current] + max(self.calculateLoot(nums,current+2,cache), self.calculateLoot(nums,current+3,cache))
        return cache[current]

    def rob(self, nums: List[int]) -> int:
        cache = {}
        return max(self.calculateLoot(nums,0,cache), self.calculateLoot(nums,1,cache))


        

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1,1,3,3]))
    print(solution.rob([2,9,8,3,6]))
    print(solution.rob([1,3,5,7,9,11,13,15,17,19,2,4,6,8,10,12,14,16,18,20,21,23,25,27,29,31,33,35,37,39,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,99,97,95,93,91,89,87,85,83,81,79,77,75,73,71,69,67,65,63,61,59,57,55,53,51,49,47,45,43,41,39,37,35,33,31,29,27,25,23]))
