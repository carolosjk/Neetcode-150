from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differences = {}

        for index, num in enumerate(nums):
            dif = target-num

            if num in differences:
                return [differences[num],index]

            differences[target-num] = index
        


if __name__ == "__main__":

    solution = Solution()
    print(solution.twoSum([1,2,3,4,5,6],7))
    print(solution.twoSum([5,7,9,12,3,6,2,1,4],8))
    print(solution.twoSum([2,3,4,5,],9))
    print(solution.twoSum([-10,20,-30,-40,20],-20))



### We need nums[a] + nums[b] == target
#    nums[a] == target - nums[b]