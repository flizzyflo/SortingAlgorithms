import tkinter as tk

from src.sortingAlgorithms.abstractsort import AbstractSort
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class StartSortButton(tk.Button):

    def __init__(self, master: tk.Frame, sortingAlgorithm: AbstractSort, sortingCanvas: SortingCanvas, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.config(text=f"{sortingAlgorithm.__name__} starten")
        self.config(command=lambda: sortingAlgorithm(dataToSort=sortingCanvas.getValuesToSort(), sortingCanvas=sortingCanvas))