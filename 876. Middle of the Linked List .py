# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None: 
            return None  
        else: 
            curri=head 
            currj=head
            while curri and currj and currj.next: 
                curri=curri.next
                currj=currj.next.next

        return ListNode(curri).val