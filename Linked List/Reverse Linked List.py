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

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value: int):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def print(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
         

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head

        while current :
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous
    


if __name__ == "__main__":
        solution = Solution()

        list1 = LinkedList()
        for i in range(10):
            list1.append(i)

        list1.print()
        print(solution.reverseList(list1.head))
        list1.print()
