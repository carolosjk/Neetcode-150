from typing import List

class Solution:

    def getTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCountDict = {}
        for n in nums:
            numberCountDict[n] = numberCountDict.get(n,0) + 1

        sortedNumberList = list(tuple(sorted(numberCountDict.items(),)))
        print(sortedNumberList)

    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.getTopKFrequent([1,2,2,3,3,3], 2))
    print(solution.getTopKFrequent([1,2,2,3,3,3], 1))
    print(solution.getTopKFrequent([1,2,2,3,3,3,4,3,4,7], 3))
