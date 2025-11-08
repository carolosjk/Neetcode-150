from typing import Optional
import copy

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        oldToNew = {}

        def dfs(node: Optional["Node"]) -> Optional["Node"]:
            if node in oldToNew:
                return oldToNew[node]
            
            new = Node(node.val)
            oldToNew[node] = new
            if node.neighbors:
                for n in node.neighbors:
                    new.neighbors.append(dfs(n))
            return new
        
        return dfs(node)
    

    




if __name__ == "__main__":
    sol = Solution()
    print(sol.cloneGraph())