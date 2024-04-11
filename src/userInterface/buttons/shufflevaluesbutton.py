import tkinter as tk

from src.numbergenerator.createrandomnumbers import create_random_numbers
from src.userInterface.canvas.sortingcanvas import SortingCanvas


class ShuffleValuesButton(tk.Button):

    def __init__(self, master: tk.Frame, sortingCanvas: SortingCanvas, arraysize: int,  *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.config(text="Shuffle values")
        self.config(command= lambda: sortingCanvas.shuffleArray(create_random_numbers(arraysize)))
