def majorityElement(self, nums: List[int]) -> int:
    m = defaultdict(int)
    for n in nums:
        m[n] = m[n] + 1
        if m[n] > len(nums)//2:
            return n