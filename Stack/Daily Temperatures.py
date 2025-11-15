from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _,index = stack.pop()
                res[index] = i-index
            stack.append((temp,i))
        
        return res


    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("[]"))
    print(solution.isValid("{[]}"))
    print(solution.isValid("([(]})"))

