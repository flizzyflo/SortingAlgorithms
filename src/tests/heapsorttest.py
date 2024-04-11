import copy
import random
import unittest
from typing import List

from src.sortingAlgorithms.heapsort import HeapSort

class HeapSortTest(unittest.TestCase):

    def testFloats(self):
        floats: List[float] = [random.uniform(-10000.0, 10000.0) for iteration in range(10000)]
        sortedFloats: List[float] = sorted(copy.deepcopy(floats))
        mergeSort: HeapSort = HeapSort(dataToSort=floats, sortingCanvas=None)
        self.assertEqual(floats, sortedFloats)

    def testInts(self):
        integers: List[int] = [random.randint(-10000, 10000) for iteration in range(10000)]
        sortedInts: List[int] = sorted(copy.deepcopy(integers))
        mergeSort: HeapSort = HeapSort(dataToSort=integers, sortingCanvas=None)
        self.assertEqual(integers, sortedInts)


if __name__ == '__main__':
    unittest.main()