from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            if n & (1 << i):
                print(n,i)
                num = num | (1 << 31-i)
        return num

# 00000000000000000000000000000001 -> 10000000000000000000000000000000
# 00000000000000000000000000010101 -> 10101000000000000000000000000000
# 
# 
# 
# 

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseBits(3))
    print(solution.reverseBits(10))
    print(solution.reverseBits(4))
    print(solution.reverseBits(21))
    