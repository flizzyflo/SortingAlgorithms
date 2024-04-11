from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class HeapSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()
        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self) -> None:
        # max index for heapification
        totalElementCount: int = len(self.dataToSort)

        # starting from last element to build heaptree. as result, max value will be at index first, both children
        # are at 1 and 2. 1's children at 3 an 4, 2's at 5 and 6 and so on
        for numberIndex in range(len(self.dataToSort)//2 - 1, -1, -1):
            self.__heapify(numberIndex, totalElementCount)

        # turn the list arround into a ordered list from low to highest
        for index in range(len(self.dataToSort) - 1, -1, -1):

            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.PURPLE.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.ORANGE.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

            # last element is put to heap.
            self.dataToSort[0], self.dataToSort[index] = self.dataToSort[index], self.dataToSort[0]
            self.__heapify(0, index)

    def __heapify(self, parentIndex: int, maxAllowedIndexToBeHeapified: int) -> None:

        indexOfHighestNumber: int = parentIndex

        # for building artificial heap tree with max value as root node
        leftChildIndex: int = 2 * parentIndex + 1
        rightChildIndex: int = 2 * parentIndex + 2

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if leftChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[leftChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = leftChildIndex

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if rightChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[rightChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = rightChildIndex

        # current parent node is not the highest value within the tree, thus it needs to be switched with the highest value of its child
        # current highest value becomes new parent
        if indexOfHighestNumber != parentIndex:
            self.dataToSort[parentIndex], self.dataToSort[indexOfHighestNumber] = self.dataToSort[indexOfHighestNumber], self.dataToSort[parentIndex]

            # because of switching both values, something below could have changed as well.
            # check if heapification is required from new parent node on downwards
            self.__heapify(indexOfHighestNumber, maxAllowedIndexToBeHeapified)

if __name__ == '__main__':
    l = [1, 5, 2, 19, 2, 6, 91]
    hs = HeapSort(dataToSort=l, sortingCanvas=None)
    print(l)
from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class HeapSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()
        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self) -> None:
        # max index for heapification
        totalElementCount: int = len(self.dataToSort)

        # starting from last element to build heaptree. as result, max value will be at index first, both children
        # are at 1 and 2. 1's children at 3 an 4, 2's at 5 and 6 and so on
        for numberIndex in range(len(self.dataToSort)//2 - 1, -1, -1):
            self.__heapify(numberIndex, totalElementCount)

        # turn the list arround into a ordered list from low to highest
        for index in range(len(self.dataToSort) - 1, -1, -1):

            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.PURPLE.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.ORANGE.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

            # last element is put to heap.
            self.dataToSort[0], self.dataToSort[index] = self.dataToSort[index], self.dataToSort[0]
            self.__heapify(0, index)

    def __heapify(self, parentIndex: int, maxAllowedIndexToBeHeapified: int) -> None:

        indexOfHighestNumber: int = parentIndex

        # for building artificial heap tree with max value as root node
        leftChildIndex: int = 2 * parentIndex + 1
        rightChildIndex: int = 2 * parentIndex + 2

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if leftChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[leftChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = leftChildIndex

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if rightChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[rightChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = rightChildIndex

        # current parent node is not the highest value within the tree, thus it needs to be switched with the highest value of its child
        # current highest value becomes new parent
        if indexOfHighestNumber != parentIndex:
            self.dataToSort[parentIndex], self.dataToSort[indexOfHighestNumber] = self.dataToSort[indexOfHighestNumber], self.dataToSort[parentIndex]

            # because of switching both values, something below could have changed as well.
            # check if heapification is required from new parent node on downwards
            self.__heapify(indexOfHighestNumber, maxAllowedIndexToBeHeapified)
from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class HeapSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()
        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self) -> None:
        # max index for heapification
        totalElementCount: int = len(self.dataToSort)

        # starting from last element to build heaptree. as result, max value will be at index first, both children
        # are at 1 and 2. 1's children at 3 an 4, 2's at 5 and 6 and so on
        for numberIndex in range(len(self.dataToSort)//2 - 1, -1, -1):
            self.__heapify(numberIndex, totalElementCount)

        # turn the list arround into a ordered list from low to highest
        for index in range(len(self.dataToSort) - 1, -1, -1):

            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.PURPLE.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.ORANGE.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

            # last element is put to heap.
            self.dataToSort[0], self.dataToSort[index] = self.dataToSort[index], self.dataToSort[0]
            self.__heapify(0, index)

    def __heapify(self, parentIndex: int, maxAllowedIndexToBeHeapified: int) -> None:

        indexOfHighestNumber: int = parentIndex

        # for building artificial heap tree with max value as root node
        leftChildIndex: int = 2 * parentIndex + 1
        rightChildIndex: int = 2 * parentIndex + 2

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if leftChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[leftChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = leftChildIndex

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if rightChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[rightChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = rightChildIndex

        # current parent node is not the highest value within the tree, thus it needs to be switched with the highest value of its child
        # current highest value becomes new parent
        if indexOfHighestNumber != parentIndex:
            self.dataToSort[parentIndex], self.dataToSort[indexOfHighestNumber] = self.dataToSort[indexOfHighestNumber], self.dataToSort[parentIndex]

            # because of switching both values, something below could have changed as well.
            # check if heapification is required from new parent node on downwards
            self.__heapify(indexOfHighestNumber, maxAllowedIndexToBeHeapified)

if __name__ == '__main__':
    l = [1, 5, 2, 19, 2, 6, 91]
    hs = HeapSort(dataToSort=l, sortingCanvas=None)
    print(l)
from typing import List

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.colors.colorenum import ColorEnum


class HeapSort(AbstractSort):

    def __init__(self, *, dataToSort: List[int], sortingCanvas: SortingCanvas) -> None:
        super().__init__(dataToSort=dataToSort, sortingCanvas=sortingCanvas)
        self.sort()
        if self.sortingCanvas:
            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
            self.sortingCanvas.endSearch(self.dataToSort)

    def sort(self) -> None:
        # max index for heapification
        totalElementCount: int = len(self.dataToSort)

        # starting from last element to build heaptree. as result, max value will be at index first, both children
        # are at 1 and 2. 1's children at 3 an 4, 2's at 5 and 6 and so on
        for numberIndex in range(len(self.dataToSort)//2 - 1, -1, -1):
            self.__heapify(numberIndex, totalElementCount)

        # turn the list arround into a ordered list from low to highest
        for index in range(len(self.dataToSort) - 1, -1, -1):

            if self.sortingCanvas:
                self.sortingCanvas.colorizeSingleDrawnRectangle(index, ColorEnum.GREEN.value)
                self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

            # last element is put to heap.
            self.dataToSort[0], self.dataToSort[index] = self.dataToSort[index], self.dataToSort[0]
            self.__heapify(0, index)

    def __heapify(self, parentIndex: int, maxAllowedIndexToBeHeapified: int) -> None:

        indexOfHighestNumber: int = parentIndex

        # for building artificial heap tree with max value as root node
        leftChildIndex: int = 2 * parentIndex + 1
        rightChildIndex: int = 2 * parentIndex + 2

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if leftChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[leftChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = leftChildIndex

        # check whether left child is allowed to be switched and if it is bigger than current parent
        if rightChildIndex < maxAllowedIndexToBeHeapified and self.dataToSort[rightChildIndex] >= self.dataToSort[indexOfHighestNumber]:
            indexOfHighestNumber = rightChildIndex

        # current parent node is not the highest value within the tree, thus it needs to be switched with the highest value of its child
        # current highest value becomes new parent
        if indexOfHighestNumber != parentIndex:
            self.dataToSort[parentIndex], self.dataToSort[indexOfHighestNumber] = self.dataToSort[indexOfHighestNumber], self.dataToSort[parentIndex]

            # because of switching both values, something below could have changed as well.
            # check if heapification is required from new parent node on downwards
            self.__heapify(indexOfHighestNumber, maxAllowedIndexToBeHeapified)
