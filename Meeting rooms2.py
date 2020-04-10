#my solution is inefficient as it is an O(n)^2 solution 

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals: 
            return 0
        count=0
        l=[set()] 
        n=sorted(intervals, key=lambda x: x[0])
        for i in intervals: 
            check=False
            a,b=i
            for e in l: #l is a list of sets
                if len(set.intersection(set(range(a,b)),e))==0: #if there is no overlap
                    e.update(set(range(a,b)))
                    check=True
                    break 
            
            if not check:
                l.append(set(range(a,b)))
                count+=1
        count+=1
        return count