from typing import List, Tuple
import tkinter as tk

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.numbergenerator.createrandomnumbers import create_random_numbers
from src.userInterface.buttons.shufflevaluesbutton import ShuffleValuesButton
from src.userInterface.canvas.sortingcanvas import SortingCanvas
from src.userInterface.buttons.startsortbutton import StartSortButton
from src.userInterface.colors.colorenum import ColorEnum
from src.userInterface.frames.buttonframe import ButtonFrame
from src.userInterface.frames.canvasframe import CanvasFrame

CANVAS_WIDTH: int = 1000
CANVAS_HEIGHT: int = 800
RECTANGLE_OBJECT_TAG: str = "rectangles"
FONTSTYLE: Tuple[str, int, str] = ("Arial", 18, "bold")


class GraphicalUserInterface(tk.Tk):
    """Class to set up the whole visual presentation of the programm. Furthermore, it manages the
    visual presentation of the sorting itself."""

    def __init__(self, sortingAlgorithms: List[AbstractSort], desiredArraySize: int, backgroundColor: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.config(background=backgroundColor)
        self.CANVAS_WIDTH = CANVAS_WIDTH
        self.CANVAS_HEIGHT = CANVAS_HEIGHT
        self.sortingAlgorithms: List[AbstractSort] = sortingAlgorithms
        self.desiredArraySize: int = desiredArraySize
        self.values: List[int] = create_random_numbers(self.desiredArraySize)
        canvasFrame: CanvasFrame = CanvasFrame(master=self, background=backgroundColor, borderwidth=0)
        canvasFrame.pack(anchor="center")

        self.sortingCanvas: SortingCanvas = SortingCanvas(root=canvasFrame,
                                                          arraySize=self.desiredArraySize,
                                                          bg=backgroundColor,
                                                          width=self.CANVAS_WIDTH,
                                                          height=self.CANVAS_HEIGHT)

        buttonFrame: ButtonFrame = ButtonFrame(master=self, background=backgroundColor, borderwidth=0, border=None)
        buttonFrame.pack(anchor="center", pady=20)

        ShuffleValuesButton(buttonFrame, self.sortingCanvas, self.desiredArraySize).grid(row=0, column=0)
        self.setUpSortButtons(self.sortingAlgorithms, buttonFrame)

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