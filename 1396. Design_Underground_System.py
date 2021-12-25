# https://leetcode.com/problems/design-underground-system

from collections import defaultdict 
class UndergroundSystem:

    def __init__(self):
        #"customer-id":"Waterloo" -> defaultdict: list
        self.station_in = defaultdict(list)
        #"Customer-ID":"Time-IN"
        self.time_in = defaultdict(int)
        self.total_time = defaultdict(lambda:[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.station_in[id].append(stationName)
        self.time_in[id] = t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_in = self.station_in.pop(id)
        time_in = self.time_in.pop(id)
        self.total_time[(station_in,stationName)][0] += (t - time_in)
        self.total_time[(station_in,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.journey[(startStation,endStation)]
        return total_time / total_trips
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
