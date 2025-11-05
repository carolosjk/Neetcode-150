from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
                break

        if carry == 1:
            digits = [1] + digits

        return digits


        

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1,2,3,4]))
    print(solution.plusOne([9,9,9]))


# 1 -> 1^2 -> 1
# 2 -> 4 -> 16 -> 1 + 36 = 37 -> 9 + 49 = 58 -> 25 + 64 = 89 -> 64 + 81 = 145 -> 1 + 16 + 25 = 42 -> 16 + 4 = 20 -> 4
# 
# 
# 
# 