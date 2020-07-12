
#Slow language doesnt work 
from collections import defaultdict
def initialize_solution():
    pass

import operator

def main():
    #print("i")

    cnt=0
    N=input().strip()
    List=input().strip().split(" ")
    #R=[0]*len(List)
    s={"u":0,"d":0}
    i=1
    #while i<len(List):
    for i in range(1,len(List)): 
        if s["d"]>3 or s["u"]>3: 
            s={"u":0,"d":0}
            cnt+=1
            i+=1
        if List[i-1]>List[i]: 
            s["u"]+=1
            #i+=1
        elif List[i-1]<List[i]: 
            s["d"]+=1
            #i+=1
        elif List[i-1]==List[i]: 
            pass
            #i+=1

    print(cnt)


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

