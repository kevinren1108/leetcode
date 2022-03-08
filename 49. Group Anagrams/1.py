from collections import defaultdict
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    dic = defaultdict(list)
    ans = []
    
    for w in strs:
        dic["".join(sorted(w))].append(w)
    
    for key,value in dic.items():
        ans.append(value)
        
    return ans