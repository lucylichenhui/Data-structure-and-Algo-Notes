class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt=Counter()
        for i in words: 
            cnt[i]+=1
        cnt=sorted(cnt.items(), key=itemgetter(0))
        
        c=Counter()
        for a, b in cnt: 
            c[a]=b
        return [ i for i, x in c.most_common()][:k]