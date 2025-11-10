import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        edges = {}
        for node in times:
            if node[0] not in edges:
                edges[node[0]] = []
            edges[node[0]].append((node[1],node[2]))
        
        heap = [(0,k)]
        visited = set()

        while heap:
            dis,node = heapq.heappop(heap)
            print(dis,node)

            if node in visited:
                continue

            visited.add(node)

            if node in edges:
                for n2,t2 in edges[node]:
                    heapq.heappush(heap,(dis+t2,n2))

            if len(visited) == n:
                return dis
        return -1

        
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime([[1,2,1],[2,3,1],[1,4,4],[3,4,1]],4,1))
    print(sol.networkDelayTime([[1,2,1],[2,3,1]],3,2))
            
            