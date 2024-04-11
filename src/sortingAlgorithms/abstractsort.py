
from abc import abstractmethod, ABC
from typing import List

from src.userInterface.canvas.sortingcanvas import SortingCanvas


class AbstractSort(ABC):

    def __init__(self, *, dataToSort: List[int] | List[float], sortingCanvas: SortingCanvas | None):
        self.dataToSort = dataToSort
        self.sortingCanvas = sortingCanvas

    @abstractmethod
    def sort(self) -> None:
        pass

    def swap(self, *, leftIndex: int, rightIndex: int) -> None:
        leftVal = self.dataToSort[leftIndex]
        rightVal = self.dataToSort[rightIndex]

        self.dataToSort[rightIndex] = leftVal
        self.dataToSort[leftIndex] = rightVal
