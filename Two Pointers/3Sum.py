from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triples = []

        for i, a in enumerate(nums):

            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            j = i+1
            k = len(nums) - 1

            while j < k:
                sum = a + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                if sum < 0:
                    j += 1
                if sum == 0:
                    triples.append([a,nums[j],nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j +=1


        
        return triples

        
    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0,1,1]))

