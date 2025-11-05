from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        isSubTree = False

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
            if not p:
                return
            
            if p.val == q.val:
                if self.isSameTree(p,q):
                    nonlocal isSubTree
                    isSubTree = True
            
            dfs(p.left, q)
            dfs(p.right, q)

        dfs(root, subRoot)

        return isSubTree



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


    

