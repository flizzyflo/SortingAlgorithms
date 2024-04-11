import random
from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class QuickSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()

        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self):
        MAX_IDX: int = len(self.dataToSort) - 1
        self.__quicksort(0, MAX_IDX)

    def __quicksort(self, left: int, right: int) -> None:

        if left >= right:
            return

        # returns the middle element to split the list at
        leftPointer = self.__partition(left, right)

        # partial arrays. left pointer is set to where it met the right pointer, thus this is the
        # new middle of the subcall array to sort
        self.__quicksort(left, leftPointer - 1)
        self.__quicksort(leftPointer + 1, right)

    def __partition(self, left: int, right: int) -> int:
        pivotIndex: int = right
        leftPointer: int = left
        rightPointer: int = right

        # outer loop per call, until pointers meet
        while leftPointer < rightPointer:

            if self.sortingCanvas:
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
                self.sortingCanvas.colorizeSingleDrawnRectangle(pivotIndex, ColorEnum.PURPLE.value)


            # iterate while either pointers meet or smaller or bigger element is found
            while leftPointer < rightPointer and self.dataToSort[leftPointer] <= self.dataToSort[pivotIndex]:
                leftPointer += 1

            while rightPointer > leftPointer and self.dataToSort[rightPointer] >= self.dataToSort[pivotIndex]:
                rightPointer -= 1

            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(leftPointer, ColorEnum.GREEN.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(rightPointer, ColorEnum.GREEN.value)

            # pointers point to numbers smaller / bigger than pivot -> switch
            # thus switch
            self.swap(leftIndex=leftPointer, rightIndex=rightPointer)
        # switch element of left pointer with pivot element
        self.swap(leftIndex=leftPointer, rightIndex=right)
        return leftPointer



