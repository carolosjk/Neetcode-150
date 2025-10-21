from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i < j:
            sum = numbers[i] + numbers[j]

            if sum == target:
                return [i+1,j+1]
            if sum > target:
                j -= 1
            if sum < target:
                i += 1
    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([1,2,3,4],3))
    print(solution.twoSum([2,4,6,8,10,12,14,15,16,18,20],23))

