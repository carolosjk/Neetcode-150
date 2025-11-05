from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p:
                return True if not q else False
            
            if not q:
                return True if not p else False
            
            return p.val == q.val and dfs(p.left,q.left) and dfs(p.right,q.right)



        return dfs(p,q)
        



if __name__ == "__main__":
    solution = Solution()

    

