def twoSum(numbers: List[int], target: int) -> List[int]:
    if len(numbers) == 2:
        return [1,2]
    l = 0
    r = len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1,r+1]
        if sum < target:
            l += 1
        else:
            r -= 1
    