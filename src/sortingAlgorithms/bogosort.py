import copy
from typing import List
import random
from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class BogoSort(AbstractSort):

    def __init__(self, dataToSort: List[int], sortingCanvas: SortingCanvas, *args, **kwargs) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sortedData = sorted(copy.copy(dataToSort))
        self.sort()

    def sort(self) -> None:

        while self.dataToSort != self.sortedData:
            random.shuffle(self.dataToSort)
            indexToColorize = random.randint(0, len(self.dataToSort) - 1)
            self.sortingCanvas.colorizeSingleDrawnRectangle(indexToColorize, ColorEnum.PURPLE.value)
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
        self.sortingCanvas.endSearch(self.dataToSort)
