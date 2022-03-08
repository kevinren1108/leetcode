def strToArr(s: str):
    ans = []
    temp = ""
    for i, ch in enumerate(s):
        if ch != " " :
            temp += ch
        elif len(temp) > 0:
            
            ans.append(temp)
            temp = ""

    if len(temp) > 0:
        ans.append(temp) 
    return ans

strToArr("the sky is blue")