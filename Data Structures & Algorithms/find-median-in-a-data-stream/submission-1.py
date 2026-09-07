class MedianFinder:

    def __init__(self):
        self.median = None
        self.numList = []

    def addNum(self, num: int) -> None:
        self.numList.append(num)
        self.numList.sort()
        n = len(self.numList)
        mid = n // 2

        if n % 2 == 0:
            self.median = (self.numList[mid] + self.numList[mid - 1]) / 2
        else:
            self.median = self.numList[mid]

    def findMedian(self) -> float:
        return self.median
        