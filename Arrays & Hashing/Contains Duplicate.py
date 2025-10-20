
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_we_found = {}
        for i in nums:
            if i in numbers_we_found:
                return True
            numbers_we_found[i] = True

        return False
    

if __name__ == "__main__":

    solution = Solution()