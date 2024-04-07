from typing import List

from src.sortingAlgorithms.createRandomArray import createRandomArray
from src.userInterface.colorenum import ColorEnum
from src.userInterface.sortingcanvas import SortingCanvas


class RadixSort:

    def __init__(self, valuesToSort: List[int], sortingCanvas: SortingCanvas):
        self.valuesToSort = valuesToSort
        self.sortingCanvas = sortingCanvas
        self.bucketContainer: dict[int, List[int]] = dict()
        self.maxNumberLength = len(str(max(valuesToSort)))
        self.sort()

    def sort(self) -> None:
        self.prepareBuckets()

        numberPositionIndex: int = self.maxNumberLength - 1

        # as long as not first position is reached
        while numberPositionIndex >= 0:

            for numberToSortIntoBucket in self.valuesToSort:
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
            self.sortingCanvas.createRectangles(self.valuesToSort)
            self.sortingCanvas.endSearch(self.valuesToSort)

    def addToBucket(self, numberAtCurrentNumberPosition: int, totalNumber: int) -> None:
        self.bucketContainer[numberAtCurrentNumberPosition].append(totalNumber)

    def putBucketsToBaseList(self) -> None:
        originalArrayIndexer: int = 0

        for bucket in self.bucketContainer.values():
            for number in bucket:
                self.valuesToSort[originalArrayIndexer] = number

                # visualisation
                if self.sortingCanvas:
                    self.sortingCanvas.colorizeSingleBar(originalArrayIndexer, ColorEnum.GREEN.value)
                    self.sortingCanvas.createRectangles(self.valuesToSort)
                originalArrayIndexer += 1

    def clearBuckets(self) -> None:
        [bucket.clear() for bucket in self.bucketContainer.values()]

    def prepareBuckets(self) -> None:
        for bucketNumber in range(10):
            self.bucketContainer[bucketNumber] = []
