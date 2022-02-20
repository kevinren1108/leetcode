from typing import List


def removeCoveredIntervals(intervals: List[List[int]]) -> int:

    cover = 0
    intervals.sort(key = lambda x:(x[0], -x[1]))   ## sort by element1, if element1 are equal, sort by element2 and reverse this pair

    maxRight = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][1] <= maxRight:
            cover += 1
        else:
            maxRight = intervals[i][1]
    return len(intervals) - cover



    
removeCoveredIntervals([[1,4],[3,6],[2,8]])


#         1   2   3   4   5   6   7   8
# [1,4]   -   -   -   -
# [2,8]       -   -   -   -   -   -   -      
# [3,6]           -   -   -   -

#because the list is already sorted in increased order, so the preverse element's left most will must cover current elemnet's left most
#then we only need to know if the current right most is smaller than preverse right most element


