

import math
from random import randint


COLUMSPAN: int = 5
SORTING_SPEED: int = 75 #lower value = faster sorting

# SeedSize regulates, within which size-interval the randomly created values can be. Start is lower, end is upper bound
RANDOM_SEED_START: int = 5 
RANDOM_SEED_END: int = 100

# Specifies the total amount of values stored within the randomly generated array.
ARRAYSIZE: int = 58

CANVAS_WIDTH:int = 1920
CANVAS_HEIGHT:int = 1000
BAR_HEIGHT:int = CANVAS_HEIGHT - 1

INITIAL_RECTANGLE_COLOR: str = "#40E0D0"
RECTANGLE_OBJECT_TAG: str = "rectangles"
CANVAS_BACKGROUND_COLOR: str = "white"
ROOT_TITLE: str = "Search Algorithm Presentation"
GEOMETRY_MEASUREMENT: str = "2000x1200"

class Rectangle:

    allRectangles: list[object] = []
    canvas: object = None
    rectangleTag: str = "Rectangle"
    barWidth = math.floor(CANVAS_WIDTH / ARRAYSIZE) - 1.5

    x1Coordinate: int = 3
    x2Coordinate: int = x1Coordinate
    

    def __init__(self, rectangleValue: int) -> None:
        self.rectangleValue = rectangleValue
        self.rectangleObject = self.createRectangle(rectangleValue)


    def __repr__(self) -> str:
        return f"{Rectangle.rectangleTag} - Value: {self.rectangleValue}"


    def setCanvasObject(canvasObject: object) -> None:
        
        """Sets the canvas object for the rectangle class on which the rectangles will be drawn."""

        Rectangle.canvas = canvasObject


    def changeRectangleColor(self, color: str) -> None:
        
        """Function to change the color of the rectangle object into the color passed in as parameter."""

        Rectangle.canvas.itemconfig(self.rectangleObject, fill=color)
    

    def createRectangle(self, rectangleValue: int) -> object:
        
        """Create an rectangle object and store it within the Rectangle Class list. 
        Afterwards, returning it as return value."""      
        
        Rectangle.x2Coordinate: int = Rectangle.x1Coordinate + Rectangle.barWidth

        # Creation of the rectangle object, storing the id within tempVar
        rectangleInformation = Rectangle.canvas.create_rectangle(Rectangle.x1Coordinate, 
                                                    BAR_HEIGHT - (rectangleValue // BAR_HEIGHT) - 50, 
                                                    Rectangle.x2Coordinate, 
                                                    BAR_HEIGHT, 
                                                    tags= self.rectangleTag, 
                                                    fill=INITIAL_RECTANGLE_COLOR)

        Rectangle.x1Coordinate = Rectangle.x2Coordinate + 2

        # Appending the Rectangle Object to the class list of Rectangle Objects.
        Rectangle.allRectangles.append(self)

        # Returns a rectangle object
        return rectangleInformation


    def deleteRectangle(self) -> None:
        """Function to delete the rectangle object via accessing it with its tag. Tags are set individually."""

        Rectangle.canvas.delete(self.rectangleObject)

    
    def getCoords(self) -> tuple[int, int, int, int]:
        
        """Returns the current coordinates of the rectangle object."""

        return Rectangle.canvas.coords(self.rectangleObject)


    def setCoords(self, newCoords: tuple[int, int, int, int]) -> None:
        
        """Sets the coordinates for a given rectangle to the new coords given as input parameter"""

        Rectangle.canvas.coords(self.rectangleObject, *newCoords)

    
    def switchRectanglePositions(currentLeftRectangle: object, currentRightRectangle: object) -> None:
        
        """Switches the coordinate values of two rectangles given. Used to switch position"""

        leftRectangleCoordinates = currentLeftRectangle.getCoords()
        rightRectangleCoordinates = currentRightRectangle.getCoords()

        currentLeftRectangle.setCoords(rightRectangleCoordinates)
        currentRightRectangle.setCoords(leftRectangleCoordinates)
    
    
    def increaseHeight(self):
        Rectangle.allRectangles[9].changeRectangleColor("red")
        Rectangle.allRectangles[8].changeRectangleColor("blue")
        Rectangle.allRectangles[10].changeRectangleColor("purple")

        Rectangle.switchRectanglePositions(Rectangle.allRectangles[8], Rectangle.allRectangles[10])
        
        

# from tkinter import *

# root = Tk()
# canv = Canvas(root, bg= CANVAS_BACKGROUND_COLOR, width= CANVAS_WIDTH + 20, height=CANVAS_HEIGHT, relief= SUNKEN)
# canv.pack()
# Rectangle.setCanvasObject(canv)


# for i in range(1, ARRAYSIZE):
#     Rectangle(randint(400, 300000))


# Button(root, text= "change color", command= lambda: Rectangle.allRectangles[2].increaseHeight()).pack()


# root.mainloop()