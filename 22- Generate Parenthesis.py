class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        finalsolution=[]
        def possibilities(L=0,R=0,string=""):
            if len(string)==n*2: 
                finalsolution.append(string)
                print(string)
                return 
            else: 
                if L<n:
                    possibilities(L+1,R,string+"(")
                if R<L:
                    possibilities(L,R+1,string+")")
        possibilities()
        return finalsolution        
