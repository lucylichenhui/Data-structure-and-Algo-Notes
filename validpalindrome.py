
def isPalindrome(s):
    list1=[]
    for i in s: 
        if i.isalnum(): 
            list1.append(i.lower())
            
    list2=list1.copy()
    list2.reverse()
            
    if list1==list2: 
        return print("true")
    else: 
        return print("false")
    

isPalindrome("race a car")