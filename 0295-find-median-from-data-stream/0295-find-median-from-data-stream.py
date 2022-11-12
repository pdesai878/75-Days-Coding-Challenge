class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.count=0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.count+=1
        

    def findMedian(self) -> float:
        self.arr.sort()
        if self.count&1:
            return self.arr[self.count//2]
        m1=self.arr[self.count//2-1]
        m2=self.arr[self.count//2]
        return m1+(m2-m1)/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()