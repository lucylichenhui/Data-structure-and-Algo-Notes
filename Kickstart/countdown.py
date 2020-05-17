
def initialize_solution():
    pass

import operator

def main():
    #print("i")
    
    

    N,K=input().strip().split(" ")
    N=int(N)
    K=int(K)
    #copy=K
    #for i in N: 

    num=list(map(int,input().strip().split(" ")))
    #nums=[]
    #for i in num: 
        #nums.append(int(i))
    #num=nums
    #print(num)
    #num=list(num)
    #D=True
    f=0
    
    # j=1
    # i=0
    # #while i<N-1:
    # while i<=N-2:
    #     while j<=N-1:
    #         if i<j:
    #             if num[i]>num[j]: 
    #                 if j-i==K: 
    #                     f+=1
    #                     i+=1
    #                     j=i+1
    #                 else:
    #                     j+=1
                        
    #             else: 
    #                 i+=1
    #                 j=i+1
    #         #else: 
                #j=i+1
                
    l=[]
    for i in range(K): 
        k=i+1
        l.append(k)

    #print(l)
    num=num[::-1]
    #print(num)
    i=0
    j=i+K
    while j<=N: 
       # print(num[i:j])
        if num[i:j]==l: 
            f+=1
            i=j
            j=i+K
        else: 
            i+=1
            j=i+K

    return f


    
    """ 

                    D=True
                    #print(num[i])
                    K-=1
                    j+=1
                    #i+=1
                    continue
                else: 
                    i+=1
                    D=False
                if K==0: 
                    K=copy
                #f+=1
 """

"""


        if num[i]<=num[i+1]:
            i+=1 
            D=True
        else: 
            if D:
                K-=1
                D=False 
                i+=1 
            else: 
                i+=1
        if K==0: 
            return num[i]

    return "IMPOSSIBLE"
"""




#OUTPUT_PREFIX = ""
OUTPUT_PREFIX = "Case #{}: "
INTERACTIVE = False
INTERACTIVE_WRONG_ANSWER = "WRONG"

#################################################### HELPERS



import sys

def read(callback=int, split=True):
    ipt = input().strip()
    if INTERACTIVE and ipt == INTERACTIVE_WRONG_ANSWER:
        sys.exit()
    if split:
        return list(map(callback, ipt.split()))
    else:
        return callback(ipt)

def write(value, end="\n"):
    if value is None: return
    try:
        if not isinstance(value, str): #checks if the object(first arg) is an instance or subclass of classinfo class(second argument)
            value = " ".join(map(str, value))
    except:
        pass
    print(value, end=end)
    if INTERACTIVE:
        sys.stdout.flush()

def solve_testcase():
    result = main()
    if result is not None:
        write(result)

if OUTPUT_PREFIX is None: # output prefix is the 
    solve_testcase() # call main function 
else:
    initialize_solution()

    """

    """

    TOTAL_CASES,= read() #always remember to modify

    for CASE_NUMBER in range(1, TOTAL_CASES+1):
        write(OUTPUT_PREFIX.format(CASE_NUMBER), end="") #want whatevers printed and the next thing printed to be in the same line
        solve_testcase()

