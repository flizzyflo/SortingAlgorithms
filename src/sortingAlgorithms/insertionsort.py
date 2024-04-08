from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.colors.colorenum import ColorEnum
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class InsertionSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()

    def sort(self) -> None:
        """Implementation of insertion sort. This approach compares a value with the former value. If the former value
       is bigger than the current value, both are swapped. This algorithm works in-place and is stable."""

        if len(self.dataToSort) == 0:
            return

        for forwardCounter, currentValue in enumerate(self.dataToSort, 1):

            backwardCounter = forwardCounter - 1

            while backwardCounter >= 0:

                if self.dataToSort[backwardCounter] > currentValue:
                    # if current value is smaller than the former value, swap both.

                    self.dataToSort[backwardCounter], self.dataToSort[backwardCounter + 1] = currentValue, self.dataToSort[backwardCounter]

                    if self.sortingCanvas:
                        # updates the GUI, according to the current values of the values list, if used in visualization.
                        self.sortingCanvas.colorizeSingleDrawnRectangle(backwardCounter, ColorEnum.PURPLE.value)
                        self.sortingCanvas.colorizeSingleDrawnRectangle(backwardCounter + 1, ColorEnum.ORANGE.value)

                        self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

                backwardCounter -= 1

        if self.sortingCanvas:
            self.sortingCanvas.endSearch(self.dataToSort)
