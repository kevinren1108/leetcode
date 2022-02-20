import math
from typing import List


def findMinArrowShots( points: List[List[int]]) -> int:
    
    points.sort(key=lambda x: x[0])
    cur_end = -math.inf
    count = 0

    for start,end in points:
        if cur_end >= start:
            cur_end = min(cur_end,end)
        else:
            count += 1
            cur_end = end

    
            
    return count


findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])


#[10,16],[2,8],[1,6],[7,12]


#           1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18

#[1,6]      -   -   -   -   -   -
#[2,8]          -   -   -   -   -   -   -
#[7,12]                             -   -   -   -   -   -
#[10,16]                                        -   -   -   -   -   -   -


# for element1 -> [1,6] and element2 -> [2,8]
# we can tell that:

# since element1[1](6) > element2[0](2), we know that element1 and element2 are overlaped.    
#             
# if we find a overlaped, we can try next element in the array, which is element3[7,12], we check element e3[0] and e1[1], 
# we find that 7 > 6, which is means e1 and e3 is not overlaped. 
# so we dequeue e1 and e2, and increse our count by 1
