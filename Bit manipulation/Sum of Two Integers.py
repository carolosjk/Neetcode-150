from typing import List

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b !=0:
            carry = (a&b) << 1
            a = a^b & mask
            b = carry & mask
        
        if a > 0x8FFFFFFF:
            a = ~(a ^ mask)
        return a
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(1,2))
    print(solution.getSum(2,-5))
    print(solution.getSum(10,-3))

    m = 3
    n = 2
    print([[] for i in range(m)])
