
import math
from SortingAlgorithms.BubbleSort import bubbleSort
from SortingAlgorithms.InsertionSort import insertionSort
from SortingAlgorithms.MergeSort import splitArray
from SortingAlgorithms.createRandomArray import createRandomArray

from tkinter import *
from tkinter import ttk
from Settings import *

class GraphicalUserInterface:
    
    """Class to set up the whole visual presentation of the programm. Furthermore, it manages the 
    visual presentation of the sorting itself."""


    def __init__(self) -> None:

        self.root: object = Tk()
        self.root.title(ROOT_TITLE)
        self.root.geometry(GEOMETRY_MEASUREMENT)

        ttk.Label(self.root, 
                  text="Visulization of several sorting algoritms",
                  font=("Calibri", 14, "bold")).pack(pady=20)
                  
        frame_array: list = [Frame(self.root) for _ in range(2)]
        
        for i in range(len(frame_array)):
            frame_array[i].pack(fill=BOTH)
        
        self.rectangles = []

        self.canvas: object = Canvas(frame_array[1], bg= CANVAS_BACKGROUND_COLOR, width= CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack(pady= 20)
        

        ttk.Button(frame_array[0],                 
                    text= "Create randomized values",
                    command= lambda: self.shuffleArray(createRandomArray(ARRAYSIZE))).grid(row= 0, column=0)
        ttk.Button(frame_array[0], 
                    text= "Start Bubble Sort",
                    state= NORMAL,
                    command= lambda: bubbleSort(self.values, self.createRectangles)).grid(row= 0, column= 1)
        ttk.Button(frame_array[0], 
                    text= "Start Insertion Sort", 
                    state= NORMAL,
                    command= lambda: insertionSort(self.values, self.createRectangles)).grid(row= 0, column= 2)
        ttk.Button(frame_array[0], 
                    text= "Start Merge Sort", 
                    state= NORMAL,
                    command= lambda: splitArray(self.values)).grid(row= 0, column= 3)


        self.root.mainloop()


    def deleteRectangles(self, deletionTag: str = "all") -> None:

        """Deletes every item which is presented within the canvas widget."""

        self.canvas.delete(deletionTag)

    
    def createRectangles(self, values: list[int], initialStartingPosition: int = 3, rectangleTag: str = "all") -> None:

        """Creates rectangles based on the values stored within the values list passed in as argument."""  
       
        try:
            # If rectagles already exist, try to delete them
            self.deleteRectangles(rectangleTag)


        finally:
            barWidth = math.floor(CANVAS_WIDTH / len(values)) - 1.5
            x1Coordinate: int = initialStartingPosition

            for value in values:
                
                x2Coordinate: int = x1Coordinate + barWidth
                # setting x2 coordinate, basically the width of any bar. 

                self.canvas.create_rectangle(x1Coordinate, 
                                            BAR_HEIGHT - (value // BAR_HEIGHT) + 10, 
                                            x2Coordinate, 
                                            BAR_HEIGHT, 
                                            tags= "rectangles", 
                                            fill="grey")
                

                x1Coordinate = x2Coordinate + 2
                # Updating starting coordinate for new bar ot the place next to the bar created before with a little gap of 2 between both bars

            self.canvas.update_idletasks()

    
    def shuffleArray(self, values: list[int]) -> None:

        """Deletes existing rectangle bars presented within the canvas and recreates new bar elementes within the canvas."""

        self.values = values

        self.deleteRectangles()
        self.createRectangles(self.values)

