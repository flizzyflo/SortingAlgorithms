import copy
from typing import List

from src.numbergenerator.createrandomnumbers import create_random_numbers
from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class QuickSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()

        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            # changing the bar color to green when search is complete and algorithm is used in tkinter gui.
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self):
        MAX_IDX: int = len(self.dataToSort) - 1
        self.__quicksort(0, MAX_IDX)

    def __quicksort(self, left: int, right: int) -> None:
        if left < right:
            pivotElement: int = self.__divide(left, right)
            self.__quicksort(left, pivotElement - 1)
            self.__quicksort(pivotElement + 1, right)

    def __divide(self, left: int, right: int) -> int:

        pivotElement: int = right
        self.sortingCanvas.colorizeSingleDrawnRectangle(pivotElement, ColorEnum.PURPLE.value)

        while left < right - 1:

            # iterate over left half until element smaller than pivot element is found
            while left < right and self.dataToSort[left] < self.dataToSort[pivotElement]:
                left += 1

            while right > left and self.dataToSort[right] >= self.dataToSort[pivotElement]:
                right -= 1

            if self.dataToSort[left] > self.dataToSort[right]:
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

                self.sortingCanvas.colorizeSingleDrawnRectangle(left, ColorEnum.ORANGE.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(right, ColorEnum.YELLOW.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(pivotElement, ColorEnum.PURPLE.value)
                self.swap(leftIndex=left, rightIndex=right)

           # self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

        if self.dataToSort[left] > self.dataToSort[pivotElement]:
            self.swap(leftIndex=left, rightIndex=right)

        else:
            left = right

        self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

        return left

