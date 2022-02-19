
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    total = 0

    prev = intervals[0][1]
    for i in range(1,len(intervals)):
        if prev > intervals[i][0]:
            total += 1
        else:
            prev = intervals[i][0]
            
    return total

eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])