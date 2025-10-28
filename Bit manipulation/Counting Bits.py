from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            bitCount = 0
            num = i
            while num:
                bitCount += num & 1
                num >>= 1
            arr.append(bitCount)
        
        return arr
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(3))
    print(solution.countBits(10))
    print(solution.countBits(4))
    