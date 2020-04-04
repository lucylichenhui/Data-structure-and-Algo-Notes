
 
def isduplicates(array): 
    for i in range(0,len(array)):
        for j in range(1, len(array)): 
            if j!=i: 
                if array[i]==array[j]: 
                    return True 
    
    return False

def islatinsquare(dimension,matrix): 
    BOOL=True
    global r 
    global c
    c=0
    r=0
    #print(matrix)
    for a in range(dimension): 
        #print([row[a] for row in matrix])
        if isduplicates([row[a] for row in matrix]): #column array 
            c+=1
            BOOL=False #important to note that if return False, func will terminate
    for array in matrix: #row array 
        if isduplicates(array): 
            r+=1
            BOOL=False
    #print(r)
    #print(c)
    

def output(T,dimension,matrix):
    k=0
    for i in range(dimension):
        k+=matrix[i][i]
    #print(trace)
    x=casenum
    islatinsquare(dimension,matrix)
    print("Case #"+str(x)+": "+str(k)+" "+str(r)+" "+str(c))



T=int(input().strip())

for i in range(T): 
    casenum=i+1
    matrix = [] 
    dimension=int(input().strip())
    # For user input 
    for i in range(dimension):          # A for loop for row entries 
        a =[] 
        input1=input().split(" ")
        for j in range(dimension):      # A for loop for column entries 
            a.append(int(input1[j])) 
        matrix.append(a)
    output(T,dimension,matrix)