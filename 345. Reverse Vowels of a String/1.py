
def reverseVowels(s: str) -> str:
    vow = []
    newS = ""
    v  = set(list(["a","e","i","o","u","A","E","I","O","U"]))
    for i in range(len(s)):
        if s[i] in v:
            newS += "0"
            vow += [s[i]]
        else:
            newS += s[i]
    ans = ""  
    count = 1
    for i in range(len(newS)):
        if newS[i] != "0":
            ans += newS[i]
        else:
            ans += vow[-count]
            count += 1
            
    return ans

reverseVowels("Live on evasions? No, I save no evil.")