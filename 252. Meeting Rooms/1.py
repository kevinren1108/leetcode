def can_attend_meetings(self, intervals: List[Interval]) -> bool:
    # Write your code here
    intervals.sort(key = lambda x: x.start)
    #print(intervals)
    n = len(intervals)
    for i in range(0,n-1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True 