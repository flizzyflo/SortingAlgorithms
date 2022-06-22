import math
from random import randint

# COLUMSPAN: int = 5
# SORTING_SPEED: int = 75 #lower value = faster sorting

# # SeedSize regulates, within which size-interval the randomly created values can be. Start is lower, end is upper bound
# RANDOM_SEED_START: int = 5 
# RANDOM_SEED_END: int = 100

# # Specifies the total amount of values stored within the randomly generated array.
# ARRAYSIZE: int = 30

# CANVAS_WIDTH:int = 1920
# CANVAS_HEIGHT:int = 1000
# BAR_HEIGHT:int = CANVAS_HEIGHT - 1

# INITIAL_RECTANGLE_COLOR: str = "#40E0D0"
# RECTANGLE_OBJECT_TAG: str = "rectangles"
# CANVAS_BACKGROUND_COLOR: str = "white"


class Rectangle:

    """Rectangle class represents the rectangles displayed on a canvas passed in as object.
    The class manages the comparison, ordering and visualisation of both, the rectangles and the 
    values list underlying the rectangles. The class has either class (static) or object methods to
    manage the data."""


    allRectangles: list[object] = []
    canvas: object = None
    rectangleTag: str = "Rectangle"
    barWidth = math.floor(CANVAS_WIDTH / ARRAYSIZE) - 1.5

    x1Coordinate: int = 3
    x2Coordinate: int = x1Coordinate
    
    def __init__(self, rectangleValue: int, canvasObject: object) -> None:
        
        """Initializes the class wide canvas object, where all rectangles are drawn on and
        sets up the visualisation per individual rectangle instance."""
        
        Rectangle.initializeCanvasObject(canvasObject= canvasObject)
        
        self.rectangleValue = rectangleValue
        self.rectangleOnCanvas = self.initializeRectangle(rectangleValue)


    def __repr__(self) -> str:
        return f"{self.rectangleValue}"


    def __eq__(self, object: object) -> bool:
        return self.rectangleValue == object.rectangleValue


    def __lt__(self, object: object) -> bool:
        return self.rectangleValue < object.rectangleValue


    def __le__(self, object: object) -> bool:
        return self.rectangleValue <= object.rectangleValue


    def __gt__(self, object: object) -> bool:
        return self.rectangleValue > object.rectangleValue


    def __ge__(self, object: object) -> bool:
        return self.rectangleValue >= object.rectangleValue


    def createRandomValues(canvasObject: object = None) -> None:
        
        """Populates the allRectangles list with rectangles, containing randomly created values. Basically sets up the rectangles visualized on screen."""

        try: 
            # Trying to delete existing rectangles, if some exist
            # Counts for both, the rectangle values list which takes care of the raw list order
            # as well as for the visualization. 

            Rectangle.deleteAllRectanglesList()
            Rectangle.clearCanvas()

        finally:

            # In every case, new rectangle objects are created, the rectanglesAll list is populated with values and the 
            # rectangles are visualized on the canvas object

            for _ in range(1, ARRAYSIZE):
                Rectangle.initializeCanvasObject(canvasObject)
                Rectangle(randint(1, 150000), Rectangle.canvas)


    def initializeCanvasObject(canvasObject: object) -> None:
        
        """Sets the canvas object for the rectangle class on which the rectangles will be drawn."""

        Rectangle.canvas = canvasObject


    def deleteAllRectanglesList() -> None:
        
        """Deletes the class list for all rectangles. Needed when new, randomized values should be created and visualized as rectangles.
        Resets the rectangle coordinates as well, since they need to be reset to present new rectangles."""

        Rectangle.allRectangles.clear()
        Rectangle.x1Coordinate = 3
        Rectangle.x2Coordinate = Rectangle.x1Coordinate


    def clearCanvas() -> None:
        
        """Deletes the rectangles displayed on the Rectangle.canvas object."""

        Rectangle.canvas.delete("all")


    def switchRectanglePositions(currentLeftRectangleIndex: int, currentRightRectangleIndex: int) -> None:
        
        """Switches the coordinate values of two rectangles given. Used to switch position"""

        leftRectangle = Rectangle.allRectangles[currentLeftRectangleIndex]
        rightRectangle = Rectangle.allRectangles[currentRightRectangleIndex]


        leftx1, lefty1, leftx2, lefty2 = Rectangle.canvas.coords(leftRectangle.rectangleOnCanvas)
        rightx1, righty1, rightx2, righty2 = Rectangle.canvas.coords(rightRectangle.rectangleOnCanvas)


        Rectangle.canvas.coords(leftRectangle.rectangleOnCanvas, rightx1, lefty1, rightx2, lefty2)
        Rectangle.canvas.coords(rightRectangle.rectangleOnCanvas, leftx1, righty1, leftx2, righty2)


    def switchRectangleListPositions(currentLeftRectangleIndex: int, currentRightRectangleIndex: int) -> None:
        
        """Switches the values within the rectanle list. Important for comparison reason to let the list be sorted not 
        only visually, but by values as well."""

        temp = Rectangle.allRectangles[currentLeftRectangleIndex]
        Rectangle.allRectangles[currentLeftRectangleIndex] = Rectangle.allRectangles[currentRightRectangleIndex]
        Rectangle.allRectangles[currentRightRectangleIndex] = temp


    def changeRectangleColor(self, color: str) -> None:
        
        """Function to change the color of the rectangle object into the color passed in as parameter."""

        Rectangle.canvas.itemconfig(self.rectangleOnCanvas, 
                                    fill= color)
    

    def initializeRectangle(self, rectangleValue: int) -> object:
        
        """Create an rectangle object and store it within the Rectangle Class list. 
        Afterwards, returning it as return value."""      
        
        Rectangle.x2Coordinate: int = Rectangle.x1Coordinate + Rectangle.barWidth

        # Creation of the rectangle object, storing the id within tempVar
        rectangleOnCanvas = Rectangle.canvas.create_rectangle(Rectangle.x1Coordinate, 
                                                            BAR_HEIGHT - (rectangleValue // BAR_HEIGHT) - 50, 
                                                            Rectangle.x2Coordinate, 
                                                            BAR_HEIGHT, 
                                                            tags= Rectangle.rectangleTag, 
                                                            fill=INITIAL_RECTANGLE_COLOR)

        Rectangle.x1Coordinate = Rectangle.x2Coordinate + 2

        # Appending the Rectangle Object to the class list of Rectangle Objects.
        Rectangle.allRectangles.append(self)

        # Returns a rectangle object
        return rectangleOnCanvas


    def deleteRectangle(self) -> None:
        
        """Function to delete the rectangle object via accessing it with its tag. Tags are set individually."""

        Rectangle.canvas.delete(self.rectangleOnCanvas)



### Since this rectangle class is not implemented yet, this commented section is a "testrun" for this class
# from tkinter import *
# root = Tk()
# can = Canvas(root, bg= CANVAS_BACKGROUND_COLOR, width= CANVAS_WIDTH + 20, height=CANVAS_HEIGHT, relief= SUNKEN)
# can.pack()

# Button(root, text="Start Bubblesort", command= lambda: bubblesort()).pack()
# Button(root, text="Generate random values", command= lambda: Rectangle.createRandomValues(canvasObject = can)).pack()

# def bubblesort():

#     for i in range(len(Rectangle.allRectangles)):
#         for i in range(len(Rectangle.allRectangles)):

#             if i+1 > len(Rectangle.allRectangles) -1:
#                 break

#             Rectangle.allRectangles[i].changeRectangleColor("pink")

#             if Rectangle.allRectangles[i].rectangleValue > Rectangle.allRectangles[i + 1].rectangleValue:
#                 Rectangle.allRectangles[i].changeRectangleColor("red")
#                 Rectangle.allRectangles[i + 1].changeRectangleColor("red")
#                 Rectangle.switchRectanglePositions(i , i+1)
#                 Rectangle.switchRectangleListPositions(i , i+1)

#             var = IntVar()
#             root.after(5, lambda: var.set(1))
#             root.wait_variable(var)

#             Rectangle.allRectangles[i].changeRectangleColor(INITIAL_RECTANGLE_COLOR)
#             Rectangle.allRectangles[i + 1].changeRectangleColor(INITIAL_RECTANGLE_COLOR)
   
#     for i in range(len(Rectangle.allRectangles)):
#         var = IntVar()
#         root.after(5, lambda: var.set(1))
#         root.wait_variable(var)

#         Rectangle.allRectangles[i].changeRectangleColor("green")

# root.mainloop()
