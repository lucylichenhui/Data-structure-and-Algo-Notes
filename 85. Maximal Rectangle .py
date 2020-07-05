class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        mat = [[0 for x in range(cols)] for y in range(rows)]
        mat[0]=[(0,i) for i in range(len(matrix[0]))] #row1
        print(mat[0])
        
        #for 
