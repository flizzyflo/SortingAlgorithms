
from datetime import datetime
from random import randint
from typing import Callable

import BubbleSort, InsertionSort, MergeSort

arr = []   
for i in range (15_000):
   arr.append(randint(1, 1_000_000))

def testPerformance(array: list[int], algoritm: Callable):
    start = datetime.now()
    algoritm(array)
    duration = datetime.now() - start
    
    return f"Sorting is done. '{algoritm.__name__}' took {duration} for sorting an array with '{len(array)}' random values."


arr_comp = arr.copy()
arr2 = arr.copy()
arr2_comp = arr2.copy()
arr3 = arr.copy()

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
