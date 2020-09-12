#This was not very straightforward.

"""
3
1
3
7
3
4
3
3

"""


n=input()
wallpos=[]
wallheight=[]
for i in range(n): 
    wallpos.append(input())

m=input()
for i in range(m): 
    wallheight.append(input())

"""
maximumheight=0
newlist=[wallheight[0]]
for a in range(min(wallpos)+1,max(wallpos)): 
    if a in wallpos: 
        newlist.append(wallheight[wallpos.index(a)])
        pass
    else: 
        value=newlist[a-2]
        if a+1 in wallpos: 
            nextheight=wallheight[wallpos.index(a+1)]
        else:
            nextheight=float('inf')
        maximumheight=max(maximumheight,min(value+1,nextheight))
        newlist.append(min(value+1,nextheight))

print(newlist)
print(maximumheight)
"""
from math import ceil
# Solution I coded was suboptimal, should not think this way
maximum=0
for i in range(n-1): 
    if wallpos[i]<wallpos[i+1]-1: 
        heightdiff=abs(wallheight[i+1]-wallheight[i-1])
        gaplen=wallpos[i+1]-wallpos[i]-1 # want total number of slots for the mud
        localmax=0
        if gaplen>heightdiff: 
            low=max(wallheight[i+1],wallheight[i])+1
            remaininggap=gaplen-heightdiff-1
            localmax=low+ceil(remaininggap/2)
        else: 
            localmax=min(heightdiff[i+1],heightdiff[i])
        maximum=max(localmax,maximum)
print(maximum)