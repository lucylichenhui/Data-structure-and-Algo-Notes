
#Q 451
#Given a string, sort it in decreasing order based on the frequency of characters.

def keywithmaxval(d):
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol=""
        d=defaultdict(int)
        for w in s: 
            d[w]+=1 

        while d:
            maxkey=keywithmaxval(d)
            sol+=maxkey*d[maxkey]
            del d[maxkey]

        return sol

    