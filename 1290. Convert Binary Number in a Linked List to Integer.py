# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        output = ""
        while head:
            output += str(head.val)
            head = head.next
        return int(output, 2)


def print_list(head):
    ptr = head
    while ptr is not None:
        print(ptr.val, end=' —> ')
        ptr = ptr.next

    print('None')

node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)

node1.next = node2
node2.next = node3

print_list(node1)
solution = Solution()
print(solution.getDecimalValue(node1))