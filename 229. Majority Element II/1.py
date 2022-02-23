def majorityElement(self, nums: List[int]) -> List[int]:
    ans = []
    m = defaultdict(int)
    for n in nums:
        m[n] = m[n] + 1
    
    n3 = len(nums)//3
    
    for k,v in m.items():
        if v > n3:
            ans.append(k)
    
    return ans
        