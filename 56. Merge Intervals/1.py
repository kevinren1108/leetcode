from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key =lambda x: x[0])
    merged =[]
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged

    
    
# intervals [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals.sort [[1, 3], [2, 6], [8, 10], [15, 18]]

# interval = [1,3]
# merged =[]
# not merged:
# 	merged =[ [1,3] ]

# interval =[2,6]
# merged = [ [1,3] ]
# merged[-1][1] = 3 > interval[0] = 2:
# 	merged[-1][1] = max(merged[-1][1] = 3 ,interval[1] = 6) =6
# merged = [[1,6]]