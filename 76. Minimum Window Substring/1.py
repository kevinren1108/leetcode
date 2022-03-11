from collections import Counter
from math import inf


def minWindow(s: str, t: str) -> str:
    if t == "" : return ""
  
    need = Counter(t)
    have = {}
    for n in t:
        have[n] = 0

    l,r = 0, 0
    needCount, haveCount = len(need),0
    ans = ""


    size = float(inf)
    while r < len(s):
        if s[r] in need:
            have[s[r]] += 1
            if have[s[r]] == need[s[r]]:
                haveCount += 1
        r += 1

        while needCount == haveCount:
            if s[l] in have:
                have[s[l]] -= 1
                if have[s[l]] < need[s[l]]:
                    haveCount -= 1
            if (r - l + 1) < size:
                ans = s[l:r]
                size = len(ans)
            l += 1


    return ans 

minWindow("cabwefgewcwaefgcf","cae")

# import collections


# def minWindow( s, t):
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]

# s = "ADOBECODEBANC"
# t = "ABC"

# minWindow(s,t)