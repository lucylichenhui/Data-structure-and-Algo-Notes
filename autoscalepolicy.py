"""
Sample input for custom testing

1
3
5
10
80
"""

averageutil=[]
instance=input()
num=input()
for i in range(num): 
    averageutil.append(input())
for i in range(len(averageutil)): 
    if averageutil[i]>60 and instance*2<=2*10**8: 
        instance=instance*2
    elif averageutil[i]<25 and instance/2>1: 
        instance=instance/2

print(instance)
