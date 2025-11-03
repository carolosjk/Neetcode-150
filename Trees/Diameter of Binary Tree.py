from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            if not root:
                return 0
            
            nonlocal diameter
            
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter,left+right)

            return 1+max(left,right)

        dfs(root)
        return diameter




if __name__ == "__main__":
    solution = Solution()
    

