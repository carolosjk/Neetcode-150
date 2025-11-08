class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x



if __name__ == "__main__":
    sol = Solution()
    sol.isPalindrome(-10)
    sol.isPalindrome(10)
    sol.isPalindrome(0)
    sol.isPalindrome(7)
    sol.isPalindrome(123)
        