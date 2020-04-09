from collections import deque

def merge2lists(l1,l2): 
    mergedlist=[]
    deque1=deque(l1)
    deque2=deque(l2)
    
    while deque1 or deque2: 
                
        if not deque1: 
            for i in range(len(deque2)): 
                mergedlist.append(deque2[i])
            return mergedlist 

        elif not deque2:  
            for i in range(len(deque1)): 
                mergedlist.append(deque1[i])
            return mergedlist 
        else:
            a=deque1[0]
            #print(deque1)
            b=deque2[0]
            if a>b: 
                mergedlist.append(deque2.popleft())
            elif a<b: 
                mergedlist.append(deque1.popleft())

            else: 
                mergedlist.append(deque1.popleft())
                mergedlist.append(deque2.popleft())
                
    print(mergedlist)
    return mergedlist 

def findmedian(mergedlist): 
    #print(mergedlist)
    if len(mergedlist)%2==0:
        median=float(mergedlist[int(len(mergedlist)/2)]+mergedlist[int(len(mergedlist)/2-1)])/2
    else: 
        median=(mergedlist[len(mergedlist)//2])
    return median
    

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        mergedlist=merge2lists(nums1,nums2) 
        median=findmedian(mergedlist)
        return median
        