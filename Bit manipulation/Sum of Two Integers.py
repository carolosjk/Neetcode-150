from typing import List

class Solution:
    def getSum(self, a: int, b: int) -> int:

        num = 0
        carry = 0
        
        for i in range(32):
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1
            bit = bit1 ^ bit2 ^ carry
            carry = (bit1&bit2) | (bit1&carry) | (bit2&carry)
            print(bit1,bit2,bit,carry)
            if bit:
                num |= (1 << i)

        if num > 0x7FFFFFFF:
            num = ~(num^0xFFFFFFFF)
        
        return num
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(1,2))
    print(solution.getSum(2,-5))
    print(solution.getSum(10,-3))

    m = 3
    n = 2
    print([[] for i in range(m)])
