class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        from heapq import heappush, heappop, heapreplace, heapify
        if intervals==[]: 
            return 0
        rooms=[]
        heapify(rooms)
        intervals.sort(key=lambda x:x[0])
        heappush(rooms,intervals[0][1])
        for i in intervals[1:]: 
            if rooms[0]<=i[0]: 
                heappop(rooms)
            heappush(rooms,i[1])
        return len(rooms)