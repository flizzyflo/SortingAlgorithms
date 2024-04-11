from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.colors.colorenum import ColorEnum
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class MergeSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas):
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()

        if self.sortingCanvas:
            # changing the bar color to green when search is complete and algorithm is used in tkinter gui.
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self):
        self.__mergesort(self.dataToSort, 0, len(self.dataToSort) - 1)

    def __mergesort(self, unsorted_array: List[int | float], leftIdx: int, rightIdx: int) -> None:

        # more than one element unsorted array
        if leftIdx < rightIdx:
            midIndex = (leftIdx + rightIdx) // 2

            # division of every array until it contains just one element
            self.__mergesort(unsorted_array, leftIdx, midIndex)
            self.__mergesort(unsorted_array, midIndex + 1, rightIdx)

            # merging elements together, but in place in original array
            self.__merge(unsorted_array, leftIdx, midIndex, rightIdx)

    def __merge(self, parentArray: List[int | float], leftIndex: int, middleIndex: int, rightIndex: int) -> None:

        leftHalf = parentArray[leftIndex:middleIndex + 1]

        # middle index + 1 to get first element of right half from parent array
        # right index + 1 to include first element of right half from parent array since the rightindex + 1 is not picked (not inclusive)
        # required, since its in place
        rightHalf = parentArray[middleIndex + 1: rightIndex + 1]
        leftHalfIdx, rightHalfIdx = 0, 0

        # parent array, start at index zero to replace first element
        parentArrayIdx = leftIndex

        # both pointers are within array bounds
        while leftHalfIdx < len(leftHalf) and rightHalfIdx < len(rightHalf):
            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(parentArrayIdx, ColorEnum.GREEN.value)

            # swap left value to parent array index position move to next element in left list
            if leftHalf[leftHalfIdx] <= rightHalf[rightHalfIdx]:
                parentArray[parentArrayIdx] = leftHalf[leftHalfIdx]
                leftHalfIdx += 1
                if self.sortingCanvas:
                    self.sortingCanvas.colorizeSingleDrawnRectangle(leftHalfIdx, ColorEnum.PURPLE.value)

            # swap right value to parent array index position move to next element in right list
            elif rightHalf[rightHalfIdx] < leftHalf[leftHalfIdx]:
                parentArray[parentArrayIdx] = rightHalf[rightHalfIdx]
                rightHalfIdx += 1
                if self.sortingCanvas:
                    self.sortingCanvas.colorizeSingleDrawnRectangle(rightHalfIdx, ColorEnum.PURPLE.value)

            parentArrayIdx += 1
            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(leftHalfIdx, ColorEnum.GREEN.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(rightHalfIdx, ColorEnum.PURPLE.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

        # append remainder of left list to parent array
        while leftHalfIdx < len(leftHalf):
            parentArray[parentArrayIdx] = leftHalf[leftHalfIdx]
            leftHalfIdx += 1
            parentArrayIdx += 1

            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(leftHalfIdx, ColorEnum.GREEN.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

        # append remainder of right list to parent array
        while rightHalfIdx < len(rightHalf):
            parentArray[parentArrayIdx] = rightHalf[rightHalfIdx]
            rightHalfIdx += 1
            parentArrayIdx += 1
            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(rightHalfIdx, ColorEnum.PURPLE.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
