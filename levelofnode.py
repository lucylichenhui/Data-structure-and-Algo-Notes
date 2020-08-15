

def nodelevel(root,key,level): 
    if root is None: 
        return -1

    if root.data==key: 
        return level
    
    l=nodelevel(root.left,key,level+1)
    if l!==1: 
        return l 
    return nodelevel(root.right,key,level+1)