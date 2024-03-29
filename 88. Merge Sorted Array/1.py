def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    pos  = m + n -1
    m = m - 1
    n = n - 1
    
    
    while m >= 0 and n >= 0:
        if nums2[n] > nums1[m]:
            nums1[pos] = nums2[n]
            n -= 1
            pos -= 1
        else:
            nums1[pos] = nums1[m]
            m -= 1
            pos -= 1
    while n >= 0:
        nums1[pos] = nums2[n]
        n -= 1
        pos -= 1