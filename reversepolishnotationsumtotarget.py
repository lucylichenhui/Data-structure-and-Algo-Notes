

import itertools
from itertools import permutations

def check(curr,o,n): 
    curr1=None 
    curr2=None
    if o=="+": 
        curr1=curr+n
    elif o=="*": 
        curr1=curr*n
    elif o=="-": 
        curr1=curr-n
        curr2=n-curr
    elif o=="/": 
        try:
            curr1=curr/n
            curr2=n/curr
            return curr1, curr2
        except ZeroDivisionError: 
            return float("inf"), float("inf")
        try:
            curr1=curr/n
            curr2=n/curr
            return curr1, curr2
        except ZeroDivisionError: 
            return float("inf"), float("inf")
    return curr1, curr2

        
def rpnevaluator(arr,i,target):
    curr1=None
    curr2=None
    stack=[]
    start=0
 

    arr=[char for char in arr]
    i=list(i)
    while len(arr)!=0 and len(i)!=0: 

        if start==0:
            curr=arr.pop()
            
            start+=1
            o=i.pop()
            n=arr.pop()
            curr1, curr2=check(curr,o,n)
            if not curr2: 
                stack.append(curr1)
            else: 
                stack.extend([curr1,curr2])

        o=i.pop()
        n=arr.pop() 
        newstack=[]
        start+=1
        while stack:

            curr=stack.pop()
            curr1, curr2=check(curr,o,n)

            if curr2: 
                newstack.extend([curr1,curr2])
            else: 
                newstack.extend([curr1])
                #stack=[]
            if start==3:  
                if curr1==target: 
                    #print(curr1)
                    return True
                    
                if curr2: 
                    if curr2==target: 
                        #print(curr2)
                        return True 
        if newstack is not None: 
            stack.extend(newstack)

    if curr1==target: 
        return True
    if curr2: 
        if curr2==target: 
            return True 
    return False

            

def main(arr, target):
    perm=itertools.permutations(arr)
    #print(perm)

    operands=["+","-","*","/"]

    visited=[]

    for a in operands: 
        for b in operands: 
            for c in operands: 
                if a+b+c not in visited: 
                    visited.append(a+b+c)
    sol=[]

    for i in perm: 
        for p in visited: 
            if rpnevaluator(i,p,target): 
                print(i)
                print(p)


main(arr=[5,6,2,3],target=24)