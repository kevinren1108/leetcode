from typing import List
      
def min_meeting_rooms(intervals: List[List]) -> int:
        # Write your code here
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        count = 0
        s,e = 0,0
        maxCount = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
                maxCount = max(maxCount,count)
            elif start[s] >= end[e]:
                e += 1
                count -= 1
        return maxCount





min_meeting_rooms([[2,15],[36,45],[9,29],[16,23],[4,9]])