def isPowerOfTwo(self, n: int) -> bool:
    binStr = bin(n)
    binStr = binStr[2:]
    print(binStr)
    
    if binStr == "1":
        return True
    if binStr[0] == "1" and int(binStr[1:]) == 0:
        return True
    return False