class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        setofintervals=set()
        for i in intervals: 
            a, b=i[0],i[1]
            temp=range(i[0], i[1])
            if len(set.intersection(set(range(i[0], i[1])),setofintervals))!=0:
                return False
            setofintervals.update(range(a,b))
        return True

from collections import deque 
