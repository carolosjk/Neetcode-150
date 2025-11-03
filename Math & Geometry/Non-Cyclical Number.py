

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        num = n

        while num != 1:
            if num in visited:
                return False
            
            new_num = 0
            for i in str(num):
                new_num += int(i) ** 2
            visited.add(num)
            num = new_num


        return True




        

if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(1))
    print(solution.isHappy(2))
    print(solution.isHappy(3))


# 1 -> 1^2 -> 1
# 2 -> 4 -> 16 -> 1 + 36 = 37 -> 9 + 49 = 58 -> 25 + 64 = 89 -> 64 + 81 = 145 -> 1 + 16 + 25 = 42 -> 16 + 4 = 20 -> 4
# 
# 
# 
# 