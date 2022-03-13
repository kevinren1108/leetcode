from collections import deque


def addBinary( a: str, b: str) -> str:
    haveA = True
    haveB = True
    
    p = -1
    ans = deque()
    carr = "0"
    while p > -max(len(a),len(b))-1:
        if -p > len(a):
            haveA = False
        if -p > len(b):
            haveB = False
        
        valA,valB = '0','0'
        
        if haveA:
            valA = a[p]
        if haveB:
            valB = b[p]
        
        print(valA,valB)
        
        p -= 1

addBinary("1010","1011")