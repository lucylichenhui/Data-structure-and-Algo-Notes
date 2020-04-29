

""" 
Euclidean algorithm
"""

a=10
b=20

def compare(a,b)
    if a>b: 
        return gdc(a,b)
    else: 
        return gdc(b,a)

def gdc(num,remainder): 
    if remainder==0: 
        return num
    return gdc(num,num%remainder)

""" 
Fast modular exponentiation
"""
A=4
B=5 
C=3

def fme(A,B,C): 
    if powerofTwo==0: 
        return None 
    powerofTwo=B/2 
    while powerofTwo>0: 
        powerofTwo-=1
        A=(A%C)*(A%C)%C
        return A 

"""
LC medium 29 Divide 2 integers 
"""
def d2int():
    quotient=0 
    while dividend>=divisor: 
        powerofTwo=1
        value=quotient
        while value+value<dividend: 
            value+=value
            powerofTwo+=powerofTwo
        quotient+=powerofTwo
        dividend-=value
    return quotient





