class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for strings in strs:     
            tokens=str(sorted([i for i in strings]))
            d[tokens].append(strings)
        f=[]
        for i in d.values(): 
            f.append(i)
        return f
            