# Given the head of a linked list and an integer val, remove all the nodes of the linked list
# that has Node.val == val, and return the new head.

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


     def __str__(self):
         return str(self.val)

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        cur = head
        prev = dummy

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur

            cur = cur.next

        return dummy.next

def print_list(head):
    ptr = head
    while ptr is not None:
        print(ptr.val, end=' —> ')
        ptr = ptr.next

    print('None')



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7


solution = Solution()
print_list(node1)
solution.removeElements(node1,6)
print_list(node1)