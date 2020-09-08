class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s=defaultdict(int)
        for i in bills: 
            if i==5:
                s[5]+=1
            if i==10: 
                if s[5]: 
                    s[5]-=1
                else: 
                    return False
                s[10]+=1
            if i==20: 
                if s[10]>=1 and s[5]>=1: 
                    s[10]-=1
                    s[5]-=1 
                elif s[5]>=3:
                    s[5]-=3
                else: 
                    return False
                #s[20]+=1
        return True