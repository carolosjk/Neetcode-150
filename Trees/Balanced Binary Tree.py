from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def getHeight(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return 1+max(self.getHeight(root.right),self.getHeight(root.left))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return -1 <= self.getHeight(root.left)-self.getHeight(root.right) <= 1




if __name__ == "__main__":
    solution = Solution()
    

