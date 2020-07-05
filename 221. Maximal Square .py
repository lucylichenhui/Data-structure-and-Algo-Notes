class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n=len(matrix)
        m=len(matrix[0])
        #bfs
        m=0
        cnt=1
        mat = [[1 for x in range(m)] for y in range(n)] 
        #mat[0][0]=1
        for a in range(1,n): # col 
            for b in range(1,m): # row
                if mat[a-1][b-1]>0: 
                    ma=mat[a-1][b-1]
                    if all(element>0 for element in mat[a-ma:a][b]) and all(element>0 for element in mat[a][b-ma:b]): 
                        mat[a][b]=mat[a-1][b-1]+1
                        cnt+=1 
                    
    
        return cnt**2



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[]: 
            return 0

        
        n=len(matrix)
        m=len(matrix[0])
        print(n)
        print(m)

        cnt=0
        #mat = [[1 for x in range(m)] for y in range(n)] 
        #mat=matrix
        #mat[0][0]=1
        for a in range(0,n): # col 
            for b in range(0,m): # row
                if matrix[a][b]=="1":
                    cnt=max(1,cnt)
                if a!=0 and b!=0:
                    if int(matrix[a-1][b-1])>0: 
                        ma=int(matrix[a-1][b-1])
                        try:
                            #print(matrix[a-ma:a][b])
                            #Y=all(int(element)>0 for element in matrix[a-ma:a][b])
                            #print(Y)
                            if all(int(element)>0 for element in matrix[a-ma:a+1][b]) and all(int(element)>0 for element in matrix[a][b-ma:b+1]): 
                                matrix[a][b]=int(matrix[a-1][b-1])+1
                                cnt=max(cnt,matrix[a][b])

                        except IndexError: 
                            pass
        return cnt**2 



class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[]: 
            return 0

        
        n=len(matrix)
        m=len(matrix[0])
        #print(n)
        #print(m)

        cnt=0
        #mat = [[1 for x in range(m)] for y in range(n)] 
        #mat=matrix
        #mat[0][0]=1
        for a in range(0,n): # col 
            for b in range(0,m): # row
                if matrix[a][b]=="1":
                    cnt=max(1,cnt)
                if a!=0 and b!=0:
                    if int(str(matrix[a-1][b-1]))>0: 
                        ma=int(matrix[a-1][b-1])
                        print(ma)
                        try:
                            #print(matrix[a-ma:a][b])
                            #Y=all(int(element)>0 for element in matrix[a-ma:a][b])
                            #print(Y)
                            mr= min([int(element) for element in matrix[a-ma:a+1][b]])
                            mc= min([int(element) for element in matrix[a][b-ma:b+1]])                            
                            mini=min(mr,mc)
                            print("Y")
                            if ma>mini: 
                                matrix[a-1][b-1]=mini
                            matrix[a][b]=int(matrix[a-1][b-1])+1
                            cnt=max(cnt,matrix[a][b])

                        except IndexError: 
                            pass


                    
        print(matrix)
        return cnt**2 




class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[]: 
            return 0

        
        n=len(matrix)
        m=len(matrix[0])
        print(n)
        print(m)

        cnt=0
        #mat = [[1 for x in range(m)] for y in range(n)] 
        #mat=matrix
        #mat[0][0]=1
        for a in range(0,n): # col 
            for b in range(0,m): # row
                if matrix[a][b]=="1":
                    cnt=max(1,cnt)
                if a!=0 and b!=0:
                    if int(matrix[a-1][b-1])>0: 
                        try:
                            r=matrix[0:a+1][:: -1][b].index("0")-1
                        except ValueError: 
                            r=n
                        try:
                            c=matrix[a][0:b+1][::-1].index("0")-1
                        except ValueError: 
                            c=m
                        ma=min(int(matrix[a-1][b-1]),r,c)
                        try:
                            #print(matrix[a-ma:a][b])
                            #Y=all(int(element)>0 for element in matrix[a-ma:a][b])
                            #print(Y)
                            #if all(int(element)>0 for element in matrix[a-ma:a+1][b]) and all(int(element)>0 for element in matrix[a][b-ma:b+1]): 
                            matrix[a][b]=min(int(matrix[a][b]),ma)+1
                            cnt=max(cnt,matrix[a][b])

                        except IndexError: 
                            pass
                        
        print(matrix)
        return cnt**2 


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[]: 
            return 0

        
        n=len(matrix)
        m=len(matrix[0])
        print(n)
        print(m)

        cnt=0
        #mat = [[1 for x in range(m)] for y in range(n)] 
        #mat=matrix
        #mat[0][0]=1
        for a in range(0,n): # col 
            for b in range(0,m): # row
                if matrix[a][b]=="1":
                    cnt=max(1,cnt)
                if a!=0 and b!=0:
                    if int(matrix[a-1][b-1])>0: 
                        try:
                            r=matrix[0:a+1][:: -1][b].index("0")-1
                        except ValueError: 
                            r=n
                        try:
                            c=matrix[a][0:b+1][::-1].index("0")-1
                        except ValueError: 
                            c=m
                        ma=min(int(matrix[a-1][b-1]),r,c)
                        try:
                            #print(matrix[a-ma:a][b])
                            #Y=all(int(element)>0 for element in matrix[a-ma:a][b])
                            #print(Y)
                            #if all(int(element)>0 for element in matrix[a-ma:a+1][b]) and all(int(element)>0 for element in matrix[a][b-ma:b+1]): 
                            matrix[a][b]=max(int(matrix[a][b]),min(int(matrix[a-1][b-1]),ma)+1)
                            cnt=max(cnt,matrix[a][b])

                        except IndexError: 
                            pass

                    
        print(matrix)
        return cnt**2 


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[]: 
            return 0

        
        n=len(matrix)
        m=len(matrix[0])
        #print(n)
        #print(m)
        matrixzipped=zip(matrix)

        cnt=0
        #mat = [[1 for x in range(m)] for y in range(n)] 
        #mat=matrix
        #mat[0][0]=1
        for a in range(0,n): # col 
            for b in range(0,m): # row
                if matrix[a][b]=="1":
                    cnt=max(1,cnt)
                if a!=0 and b!=0:
                    
                    if int(matrix[a-1][b-1])>0 and int(matrix[a][b])>0: 
                        try:
                            .index("0")

                            len(verts) - 1 - verts[::-1].index(value)


                            print(matrix[0:a+1][b][::-1])
                            r=matrix[0:a+1][b][::-1].index("0")-1
                        
                        except ValueError: 
                            r=a
                        try:
                            c=matrix[a][0:b+1][::-1].index("0")-1
                        except ValueError: 
                            c=b
                        ma=min(r,c)
                        #print(r)
                        #print(c)
                        try:
                            
                            #print(matrix[a-ma:a][b])
                            #Y=all(int(element)>0 for element in matrix[a-ma:a][b])
                            #print(Y)
                            #if all(int(element)>0 for element in matrix[a-ma:a+1][b]) and all(int(element)>0 for element in matrix[a][b-ma:b+1]): 
                            matrix[a][b]=max(int(matrix[a][b]),min( int(matrix[a-1][b-1]),ma)+1)
                            cnt=max(cnt,matrix[a][b])

                        except IndexError: 
                            pass

                    
        print(matrix)
        return cnt**2 