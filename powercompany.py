
#Power company, greedy
"""
Sample input for custom testing

7
7
10
1
2
7
7
1

"""

import math
import operator
from collections import defaultdict
generators=input()
num=math.ceil(float(generators)/2)
d=defaultdict(int)
for i in range(generators): 
    d[input()]+=1
final=0
d = sorted(d.items(), key=operator.itemgetter(1))
while int(num)>0:
    maxiumumvalue=d[len(d)-1]
    a,b=maxiumumvalue
    num-=b
    d.pop()
    final+=1
print(final)



    
