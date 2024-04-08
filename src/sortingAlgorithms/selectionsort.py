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

            self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)

            for idxOfNumberToCompare in range(positionToInsertNewMinVal + 1, maxIndex):
                self.sortingCanvas.colorizeSingleDrawnRectangle(idxOfNumberToCompare - 1, color=ColorEnum.LIGHTBLUE.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(positionToInsertNewMinVal, color=ColorEnum.PURPLE.value)
                self.sortingCanvas.colorizeSingleDrawnRectangle(idxOfNumberToCompare, color=ColorEnum.GREEN.value)

                if self.dataToSort[idxOfNumberToCompare] < self.dataToSort[newMinIdx]:
                    newMinIdx = idxOfNumberToCompare

            if newMinIdx != positionToInsertNewMinVal:
                newMinVal = self.dataToSort[newMinIdx]
                oldMinVal = self.dataToSort[positionToInsertNewMinVal]

                self.dataToSort[newMinIdx] = oldMinVal
                self.dataToSort[positionToInsertNewMinVal] = newMinVal

            positionToInsertNewMinVal += 1

        self.sortingCanvas.drawRectanglesToCanvas(self.dataToSort)
        self.sortingCanvas.endSearch(self.dataToSort)