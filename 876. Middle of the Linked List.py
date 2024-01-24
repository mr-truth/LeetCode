# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.


from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


     def __str__(self):
         return str(self.val)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_pointer = head
        second_pointer = head

        while first_pointer and first_pointer.next:
            second_pointer = second_pointer.next
            first_pointer = first_pointer.next.next

        return second_pointer


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
print(solution.middleNode(node1))
