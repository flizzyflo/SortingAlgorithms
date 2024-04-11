
from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.colors.colorenum import ColorEnum
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class RadixSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas):
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.bucketContainer: dict[int, List[int]] = dict()
        self.maxNumberLength = len(str(max(self.dataToSort)))
        self.sort()

    def sort(self) -> None:
        self.prepareBuckets()

        numberPositionIndex: int = self.maxNumberLength - 1

        # as long as not first position is reached
        while numberPositionIndex >= 0:

            for numberToSortIntoBucket in self.dataToSort:
                currentNumberAsString = str(numberToSortIntoBucket)
                currentNumberAsString = currentNumberAsString.zfill(self.maxNumberLength)

                bucketNumberAsString = currentNumberAsString[numberPositionIndex]
                bucketNumber = int(bucketNumberAsString)

                self.addToBucket(bucketNumber, numberToSortIntoBucket)

            self.putBucketsToBaseList()
            self.clearBuckets()

            numberPositionIndex -= 1

        self.putBucketsToBaseList()
        self.clearBuckets()
        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            self.sortingCanvas.endSearch(self.dataToSort)

    def addToBucket(self, numberAtCurrentNumberPosition: int, totalNumber: int) -> None:
        self.bucketContainer[numberAtCurrentNumberPosition].append(totalNumber)

    def putBucketsToBaseList(self) -> None:
        originalArrayIndexer: int = 0

        for bucket in self.bucketContainer.values():
            for number in bucket:
                self.dataToSort[originalArrayIndexer] = number

                # visualisation
                if self.sortingCanvas:
                    self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
                    self.sortingCanvas.colorizeSingleDrawnRectangle(originalArrayIndexer, ColorEnum.GREEN.value)

                originalArrayIndexer += 1

    def clearBuckets(self) -> None:
        [bucket.clear() for bucket in self.bucketContainer.values()]

    def prepareBuckets(self) -> None:
        for bucketNumber in range(10):
            self.bucketContainer[bucketNumber] = []

