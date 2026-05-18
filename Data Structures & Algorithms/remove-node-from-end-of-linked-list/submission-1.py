# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next

        if n == len(nodes):
            return head.next
        
        nodes[-n - 1].next = nodes[-n].next
        return head

