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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        current = None

        while list1 and list2:
            smaller = None
            if list1.val < list2.val:
                smaller = list1
                list1 = list1.next
            else:
                smaller = list2
                list2 = list2.next
            if not head:
                head = smaller
                current = smaller
            else:
                current.next = smaller
                current = smaller
            
        
        while list1:
            if not head:
                head = list1
                current = list1
            else:
                current.next = list1
                current = list1
            list1 = list1.next

        while list2:
            if not head:
                head = list2
                current = list2
            else:
                current.next = list2
                current = list2
            list2 = list2.next
                

        return head
    


if __name__ == "__main__":
        solution = Solution()

        list1 = LinkedList()
        for i in range(10):
            list1.append(i)

        list2 = LinkedList()
        list2.append(2)
        list2.append(3)
        list2.append(5)
        list2.append(7)

        list1.print()
        print(solution.mergeTwoLists(list1.head, list2.head))
        list1.print()
