class MedianFinder:
    
    def __init__(self):
        #two heap: small,large
        #value: 2,3,4,5,6,7
        #max heap: [4,3,2] small[0] is the maxmen value in small heap
        #max heap ( python doesn't have max heap, so insert value time the val times -1)
        self.small = [] 
        #min heap: [5,6,7] large[0] is the smallest value in large heap
        #min heap
        self.large = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)
        
        #handle small heap[0] larger than large heap[0]
        if self.small and self.large and self.large[0] < (self.small[0] * -1):
            val = ( -1 * heappop(self.small))
            heappush(self.large, val)
         
        #handle not balance, [4,3,2,1] , [5,6]
        if len(self.small) > (len(self.large) + 1):
            val = ( -1 * heappop(self.small))
            heappush(self.large, val)
            
        #handle not balance, [2,1] , [3,4,5,6]    
        if (len(self.small) + 1) < len(self.large):
            val = heappop(self.large)
            heappush(self.small, (-1 * val))
           

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        
        if len(self.large) > len(self.small):
            return self.large[0]
    
        return (self.large[0] + (-1 * self.small[0])) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()