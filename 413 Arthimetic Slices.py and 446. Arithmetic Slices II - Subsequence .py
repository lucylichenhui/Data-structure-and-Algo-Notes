

# First try 

def ps(num): 
    s=0
    for i in range(num): 
        s+=i 
    return s

def printsum(e): 
    a=0
    for i in range(e): 
        a+=i 
    f=e+1
    print(f)
    while f-1//2>=2:
        if f%2!=0: 
            u=f//2+1
            d=f//2
        else: 
            d=f//2
            u=f//2
        #print(u)
        #print(d)
        if u>=3:
            a+=ps(u-1) 
            print("u")
            print(u)
            #print(u)
            print(ps(u-1) )
        if d>=3:
            a+=ps(d-1)
            #print(d)
            print("d")
            print(d)
            print(ps(d-1) )
        #printsum(e//2)
        f-=2
    return a


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
                
        cnt=0
        i=0
        while i<len(A)-2:
        #for i in range(len(A)-2): 
            B=False
            initialdiff=A[i+1]-A[i]
            for j in range(i+2,len(A)): 
                if A[j]-A[j-1]==initialdiff: 
                    pass
                else: 
                    cnt+=printsum(len(A[i:j-1]))
                    #print(cnt)
                    B=True
                    i=j-1
                    break 
            if not B: 
                #print(len(A[i:j]))
                cnt+=printsum(len(A[i:j]))
                i=j  
        return cnt






class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        from collections import defaultdict
        d = [defaultdict(int) for item in A]
        #print(d)
        total=0
        for i in range(len(A)): 
            for j in range(i): 
                d[i][A[i]-A[j]]+=1
                if A[i]-A[j] in d[j]: 
                    d[i][A[i]-A[j]]+=d[j][A[i]-A[j]]
                    total+=d[j][A[i]-A[j]]
        return total
                
                


