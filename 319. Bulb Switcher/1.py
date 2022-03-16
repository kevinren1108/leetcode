def bulbSwitch(n: int) -> int:
    bulb = [True] * (n)
    distance = 2
    for i in range(1,n-1):
        temp = i
        while temp < n:
            bulb[temp] = not bulb[temp]
            temp += distance
            
        distance += 1
        
    print(bulb)

bulbSwitch(12)