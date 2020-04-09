

#two sums
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): 
            other=target-nums[i]
            for j in range(len(nums)): 
                if nums[j]==other:
                    if j!=i:
                        return [i,j]



def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []



#================# 

# reverse and add elements of 2 linked lists 


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reversal(list): 
    head=ListNode(-1)
    global numlist 

    numlist=[]
    string=""
    prev=None 
    current=head
    while current: 
        numlist.append(current.val)
        nextnode=current.next
        current.next=prev 
        prev=current 
        current=nextnode
    return list

def add(sol1,sol2): 
    prev=None 
    temp=None
    carry=0
    while sol1 is not None and sol2 is not None: 
        fdata=sol1.val 
        sdata=sol2.val
        Sum=carry+fdata+sdata # val in int form, already 
        carry=1 if Sum>=10 else 0 # update carry to the new node 
        Sum= Sum if Sum <10 else Sum % 10 # update sum as remainder of carry 
        temp=ListNode(Sum) # note that in this question, we have to redefine temp 

        head=temp 
        #prev.next=temp 
        prev=temp
        if sol1 is not None: 
            sol1=sol1.next 
        if sol2 is not None: 
            sol2= sol2.next 
    if carry>0: 
        temp.next=Node(carry)
        
    temp=head
    result=[]
    while temp:
        result.append(temp)
        temp=temp.next
    return result
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sol1=reversal(l1)
        sol2=reversal(l2)
        sumlist=add(sol1, sol2)
        print(sumlist)



#================# 

