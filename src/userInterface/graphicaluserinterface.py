from typing import List, Tuple
import tkinter as tk
from src.sortingAlgorithms.bubblesort import bubbleSort
from src.sortingAlgorithms.insertionsort import insertionSort
from src.sortingAlgorithms.mergesort import MergeSort
from src.sortingAlgorithms.radixsort import RadixSort
from src.sortingAlgorithms.createRandomArray import createRandomArray
from src.userInterface.colorenum import ColorEnum
from src.userInterface.sortingcanvas import SortingCanvas

CANVAS_WIDTH: int = 2000
CANVAS_HEIGHT: int = 1000
CANVAS_BACKGROUND_COLOR: str = "white"
ARRAYSIZE: int = 200
RECTANGLE_OBJECT_TAG: str = "rectangles"
FONTSTYLE: Tuple[str, int, str] = ("Calibri", 18, "bold")


class GraphicalUserInterface(tk.Tk):
    """Class to set up the whole visual presentation of the programm. Furthermore, it manages the
    visual presentation of the sorting itself."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.CANVAS_WIDTH = CANVAS_WIDTH
        self.CANVAS_HEIGHT = CANVAS_HEIGHT
        self.DELAY: int = 5
        self.BAR_GAP: int = 3
        self.BAR_WIDTH_OFFSET: float = 1.0
        self.values: List[int] = createRandomArray(ARRAYSIZE)

        tk.Label(self,
                 text="Visualization of several sorting algoritms",
                 font=FONTSTYLE).pack()

        tk.Label(self,
                 text=f"Total of {ARRAYSIZE} values to sort",
                 font=FONTSTYLE).pack()

        framesInRootWidget: list = [tk.Frame(self) for _ in range(2)]
        for i in range(len(framesInRootWidget)):
            framesInRootWidget[i].pack(anchor="center")

        self.sortingCanvas: SortingCanvas = SortingCanvas(root=framesInRootWidget[1],
                                                          bg=CANVAS_BACKGROUND_COLOR,
                                                          width=self.CANVAS_WIDTH,
                                                          height=self.CANVAS_HEIGHT,
                                                          relief=tk.SUNKEN)

        self.sortingCanvas.pack(pady=20)

        tk.Button(framesInRootWidget[0],
                  text="Shuffle Values",
                  command=lambda: self.sortingCanvas.shuffleArray(createRandomArray(ARRAYSIZE))).grid(row=0,
                                                                                                      column=0)
        tk.Button(framesInRootWidget[0],
                  text="Start Bubble Sort",
                  state=tk.NORMAL,
                  command=lambda: bubbleSort(self.sortingCanvas.getValuesToSort(), self.sortingCanvas)).grid(row=0,
                                                                                                             column=1)
        tk.Button(framesInRootWidget[0],
                  text="Start Insertion Sort",
                  state=tk.NORMAL,
                  command=lambda: insertionSort(self.sortingCanvas.getValuesToSort(), self.sortingCanvas)).grid(row=0,
                                                                                                                column=2)
        tk.Button(framesInRootWidget[0],
                  text="Start Merge Sort",
                  state=tk.NORMAL,
                  command=lambda: MergeSort(self.sortingCanvas.getValuesToSort(), self.sortingCanvas)).grid(row=0,
                                                                                                            column=3)
        tk.Button(framesInRootWidget[0],
                  text="Start Radix Sort",
                  state=tk.NORMAL,
                  command=lambda: RadixSort(self.sortingCanvas.getValuesToSort(), self.sortingCanvas)).grid(row=0,
                                                                                                            column=4)

    def mainloop(self, n=0) -> None:
        super().mainloop()

    def getCanvasHeight(self) -> int:
        return self.CANVAS_HEIGHT

    def getCanvasWidth(self) -> int:
        return self.CANVAS_WIDTH
