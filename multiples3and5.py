
# Akuna 
# find numbers taking the form of 3^n*5^m between 2 numbers

x=input()
y=input()
x=int(x)
y=int(y)

ycopy=y
ycopy1=y
m=0
#Find max n and m
while y>=5: 
    y=y/5
    m+=1
n=0
while ycopy>=3:
    ycopy=ycopy/3
    n+=1

y=ycopy1

sum=0
stack=[]
for a in range(n+1): 
    for b in range(m+1): 
        #print(3**a*5**b)
        if 3**a*5**b>=x and 3**a*5**b<y: 
            sum+=3**a*5**b
            stack.append(3**a*5**b)
        if 3**a*5**b>=y:
            break
print(stack)
print(sum)