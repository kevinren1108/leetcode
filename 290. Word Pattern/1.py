
def wordPattern( pattern: str, s: str) -> bool:
    pMap, sMap = {}, {}
    s = s.split(" ")
    if len(pattern) != len(s):
        return False
    
    for i in range(len(pattern)):
        if pMap.get(pattern[i], -1) != sMap.get(s[i], -1):
            return False
        pMap[pattern[i]] = sMap[s[i]] = i

            
    return True

wordPattern("abba","dog cat cat fish")