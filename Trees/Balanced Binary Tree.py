from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(root: Optional[TreeNode]) -> bool:
            nonlocal isBalanced 
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right) > 1:
                isBalanced = False
            
            return 1+max(left,right)
        
        dfs(root)
        return isBalanced






if __name__ == "__main__":
    solution = Solution()

    

