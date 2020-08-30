

def printSol(matrix,output,n): 
    #print(n)
    newmatrix=[]
    for i in range(n): 
        string=""
        for j in range(n): 
            if matrix[i][j]==1:
                string+="Q"
            else:
                string+="."
        newmatrix.append(string)
    output.append(newmatrix)
    #print(output)
    return output


# need to check for columns that are to the left of the queens placed 
def feasible(matrix,i,j,n): 

    #check horizontally
    for a in range(j): 
        if matrix[i][a]==1: 
            return False
    
    #going along the left diagonal, up
    for a,b in zip(range(i,-1,-1),range(j,-1,-1)): 
        if matrix[a][b]==1: 
            return False 

    #going along the left diagonal, down 
    for a,b in zip(range(i,n,1),range(j,-1,-1)): 
        if matrix[a][b]==1: 
            return False 
    return True

# places queens column by column
def placeQueens(matrix,j,n,output): 
    if j==n: 
        printSol(matrix,output,n)
        return True
    res=False
    for row in range(n): 
        if feasible(matrix,row,j,n)==True: 
            matrix[row][j]=1
            res= placeQueens(matrix,j+1,n,output) or res#if last layer is placed, return True  
            #return True
            matrix[row][j]=0
    return res

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output=[]
        matrix=[]
        for i in range(n):
            input1=[int(0)]*n
            matrix.append(input1)
        #if placeQueens(matrix,j,n)==False: 
            #return False
        #placeQueens(matrix,0,n,output)
        if placeQueens(matrix,0,n,output)==False: 
            return 
        return output

