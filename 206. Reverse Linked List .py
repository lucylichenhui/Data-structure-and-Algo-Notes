class Solution(object):        
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

        #changing curr.next to prev changes the order or the links
        
        
    def reverseList_v1(self, head):  # Recursive
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p 