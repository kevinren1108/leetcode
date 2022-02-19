from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    count = 0
    i = 0
    prev = flowerbed[0]
    next = 0
    while i < len(flowerbed):
        if i + 1 < len(flowerbed):
            next = flowerbed[i+1]
        if prev == 0 and next == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            count += 1
            i += 2
        elif prev == 0 and i+1 == len(flowerbed) and flowerbed[i] == 0:
            flowerbed[i] = 1
            count += 1
            i += 2
        else:
            i += 1
            prev = flowerbed[i-1]

    print(flowerbed, count)
    if count >= n:
        return True
    return False

canPlaceFlowers([0,0,1,0,1], 2)