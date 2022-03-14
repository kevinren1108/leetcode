from collections import Counter, defaultdict

def longestSubstring(s: str, k: int) -> int:
	
    if len(s) < k: return 0
    
    c = Counter(s)
    st = 0
    for p, v in enumerate(s):
        
        if c[v] < k:
            
            return max(longestSubstring(s[st:p],k), longestSubstring(s[p+1:],k))
    
    return len(s)

longestSubstring("ababcaabba",2)

# Follow up: Can you improve?:

# def longestSubstring(self, s, k):
#         if len(s) < k: return 0
        
#         dic = set(s)
#         st = 0

#         for ch in dic:
#             if s.count(ch) < k:
#                 return max(self.longestSubstring(t,k) for t in s.split(ch))
#         return len(s)