from src.userInterface.colorenum import ColorEnum
from src.userInterface.sortingcanvas import SortingCanvas


def bubbleSort(values: list[int], sortingCanvas: SortingCanvas) -> None:

    """Implementation of bubble sort. This sorting algorithm grabs a number and switches it with the next number, if the next one is less. The grabed number
    "marches" through the list until a number bigger than itself is found. With this bigger number, the process repeats again Finally, the biggest number 
    is at the end of the array and the process is repeated until the whole array is sorted. This algorithm works in-place and is stable."""

    if len(values) == 0:
      return

    for run in range(len(values)):
        # overall run through the entire values array

        for currentIndex, currentValue in enumerate(values):
            
            if (currentIndex + 1) > len(values) - 1:
                continue

            if currentValue > values[currentIndex + 1]:  
                # If next value is smaller than current value, swap both.
              
                temporary_object: int = values[currentIndex + 1]
                values[currentIndex + 1] = currentValue
                values[currentIndex] = temporary_object

                if sortingCanvas:
                    sortingCanvas.colorizeSingleBar(currentIndex, ColorEnum.GREEN.value)
                    sortingCanvas.colorizeSingleBar(currentIndex + 1, ColorEnum.PURPLE.value)
                # updates the GUI, according to the current values of the values list, if used in visualization.
                    sortingCanvas.createRectangles(values)
                
            else:
                continue

    if sortingCanvas:
    # changing the bar color to green when search is complete and algorithm is used in tkinter gui.        
        sortingCanvas.endSearch(values)
           