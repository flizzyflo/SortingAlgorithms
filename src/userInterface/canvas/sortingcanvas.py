import math
import tkinter as tk
from typing import List

from src.numbergenerator.createrandomnumbers import create_random_numbers
from src.userInterface.colors.colorenum import ColorEnum

BAR_HEIGHT: int = 680
BAR_GAP: int = 2
RENDER_DELAY: int = 10
RECTANGLE_OBJECT_TAG: str = "rectangles"
CANVAS_BACKGROUND_COLOR: str = "white"


class SortingCanvas(tk.Canvas):

    def __init__(self, root: tk.Widget, arraySize: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root: tk.Widget = root
        self.arraySize = arraySize
        self.BAR_TOP_PADDING: int = 10
        self.BAR_FLOOR_PADDING: int = 10

        self.rectangles: List[int] = []
        self.dataToSort: List[int] = create_random_numbers(self.arraySize, 10, 990)
        self.shuffleArray(self.dataToSort)

    def getValuesToSort(self) -> List[int]:
        return self.dataToSort

    def deleteDrawnRectanglesFromCanvas(self, deletionTag: str = "all") -> None:

        """Deletes every item which is presented within the canvas widget."""

        self.delete(deletionTag)
        self.rectangles.clear()

    def drawRectanglesToCanvas(self, values: list[int], initialStartingPosition: int = 3, rectangleTag: str = RECTANGLE_OBJECT_TAG) -> None:

        """Creates rectangles based on the values stored within the values list passed in as argument."""

        try:
            # If rectagles already exist, try to delete them
            self.deleteDrawnRectanglesFromCanvas(rectangleTag)

        except Exception as e:
            print("Error:", e)

        finally:
            BAR_WIDTH: int = ((self.root.master.getCanvasWidth() - initialStartingPosition) / self.arraySize)

            x0: float = initialStartingPosition
            maxValue = max(self.dataToSort)
            for value in values:

                x1: float = x0 + BAR_WIDTH
                y0: float = BAR_HEIGHT - ((value / maxValue) * BAR_HEIGHT) + self.BAR_TOP_PADDING # top coordinate
                y1: float = BAR_HEIGHT
                self.rectangles.append(self.create_rectangle(x0, y0, x1, y1,
                                                             tags=rectangleTag,
                                                             fill=ColorEnum.WHITE.value,
                                                             outline=""))

                x0 = x1

    def shuffleArray(self, values: list[int]) -> None:

        """Deletes existing rectangle bars presented within
        the canvas and recreates new bar elementes within the canvas."""

        self.dataToSort = values

        self.deleteDrawnRectanglesFromCanvas()
        self.drawRectanglesToCanvas(self.dataToSort)

    def colorizeSingleDrawnRectangle(self, indexNumber: int, color: str = ColorEnum.LIGHTBLUE.value) -> None:

        """Function to change the color of a rectangle item within the canvas."""
        self.itemconfig(self.rectangles[indexNumber], fill=color)

        # Forces the tkinter gui to wait, thus the animation of the sorting itself is smoothened.
        var = tk.IntVar()
        self.after(RENDER_DELAY, lambda: var.set(1))
        self.wait_variable(var)

    def endSearch(self, valuesToSort: List[int]) -> None:
        for index in range(len(valuesToSort)):
            self.colorizeSingleDrawnRectangle(index, ColorEnum.GREEN.value)
