def length_of_longest_substring_k_distinct(s: str, k: int) -> int:

    if k == 0 or len(s) == 0:
        return 0

    seen = set()
    
    l = 0
    r = 0
    size = 0

    while r < len(s):
        if s[r] not in seen:
            seen.add(s[r])
        r += 1
        while len(seen) > k:
            seen.remove(s[l])
            l += 1
        
        size = max(size,r-l)
    
    return size

length_of_longest_substring_k_distinct("eceba",3)