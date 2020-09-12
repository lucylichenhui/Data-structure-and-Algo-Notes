class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        generators=len(arr)
        num=math.ceil(float(generators)/2)
        d=defaultdict(int)
        for i in arr: 
            d[i]+=1
        final=0
        d = sorted(d.items(), key=operator.itemgetter(1))
        while int(num)>0:
            maxiumumvalue=d[len(d)-1]
            a,b=maxiumumvalue
            num-=b
            d.pop()
            final+=1
        return final