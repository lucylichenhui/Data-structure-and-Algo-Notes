class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        cnt=0
        for i in range(1,len(A)): 
            if A[i]==A[i-1]: 
                if B[i-2]<A[i-1]:
                    Bi=B[i-1]
                    Ai=A[i-1]
                    A[i-1]=Bi
                    B[i-1]=Ai
                    cnt+=1
                elif B[i]>A[i-1]: 
                    Bi=B[i]
                    Ai=A[i]
                    A[i]=Bi
                    B[i]=Ai
                    cnt+=1
                
            if  B[i]==B[i- 1]:
                if A[i-2]<B[i-1]:
                    Bi=B[i-1]
                    Ai=A[i-1]
                    A[i-1]=Bi
                    B[i-1]=Ai
                    cnt+=1
                elif A[i]>B[i-1]: 
                    Bi=B[i]
                    Ai=A[i]
                    A[i]=Bi
                    B[i]=Ai
                    cnt+=1                
                
            elif A[i]<A[i-1] or B[i]<B[i- 1]: 
                Bi=B[i]
                Ai=A[i]
                A[i]=Bi
                B[i]=Ai
                cnt+=1
        print(A)
        print(B)

        return cnt
        



        for i in range(1,len(A)): 
            if A[i]<=A[i-1]: 
                if B[i-2]<A[i-1]:
                    Bi=B[i-1]
                    Ai=A[i-1]
                    A[i-1]=Bi
                    B[i-1]=Ai
                    cnt+=1
                elif B[i]>A[i-1]: 
                    Bi=B[i]
                    Ai=A[i]
                    A[i]=Bi
                    B[i]=Ai
                    cnt+=1
                
            if  B[i]<=B[i- 1]:
                if A[i-2]<B[i-1]:
                    Bi=B[i-1]
                    Ai=A[i-1]
                    A[i-1]=Bi
                    B[i-1]=Ai
                    cnt+=1
                elif A[i]>B[i-1]: 
                    Bi=B[i]
                    Ai=A[i]
                    A[i]=Bi
                    B[i]=Ai
                    cnt+=1                

        print(A)
        print(B)

        return cnt






class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        cntA1=copy.deepcopy(A)
        cntA2=copy.deepcopy(A)
        cntB1=copy.deepcopy(B)
        cntB2=copy.deepcopy(B)
        for i in range(1,len(A)): 
            ai=A[i]
            bi=B[i]
            if A[i-1]>=A[i] or B[i-1]>=B[i]: 
                if B[i-2]<A[i-1]
                    Bi=B[i-1]
                    Ai=A[i-1]
                    cntA1[i-1]=Bi
                    cntB1[i-1]=Ai


                B[i]=ai
                A[i]=bi
                arr[i]=1

        print(A)
        print(B)
        print(arr)
        return sum(arr)


