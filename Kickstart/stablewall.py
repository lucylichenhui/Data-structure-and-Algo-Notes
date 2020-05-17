
from collections import deque




def initialize_solution():
    pass

import operator

def main():
    global matrix 
    global visited 
    f=""
    matrix=[] 
    d1, d2=input().strip().split(" ")
    d1=int(d1)
    d2=int(d2)
    # For user input 
    for i in range(d1):          # A for loop for row entries 
        a =[] 
        input1=input()
        l=[]
        for i in input1: 
            l.append(i)
        for j in range(d2):      # A for loop for column entries 
            a.append(l[j]) 
        matrix.append(a)

        
    n=d1
    m=d2
    
    visited = [[0] * m for i in range (n)] #m being row, n being column 

    # use BFS 

    
    for j in range(m):
        for i in range(n-1,-1,-1): 
            if visited[i][j]!=1:
                if bfs(i,j,visited,n,m) is not None: 
                    f+=bfs(i,j,visited,n,m) 
    return f


def bfs(i,j,visited,n,m):
    copy=visited
    visited[i][j]=1
    queue = deque([(i,j)]) #always hold indexes in a tuple 
    while queue:
        # print(queue)
        point = queue.pop() 
        i = point[0]
        j = point[1] 

        if i < n-1 and visited[i+1][j] == 0 and matrix[i+1][j] == matrix[i][j] : #start from the bottom right hand corner
            queue.append((i+1, j ))
            visited[i+1][j]=1
            
        if j < m-1 and visited[i][j+1] == 0 and matrix[i][j+1] == matrix[i][j]:
            queue.append((i, j+1 ))
            visited[i][j+1]=1
        
        if matrix[i][j]!=matrix[i][j-1] or visited[i][j-1]!=1: 
            visited=copy
            return None 

    print(visited)
    return matrix[i][j]
    """



    while i<=colu: 
        while j<=rows: 
            num1=1
            num=0
            if col[i]!=col[i+1]:
                if matrix[row-num1][col]==matrix[row-num][col] or du[row-num1][col]==1:
                    du[row-num][col]=1
                    num1-=1 
                    num-=1

                else: 
                    i=i+1 
                if j==rows: 

    #print(matrix)

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
