import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        n, node = len(points), 0
        visited = set()
        distances = [1000000000] * n
        distance = 0

        while len(visited) < n-1:
            visited.add(node)

            next_node = -1

            for i in range(n):

                if i in visited:
                    continue

                dist = (abs(points[i][0]-points[node][0]) 
                         + abs(points[i][1]-points[node][1]))

                distances[i] = min(distances[i], dist)

                if next_node == -1 or distances[i] < distances[next_node]:
                    next_node = i
            
            node = next_node
            distance += distances[next_node]

        return distance




        
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]]))
    print(sol.minCostConnectPoints([[7,7],[8,0],[9,-9],[-3,4]]))
            
            