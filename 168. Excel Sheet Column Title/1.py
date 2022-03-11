
def convertToTitle(columnNumber: int) -> str:
    arr = ""

    while columnNumber > 0:
        rem = (columnNumber-1) % 26
        ch = chr(rem + 65)
        arr += ch
        columnNumber = (columnNumber - 1) // 26

    
    ans = ""
    
    for i in range(len(arr)-1,-1,-1):
        ans += arr[i]
    
    return ans


convertToTitle(701)