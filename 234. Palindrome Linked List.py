# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

lreverse=[]
def traverseinreverse(head): 
    if not head: #base case, empty list 
        return
    traverseinreverse(head.next) 
    lreverse.append(head.val)
    return lreverse

list=[]
def traverselist(head): 
    temp=head
    while temp: 
        list.append(temp.val)
        temp=temp.next 
    return list


def isPalindrome():
    if not head:
        return True
    traverseinreverse(head)
    traverselist(head)
    #i,j=0,len(list)-1
    #while i!=len(list)-1 and j!=0:
        #if list[i]==lreverse[j]: 
            #i+=1 
            #j-=1 
        #else: return "false"
    #return "true"

    return lreverse==list




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        if head.next is None:
            return True
        
        address = head.next
        
        res = [head.val]
        
        while address:
            res.append(address.val)
            address = address.next
            
        return res == res[::-1]
            