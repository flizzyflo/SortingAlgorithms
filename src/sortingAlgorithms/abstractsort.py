
from abc import abstractmethod, ABC
from typing import List

from src.userInterface.canvas.sortingcanvas import SortingCanvas


class AbstractSort(ABC):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas):
        self.dataToSort = dataToSort
        self.sortingCanvas = sortingCanvas

    @abstractmethod
    def sort(self) -> None:
        pass

    def __str__(self) -> str:
        return "!"

    def __repr__(self) -> str:
        return "!"