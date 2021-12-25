# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

def check_if_string_homogenic(string:str):
    for index in range(1,len(string)):
        if string[index-1]!=string[index]:
            return False
    return True
            
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # create moving window
        stack = []
        counter_stack = []
        for i in range(len(s)):
            if not stack or stack[-1]!=s[i]:
                stack.append(s[i])
                counter_stack.append(1)
            elif stack[-1] == s[i]:
                counter_stack[-1]+=1
            if counter_stack[-1] ==k: 
                counter_stack.pop()
                stack.pop()
        
        return "".join([stack[i]*counter_stack[i] for i in range(len(stack))])
                
            
