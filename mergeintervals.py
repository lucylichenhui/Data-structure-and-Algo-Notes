
#attempt 1 
 def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #want index of merged lists, return merged lists 
        d=deque(interval)
        y=True 
        while y: 
            curr=d[0]
            a,b=curr[0], curr[1]
            for i in d[1:]: 
                c, d=i[0], i[1]
                y=False
                if len(set.intersection(set(range(a,b)),set(range(c,d))))!=0 or c==b or d==a:
                    """

                    if c<b: 
                        a=a 
                        b=d
                    elif a<d: 
                        a=c
                        b=b
                    elif c==b: 
                        a=a 
                        b=d
                    elif d==a: 
                        a=c
                        b=b

                    """
                    a=min(a,c)
                    b=max(d,b)
                    y=True
                    d.popleft()
                    d.append([a,b])
            print(d)
            return d
        
#attempt 2 

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #want index of merged lists, return merged lists 
        if not intervals : 
            return []
        deq=deque(intervals)
        y=True 
        while y: 
            
            curr=deq[0]
            print(curr)
            a,b=curr[0], curr[1]
            deque_slice = collections.deque(itertools.islice(deq, 1,len(deq)))
            y=False
            z=True
            i=0
            while i<len: 
                
            for i in range(len(deque_slice)): 
                c, d=deque_slice[i][0], deque_slice[i][1]
                if len(set.intersection(set(range(a,b)),set(range(c,d))))!=0 or c==b or d==a:
                    a=min(a,c)
                    b=max(d,b)
                    y=True
                    print(deq)
                    print(deque_slice)
                    print(deque_slice[i])
                    print(i)
                    del deq[i+1]
                    del deque_slice[i]
                    deq.popleft()
                    deq.append([a,b])
                    
        return(list(deq))


#final try yields correct solution
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #want index of merged lists, return merged lists 
        if not intervals : 
            return []
        
        n=sorted(intervals, key=lambda x: x[0])
        #merged=[n[0]]
        merged=[]
        for i in n: 
            if not merged or merged[-1][1]<i[0]: 
                merged.append(i)
                
            else: 
                merged[-1][1]=max(merged[-1][1],i[1])
            
        return merged
                