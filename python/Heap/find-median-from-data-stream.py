# https://leetcode.com/problems/find-median-from-data-stream/submissions/

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_ = []

    def addNum(self, num: int) -> None:
        self.list_.append(num)
        self.list_.sort()

    def findMedian(self) -> float:
        if len(self.list_) % 2 == 0:
            return ( self.list_[len(self.list_)//2] + self.list_[(len(self.list_)//2) - 1] ) / 2
        else:
            return self.list_[len(self.list_)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()