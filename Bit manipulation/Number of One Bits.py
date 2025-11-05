from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res +=1 if 1&n else 0
            n = n >> 1
        return res