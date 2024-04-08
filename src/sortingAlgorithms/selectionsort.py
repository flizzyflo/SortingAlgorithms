from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.colors.colorenum import ColorEnum


class SelectionSort(AbstractSort):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sort()

    def sort(self) -> None:

        maxIndex: int = len(self.dataToSort)
        positionToInsertNewMinVal: int = 0

        while positionToInsertNewMinVal < maxIndex:

            newMinIdx: int = positionToInsertNewMinVal

            for idxOfNumberToCompare in range(positionToInsertNewMinVal + 1, maxIndex):

                self.sortingCanvas.colorizeSingleBar(positionToInsertNewMinVal, color=ColorEnum.PURPLE.value)
                self.sortingCanvas.colorizeSingleBar(newMinIdx, color=ColorEnum.ORANGE.value)
                self.sortingCanvas.colorizeSingleBar(idxOfNumberToCompare, color=ColorEnum.GREEN.value)
                self.sortingCanvas.createRectangles(self.dataToSort)

                if self.dataToSort[idxOfNumberToCompare] < self.dataToSort[newMinIdx]:
                    newMinIdx = idxOfNumberToCompare

            if newMinIdx != positionToInsertNewMinVal:
                newMinVal = self.dataToSort[newMinIdx]
                oldMinVal = self.dataToSort[positionToInsertNewMinVal]

                self.dataToSort[newMinIdx] = oldMinVal
                self.dataToSort[positionToInsertNewMinVal] = newMinVal

            positionToInsertNewMinVal += 1


if __name__ == '__main__':
    l = [2, 4, 6, 1, 2, 5]
    s = SelectionSort(dataToSort=l, sortingCanvas=None)

    s.sort()
    print(l)