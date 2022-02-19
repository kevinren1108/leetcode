from typing import List


def candy( ratings: List[int]) -> int:
    res = [1] * len(ratings)

    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            res[i] = res[i-1] + 1

    for j in range(len(ratings)-1,0,-1):
        if ratings[j] < ratings[j-1]:
            res[j-1] = max(res[j-1], res[j] + 1)

    result = 0
    for val in res:
        result += val
    
    return result