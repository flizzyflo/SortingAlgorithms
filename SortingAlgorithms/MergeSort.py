import math
from typing import List

class MergeSort:

    def __init__(self, rawValues: List[int], createRectangles):
        self.rawValues = rawValues
        self.createRectangles = createRectangles
        self.sort(self.rawValues)

    def sort(self, unsorted_array: List[int | float]) -> None:

        midIndex: int = len(unsorted_array) // 2

        if len(unsorted_array) < 2:
            return

        leftLow = 0
        leftHigh = midIndex
        rightLow = midIndex
        rightHigh = len(unsorted_array) - 1

        leftArray = unsorted_array[:midIndex]
        rightArray = unsorted_array[midIndex:]

        self.sort(leftArray)
        self.sort(rightArray)
        self.merge(unsorted_array, leftArray, rightArray)

    def merge(self, parentArray, leftHalf, rightHalf) -> None:

        #self.createRectangles(self.rawValues)
        leftHalfIdx, rightHalfIdx, parentArrayIdx = 0, 0, 0

        while leftHalfIdx < len(leftHalf) and rightHalfIdx < len(rightHalf):
            #self.createRectangles(self.rawValues)
            if leftHalf[leftHalfIdx] <= rightHalf[rightHalfIdx]:
                parentArray[parentArrayIdx] = leftHalf[leftHalfIdx]
                leftHalfIdx += 1

            elif rightHalf[rightHalfIdx] < leftHalf[leftHalfIdx]:
                parentArray[parentArrayIdx] = rightHalf[rightHalfIdx]
                rightHalfIdx += 1
            parentArrayIdx += 1


        while leftHalfIdx < len(leftHalf):
            parentArray[parentArrayIdx] = leftHalf[leftHalfIdx]
            leftHalfIdx += 1
            parentArrayIdx += 1
            #self.createRectangles(self.rawValues)

        while rightHalfIdx < len(rightHalf):
            parentArray[parentArrayIdx] = rightHalf[rightHalfIdx]
            rightHalfIdx += 1
            parentArrayIdx += 1

            #self.createRectangles(self.rawValues)
