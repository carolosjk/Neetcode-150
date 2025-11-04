from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> bool:
        start_times = sorted(i.start for i in intervals)
        end_times = sorted(i.end for i in intervals)

        max_count = count = 0
        si = ei = 0

        while si < len(start_times):
            if start_times[si] < end_times[ei]:
                count += 1
                max_count = max(max_count,count)
                si += 1
            else:
                count -= 1
                ei += 1

        return max_count








if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([Interval(0,30),Interval(5,10),Interval(15,20)]))
    print(sol.minMeetingRooms([Interval(5,8),Interval(9,15),Interval(15,20)]))
    print(sol.minMeetingRooms([Interval(5,8)]))
    print(sol.minMeetingRooms([Interval(5,8),Interval(5,8)]))
    print(sol.minMeetingRooms([]))