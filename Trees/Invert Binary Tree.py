from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def invertNodes(self, root: Optional[TreeNode]):
        if not root:
            return None
        
        temp = root.left
        root.left = self.invertNodes(root.right)
        root.right = self.invertNodes(temp)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertNodes(root)

        return root




if __name__ == "__main__":
    solution = Solution()
    # print(solution.invertTree([[1,2,4,8],[10,11,12,13],[14,20,30,40]],10))

