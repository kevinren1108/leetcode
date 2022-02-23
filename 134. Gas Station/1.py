def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    tripTank,currTank,start,n = 0,0,0,len(gas) 
    for i in range(n):
        tripTank += gas[i] - cost[i]
        currTank += gas[i] - cost[i]
        print(tripTank,currTank)
        if currTank < 0:
            start = i + 1
            currTank = 0
        
    if tripTank >= 0:
        return start
    else:
        return -1