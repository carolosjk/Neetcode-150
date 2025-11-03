from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def getDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return 1+max(self.getDepth(root.left),self.getDepth(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)




if __name__ == "__main__":
    solution = Solution()
    # print(solution.invertTree([[1,2,4,8],[10,11,12,13],[14,20,30,40]],10))

