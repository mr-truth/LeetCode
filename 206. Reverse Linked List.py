# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


     def __str__(self):
         return str(self.val)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous



def print_list(head):
    ptr = head
    while ptr is not None:
        print(ptr.val, end=' —> ')
        ptr = ptr.next

    print('None')


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print_list(node1)
solution = Solution()
print(solution.reverseList(node1))