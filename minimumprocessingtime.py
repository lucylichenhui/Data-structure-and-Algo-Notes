
"""
Test cases
[8,10] 
[2,2,3,1,8,7,4,5]
"""

x=input()
y=input()

y.sort()
i=0
mini=0
a=1
while i<len(y): 
    mini=max(y[i+3]+x[len(x)-a],mini)
    i+=4
    a+=1

print(mini)