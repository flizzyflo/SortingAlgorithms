import BubbleSort
from UserInterface import *
from ValueObjects import *


def testBubbleSort() -> bool:

    # Creating two arrays. Sorted and compared for testing purposes 
    pythonSortArray: list = createNewRandomValues(5, 25)
    BubbleSortArray: list = valueObjects.createValueObjects(pythonSortArray)
    
    # Sorting array with python internal sort method
    pythonSortArray.sort()

    # Initializing the class attribute counter
    BubbleSort.incrementCounter()

    # Sort array with same values with BubbleSort.
    while BubbleSort.getTotalRuns() < len(BubbleSortArray):
        BubbleSort.bubbleSort(BubbleSortArray)

    # Set Class attribute to zero, to be able to perform bubble sort again.    
    BubbleSort.setTotalRuns(0)

    # Compare Numbers in sorted Arrays
    for number, number2 in zip(pythonSortArray, BubbleSortArray):
        result:bool = (number == number2.getValue())
        assert result == True, "Comparison should be true"
    
    return True