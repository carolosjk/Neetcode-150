from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        u,d = 0, len(matrix)-1

        while u <= d:

            row = (u+d)//2

            if target < matrix[row][0]:
                d = row-1
            elif target > matrix[row][len(matrix[row])-1]:
                u = row+1
            else:
                l,r = 0, len(matrix[row])-1

                while l <=r:
                    m = (l+r)//2

                    if target < matrix[row][m]:
                        r = m-1
                    elif target > matrix[row][m]:
                        l=m+1
                    else:
                        return True
                    
                return False


        return False


#   u = 0, d = 2, row = 1
#   u = 2, d = 2, row = 2
#   l = 0, r = 3, m = 1
#   l = 0, r = 0, m = 0
#   l = 0, r = -1




if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]],10))
    print(solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]],15))
