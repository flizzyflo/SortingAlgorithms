from src.sortingAlgorithms.bogosort import BogoSort
from src.sortingAlgorithms.bubblesort import BubbleSort
from src.sortingAlgorithms.heapsort import HeapSort
from src.sortingAlgorithms.insertionsort import InsertionSort
from src.sortingAlgorithms.mergesort import MergeSort
from src.sortingAlgorithms.quicksort import QuickSort
from src.sortingAlgorithms.radixsort import RadixSort
from src.sortingAlgorithms.selectionsort import SelectionSort
from src.userInterface.colors.colorenum import ColorEnum
from src.userInterface.mainframe.graphicaluserinterface import GraphicalUserInterface

ROOT_TITLE: str = "Search Algorithm Visualization"
GEOMETRY_MEASUREMENT: str = "1400x800"


def main():
    sortingAlgorithms = [BubbleSort, InsertionSort, SelectionSort, MergeSort, RadixSort, QuickSort, HeapSort, BogoSort]

    window = GraphicalUserInterface(sortingAlgorithms, desiredArraySize=350, backgroundColor=ColorEnum.GREY.value)
    window.title(ROOT_TITLE)
    window.geometry(GEOMETRY_MEASUREMENT)

    window.mainloop()

if __name__ == "__main__":
    main()
