#150. Evaluate Reverse Polish Notation

def isoperand(i): 
    if i=="*" or i=="+" or i=="-" or i=="/": 
        return True 
def calc(i,a,b): 
    if i=="*": 
        s=a*b
    if i=="+": 
        s=a+b 
    if i=="-":
        s=b-a
    if i=="/":
        s=b/a
    return s
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack=[] 
    for i in tokens: 
        if not isoperand(i): 
            stack.append(i)
        if isoperand(i): 
            a=int(stack.pop())
            b=int(stack.pop())
            res=calc(i,a,b)
            stack.append(res)
    if len(stack)==1: 
        for e in stack: 
            print(e)
            return e


evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
        
# a more elegant solution


op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: int(x / y)}

class Solution(object):
    def evalRPN(self, tokens):

        num_stack = []
        for t in tokens:
            if len(t) > 1 or t.isdigit():
                num_stack.append(int(t))
            else:
                b = num_stack.pop()
                a = num_stack.pop()
                num_stack.append(op[t](a, b))
        return num_stack[0]


#http://csis.pace.edu/~wolf/CS122/infix-postfix.htm