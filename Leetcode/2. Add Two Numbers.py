from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2:

            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            sum = d1+d2+carry

            tail.next = ListNode(sum % 10)
            carry = sum // 10

            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next
            



        


if __name__ == "__main__":
    sol = Solution()
    # sol.addTwoNumbers()

        