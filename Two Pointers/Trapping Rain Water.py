from typing import List
import re

class Solution:

    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        
        total = 0
        l,r = 0,1

        while r < length:

            while r < length and height[l] > height[r]: # while the left column is shorter than the right one
                r += 1
                print("r+1",r)

            if r == length:
                print("r==len")
                if height[l] > 0:
                    height[l] -= 1
                    r = l+1
                else:
                    l += 1
                    r = l+1
                continue

            if r-l < 2:
                l = r
                r += 1
                print("l=r, r=",r)
                continue

            smallest_height = min(height[r],height[l])
            print("smallest",smallest_height)
            l +=1
            while l < r:
                total += smallest_height - height[l]
                print("adding:", smallest_height - height[l])
                l += 1
            r +=1

        return total


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

