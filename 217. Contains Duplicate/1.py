def containsDuplicate(self, nums: List[int]) -> bool:
    numDic = defaultdict(int)
    for i in nums:
        numDic[i] = numDic[i] + 1
    
    for k,v in numDic.items():
        if v >= 2:
            return True
        
    return False