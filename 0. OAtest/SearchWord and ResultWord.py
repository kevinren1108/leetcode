import string

def word(search:string, result:string)->int:
    res = 0
    schPointer = 0
    resPointer = 0

    while schPointer < len(search) and resPointer < len(result):
        if search[schPointer] == result[resPointer]:
            schPointer += 1
            resPointer += 1
        else:
            schPointer += 1
    res = len(result) - resPointer
    print(res)   
    return res

word("armaze", "amazon")
