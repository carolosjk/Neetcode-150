from typing import List
import heapq

class Solution:
        
        def getDistance(self, p: List[int]) ->int:
            return (p[0]**2 + p[1] **2)**(1/2)
              

        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            heap = [[self.getDistance(i),i] for i in points]
            heapq.heapify(heap)

            return [y for x,y in (heapq.nsmallest(k,heap))]


    

if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest([[0,2],[2,0],[2,2]],2))
    print(solution.kClosest([[0,2],[2,2]],3))
    print(solution.kClosest([[0,3],[2,3],[1,1],[5,6],[0,7],[2,4],[-2,-4],[5,-1]],4))

    




