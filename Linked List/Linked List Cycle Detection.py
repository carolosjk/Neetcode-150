# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next         

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        p1, p2 = head, head
         
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True
         

        return False


if __name__ == "__main__":
        solution = Solution()
