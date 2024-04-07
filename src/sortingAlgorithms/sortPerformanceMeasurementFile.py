
from datetime import datetime, timedelta
from typing import Callable
from src.numbergenerator.createrandomnumbers import create_random_numbers

# Creating the random array for the testing purposes
unsortedArray: list[int] = create_random_numbers(150_000)

def testPerformance(arrayToBeSorted: list[int], sortAlgorithm: Callable):

    """Function to track the performance of the sorting algorithms. Tracking is created with the 
    time function. Rough estimate, just for raw comparison."""

    start: datetime = datetime.now()
    sortAlgorithm(arrayToBeSorted)
    duration: timedelta = datetime.now() - start
    
    return f"Sorting is done. '{sortAlgorithm.__name__}' took {duration} for sorting an array with '{len(arrayToBeSorted)}' random values."


# Creating the comparison arrays for the build in sorted function.
arr_comp = unsortedArray.copy()
arr2 = unsortedArray.copy()
arr2_comp = arr2.copy()
arr3 = unsortedArray.copy()

print("\n" * 3)
print("-" * 30, "Sorting Performance", "-" * 30)
# print(testPerformance(arr, BubbleSort.bubbleSort))
# print(f"Sorting ist correct: {arr == sorted(arr_comp)}")
# print("-" * 81)
# print(testPerformance(arr2, InsertionSort.insertionSort))
# print(f"Sorting ist correct: {arr2 == sorted(arr2_comp)}")
# print("-" * 81)
print(testPerformance(arr3, MergeSort.splitArray))
print(f"Sorting ist correct: {MergeSort.splitArray(arr3) == sorted(arr3)}")
print("Correctness check via comparison is based on build-in Python applied on the array 'sorted' function.")
print("-" * 81)
