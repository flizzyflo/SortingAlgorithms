from src.userInterface.colorenum import ColorEnum
from src.userInterface.sortingcanvas import SortingCanvas


def insertionSort(values: list[int], sortingCanvas: SortingCanvas) -> None:
    """Implementation of insertion sort. This approach compares a value with the former value. If the former value
   is bigger than the current value, both are swapped. This algorithm works in-place and is stable."""

    if len(values) == 0:
        return

    for forwardCounter, currentValue in enumerate(values, 1):

        backwardCounter = forwardCounter - 1

        while backwardCounter >= 0:

            if values[backwardCounter] > currentValue:
                # if current value is smaller than the former value, swap both.

                values[backwardCounter], values[backwardCounter + 1] = currentValue, values[backwardCounter]

                if sortingCanvas:
                    # updates the GUI, according to the current values of the values list, if used in visualization.
                    sortingCanvas.colorizeSingleBar(backwardCounter, ColorEnum.PURPLE.value)
                    sortingCanvas.colorizeSingleBar(backwardCounter + 1, ColorEnum.ORANGE.value)

                    sortingCanvas.createRectangles(values)

            backwardCounter -= 1

    if sortingCanvas:
        sortingCanvas.endSearch(values)
