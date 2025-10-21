from typing import List

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCountDict = {}
        for n in nums:
            numberCountDict[n] = numberCountDict.get(n,0) + 1

        freq = [[] for _ in range(len(nums)+1)]


        for num,count in numberCountDict.items():
            freq[count].append(num)

        topK = []

        for bucket in reversed(freq):
            for num in bucket:
                topK.append(num)

                if len(topK) == k:
                    return topK

        return topK

    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,2,2,3,3,3], 2))
    print(solution.topKFrequent([1,2,2,2,2,3,3], 1))
    print(solution.topKFrequent([1,1,1,2,2,3], 2))

    

# 0 1 1 0 1
# 1 1 0 1 0
# 0 1 1 1 0
