def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #k = k % len(nums)

    # use array to store the index of element into a dictionary
    numDic = defaultdict(list)
    for i in range(len(nums)):
        numDic[nums[i]].append(i)
        
    for key,v in numDic.items():
        if len(v) >= 2:
            for i in range(1,len(v)):
                if (v[i] - v[i-1]) <= k:
                    return True
    return False