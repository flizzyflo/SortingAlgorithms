import math
import tkinter as tk
from typing import List

from src.sortingAlgorithms.createRandomArray import createRandomArray
from src.userInterface.colorenum import ColorEnum

CANVAS_WIDTH: int = 2000
BAR_HEIGHT: int = 1000
ARRAYSIZE: int = 200
BAR_GAP: int = 2
RENDER_DELAY: int = 5
INITIAL_RECTANGLE_COLOR: str = "#40E0D0"
RECTANGLE_OBJECT_TAG: str = "rectangles"
CANVAS_BACKGROUND_COLOR: str = "white"


class SortingCanvas(tk.Canvas):

    def __init__(self, root: tk.Widget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root: tk.Widget = root

        self.rectangles: List[int] = []
        self.valuesToSort: List[int] = createRandomArray(ARRAYSIZE)
        self.shuffleArray(self.valuesToSort)

    def getValuesToSort(self) -> List[int]:
        return self.valuesToSort

    def deleteRectangles(self, deletionTag: str = "all") -> None:

        """Deletes every item which is presented within the canvas widget."""

        self.delete(deletionTag)
        self.rectangles.clear()

    def createRectangles(self, values: list[int], initialStartingPosition: int = 3,
                         rectangleTag: str = RECTANGLE_OBJECT_TAG) -> None:

        """Creates rectangles based on the values stored within the values list passed in as argument."""

        try:
            # If rectagles already exist, try to delete them
            self.deleteRectangles(rectangleTag)

        except Exception as e:
            print("Error:", e)

        finally:
            barWidth = math.floor(self.root.master.getCanvasWidth() / ARRAYSIZE) - 2
            x1Coordinate: float = initialStartingPosition

            for value in values:
                x2Coordinate: float = x1Coordinate + barWidth
                # setting x2 coordinate, basically the width of any bar.

                self.rectangles.append(self.create_rectangle(x1Coordinate,
                                                             BAR_HEIGHT - (value // BAR_HEIGHT),
                                                             x2Coordinate,
                                                             BAR_HEIGHT,
                                                             tags=rectangleTag,
                                                             fill=INITIAL_RECTANGLE_COLOR))

                x1Coordinate = x2Coordinate + BAR_GAP
                # Updating starting coordinate for new bar ot the place next to the bar created before with a little gap of 2 between both bars

            # Forces the tkinter gui to wait, thus the animation of the sorting itself is smoothened.
            var = tk.IntVar()
            self.after(RENDER_DELAY, lambda: var.set(1))
            self.wait_variable(var)

    def shuffleArray(self, values: list[int]) -> None:

        """Deletes existing rectangle bars presented within
        the canvas and recreates new bar elementes within the canvas."""

        self.valuesToSort = values

        self.deleteRectangles()
        self.createRectangles(self.valuesToSort)

    def colorizeSingleBar(self, indexNumber: int, color: str = INITIAL_RECTANGLE_COLOR) -> None:

        """Function to change the color of a rectangle item within the canvas."""
        self.itemconfig(self.rectangles[indexNumber], fill=color)

        # Forces the tkinter gui to wait, thus the animation of the sorting itself is smoothened.
        var = tk.IntVar()
        self.after(RENDER_DELAY, lambda: var.set(1))
        self.wait_variable(var)

    def endSearch(self, valuesToSort: List[int]) -> None:
        for index in range(len(valuesToSort)):
            self.colorizeSingleBar(index, ColorEnum.GREEN.value)
