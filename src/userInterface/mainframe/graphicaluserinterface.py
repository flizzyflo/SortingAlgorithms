from typing import List, Tuple
import tkinter as tk

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.sortingAlgorithms.bogosort import BogoSort
from src.sortingAlgorithms.bubblesort import BubbleSort
from src.sortingAlgorithms.insertionsort import InsertionSort
from src.sortingAlgorithms.mergesort import MergeSort
from src.sortingAlgorithms.radixsort import RadixSort
from src.numbergenerator.createrandomnumbers import create_random_numbers
from src.sortingAlgorithms.selectionsort import SelectionSort
from src.userInterface.buttons.shufflevaluesbutton import ShuffleValuesButton
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.buttons.startsortbutton import StartSortButton
from src.userInterface.frames.buttonframe import ButtonFrame
from src.userInterface.frames.canvasframe import CanvasFrame

CANVAS_WIDTH: int = 2000
CANVAS_HEIGHT: int = 1000
CANVAS_BACKGROUND_COLOR: str = "white"
ARRAYSIZE: int = 500
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
        self.values: List[int] = create_random_numbers(ARRAYSIZE)

        canvasFrame: CanvasFrame = CanvasFrame(master=self)
        canvasFrame.pack(anchor="center")

        self.sortingCanvas: SortingCanvas = SortingCanvas(root=canvasFrame,
                                                          bg=CANVAS_BACKGROUND_COLOR,
                                                          width=self.CANVAS_WIDTH,
                                                          height=self.CANVAS_HEIGHT,
                                                          relief=tk.SUNKEN)

        buttonFrame: ButtonFrame = ButtonFrame(master=self)
        buttonFrame.pack(anchor="center", pady=20)
        sortingAlgorithms = [BubbleSort, InsertionSort, SelectionSort, MergeSort, RadixSort, BogoSort]
        ShuffleValuesButton(buttonFrame, self.sortingCanvas, ARRAYSIZE).grid(row=0, column=0)
        self.setUpSortButtons(sortingAlgorithms, buttonFrame)


        self.sortingCanvas.pack(pady=20)

    def mainloop(self, n=0) -> None:
        super().mainloop()

    def getCanvasHeight(self) -> int:
        return self.CANVAS_HEIGHT

    def getCanvasWidth(self) -> int:
        return self.CANVAS_WIDTH

    def setUpSortButtons(self, sortingAlgorithmns: List[AbstractSort], buttonFrame: ButtonFrame) -> None:
        for columnPosition, sortingAlgorithm in enumerate(sortingAlgorithmns):
            StartSortButton(buttonFrame, sortingAlgorithm, sortingCanvas=self.sortingCanvas).grid(row=0, column=columnPosition + 1)