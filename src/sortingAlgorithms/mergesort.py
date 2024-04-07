from typing import List

from src.userInterface.colorenum import ColorEnum
from src.userInterface.sortingcanvas import SortingCanvas


class MergeSort:

    def __init__(self, valuesToSort: List[int], sortingCanvas: SortingCanvas):
        self.valuesToSort = valuesToSort
        self.sortingCanvas = sortingCanvas
        self.sort(self.valuesToSort, 0, len(self.valuesToSort) - 1)

        if self.sortingCanvas:
            # changing the bar color to green when search is complete and algorithm is used in tkinter gui.
            self.sortingCanvas.endSearch(self.valuesToSort)

    def sort(self, unsorted_array: List[int | float], leftIdx: int, rightIdx: int) -> None:

        # one element or empty array
        if leftIdx < rightIdx:
            midIndex = (leftIdx + rightIdx) // 2

            self.sort(unsorted_array, leftIdx, midIndex)
            self.sort(unsorted_array, midIndex + 1, rightIdx)
            self.merge(unsorted_array, leftIdx, midIndex, rightIdx)
            self.sortingCanvas.createRectangles(self.valuesToSort)

    def merge(self, parentArray: List[int | float], leftIndex: int, middleIndex: int, rightIndex: int) -> None:

        leftHalf = parentArray[leftIndex:middleIndex + 1]
        rightHalf = parentArray[middleIndex + 1: rightIndex + 1]

        leftHalfIdx, rightHalfIdx = 0, 0
        parentArrayIdx = leftIndex

        while leftHalfIdx < len(leftHalf) and rightHalfIdx < len(rightHalf):

            self.sortingCanvas.colorizeSingleBar(parentArrayIdx, ColorEnum.GREEN.value)
            self.sortingCanvas.colorizeSingleBar(rightHalfIdx, ColorEnum.PURPLE.value)

            if leftHalf[leftHalfIdx] <= rightHalf[rightHalfIdx]:

                parentArray[parentArrayIdx] = leftHalf[leftHalfIdx]
                leftHalfIdx += 1

            elif rightHalf[rightHalfIdx] < leftHalf[leftHalfIdx]:
                parentArray[parentArrayIdx] = rightHalf[rightHalfIdx]
                rightHalfIdx += 1
            parentArrayIdx += 1

            self.sortingCanvas.colorizeSingleBar(parentArrayIdx, ColorEnum.GREEN.value)
            self.sortingCanvas.colorizeSingleBar(rightHalfIdx, ColorEnum.PURPLE.value)
            self.sortingCanvas.createRectangles(self.valuesToSort)

        while leftHalfIdx < len(leftHalf):
            parentArray[parentArrayIdx] = leftHalf[leftHalfIdx]
            leftHalfIdx += 1
            parentArrayIdx += 1
            self.sortingCanvas.colorizeSingleBar(leftHalfIdx, ColorEnum.GREEN.value)

            self.sortingCanvas.createRectangles(self.valuesToSort)

        while rightHalfIdx < len(rightHalf):
            parentArray[parentArrayIdx] = rightHalf[rightHalfIdx]
            rightHalfIdx += 1
            parentArrayIdx += 1
            self.sortingCanvas.colorizeSingleBar(rightHalfIdx, ColorEnum.PURPLE.value)
            self.sortingCanvas.createRectangles(self.valuesToSort)
