from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class QuickSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)

    def sort(self):
        print("Quick Sort will be implemented here...")
