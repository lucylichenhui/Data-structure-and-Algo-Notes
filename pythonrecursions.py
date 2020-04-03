# Recursions 

#==========# 


#Palindromic partition problem


#utility function option2 
def ispalindrom(string): 
    # time complexity of this algorthim is O(n/2)
    if string[::1]==string: 
        return True


"""

#utility function option1 
def ispalindrom(string,high,low): 
    BOOL= True
    while low<high: 
        if string[low]==string[high]: 
            low+=1
            high-=1
        else: 
            BOOL=False
    return BOOL 

"""


sol=""

def partition(string,a=0): 
    global sol
    if string is not None:


        for i in range(len(string)): 
            for j in range(a,len(string)+1): 
                if i==j: 
                    substring=string[i]
                else:  
                    substring=string[i:j]


                if substring: 
                    if ispalindrom(string): 
                        sol=sol+substring+" "
                        
                        string=string[a+1:len(string)]
                        a+=1
                        print(a)
                        partition(string)
                        print(sol) 
                        sol=""   # forgot to reinitialize sol            



partition("nitin")




