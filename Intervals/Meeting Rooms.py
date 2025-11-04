from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start
    
    def __eq__(self, other):
        return self.start == other.start


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort()
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
                
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canAttendMeetings([Interval(0,30),Interval(5,10),Interval(15,20)]))
    print(sol.canAttendMeetings([Interval(5,8),Interval(9,15),Interval(15,20)]))
    print(sol.canAttendMeetings([Interval(5,8)]))
    print(sol.canAttendMeetings([Interval(5,8),Interval(5,8)]))
    print(sol.canAttendMeetings([]))