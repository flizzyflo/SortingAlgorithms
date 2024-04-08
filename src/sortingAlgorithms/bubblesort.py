from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.colors.colorenum import ColorEnum
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class BubbleSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()

    def sort(self) -> None:

        """Implementation of bubble sort. This sorting algorithm grabs a number and switches it with the next number, if the next one is less. The grabed number
        "marches" through the list until a number bigger than itself is found. With this bigger number, the process repeats again Finally, the biggest number
        is at the end of the array and the process is repeated until the whole array is sorted. This algorithm works in-place and is stable."""

        if len(self.dataToSort) == 0:
            return

        for run in range(len(self.dataToSort)):
            # overall run through the entire values array

            for currentIndex, currentValue in enumerate(self.dataToSort):

                if (currentIndex + 1) > len(self.dataToSort) - 1:
                    continue

                if currentValue > self.dataToSort[currentIndex + 1]:
                    # If next value is smaller than current value, swap both.

                    temporary_object: int = self.dataToSort[currentIndex + 1]
                    self.dataToSort[currentIndex + 1] = currentValue
                    self.dataToSort[currentIndex] = temporary_object

                    if self.sortingCanvas:
                        self.sortingCanvas.colorizeSingleBar(currentIndex, ColorEnum.GREEN.value)
                        self.sortingCanvas.colorizeSingleBar(currentIndex + 1, ColorEnum.PURPLE.value)
                        # updates the GUI, according to the current values of the values list, if used in visualization.
                        self.sortingCanvas.createRectangles(self.dataToSort)

                else:
                    continue

        if self.sortingCanvas:
            # changing the bar color to green when search is complete and algorithm is used in tkinter gui.
            self.sortingCanvas.endSearch(self.dataToSort)
