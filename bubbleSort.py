
class BubbleSort:
    
    """BubbleSort class which contains the search algorithm as class method 
    as well as some getter and setter methods."""


    def setTotalRuns(number: int) -> None:
        BubbleSort.totalRuns: int = 0

    
    def addTotalRun(number: int) -> None:
        BubbleSort.totalRuns += number

    
    def getTotalRuns() -> int:
        return BubbleSort.totalRuns

    
    def swapListItems(valueObjectList: list[object], listIndex: int) -> None:
        """Function to swap two values within the array representation of the values."""
        
        temporary_object: object = valueObjectList[listIndex + 1]
        valueObjectList[listIndex + 1] = valueObjectList[listIndex]
        valueObjectList[listIndex] = temporary_object


    def incrementCounter() -> None:
        """Increments the class-internal counter to keep track of the 
        iterations and break the sorting algorithm."""

        try:
            BubbleSort.addTotalRun(1)

        except:
            BubbleSort.setTotalRuns(0)


    def bubbleSortObjects(valueObjectList: list[object]) -> None:
        """Implementation of bubblesort in a way that the progress can be vizualized."""

        n = len(valueObjectList)
        for index, valueObject in enumerate(valueObjectList[:(n - 1)]):

            if index + 1 == n:
                break

            if valueObject.getValue() > valueObjectList[index + 1].getValue():
                BubbleSort.swapListItems(valueObjectList, index)

            
        BubbleSort.incrementCounter()

