import copy
import unittest
import random
from typing import List

from src.sortingAlgorithms.radixsort import RadixSort


class RadixSortTest(unittest.TestCase):


    def testInts(self):
        integers: List[int] = [random.randint(1, 10000) for iteration in range(10000)]
        sortedInts: List[int] = sorted(copy.deepcopy(integers))
        mergeSort: RadixSort = RadixSort(dataToSort=integers, sortingCanvas=None)
        self.assertEqual(integers, sortedInts)


if __name__ == '__main__':
    unittest.main()