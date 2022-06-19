
from turtle import bgcolor
from typing import Callable
from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from ValueObjects import *
from tkinter import *
from tkinter import ttk
from random import randint
from Settings import *

global values

def implementNewValues(valueObjectList: object, values: list[int], randomSeedStartValue: int, randomSeedEndValue: int) -> None:    
    """Wrapper function. Deletes old values, creates new random values and displays them to the canvas object."""

    deleteRectanglesUserInterface(valueObjectList, "rect")
    values = createNewRandomValues(randomSeedStartValue, randomSeedEndValue)

    for valueObject, newValueObjectValue in zip(valueObjectList, values):
        valueObject.setValue(newValueObjectValue)

    displayRectangleUserInterface(valueObjectList)

    
def createNewRandomValues(randomSeedStartValue: int, randomSeedEndValue: int) -> list[int]:
    """Creates new random values for the to be sorted array."""
    
    global values
    values = []

    for _ in range(randomSeedStartValue, randomSeedEndValue):
        values.append(randint(1, 250))

    return values


def deleteRectanglesUserInterface(valueObjectList: object, canvasItemTag: str):
    """Function to delete all rectangle items presented on the screen."""

    for valueObject in valueObjectList:
        valueObject.canvas_Object.delete(canvasItemTag)


def createRectangle(x1: int, y1: int, x2: int, y2: int, valueObject: object) -> object:
    return valueObject.canvas_Object.create_rectangle(x1, 
                                                y1, 
                                                x2, 
                                                y2, 
                                                tags= RECTANGLE_OBJECT_TAG, 
                                                fill= RECTANGLE_COLOR)
    

def displayRectangleUserInterface(valueObjectList: list[object]):
    """Function to create and display the rectangles."""

    x1, x2 = 5, 15 
    for valueObjects in valueObjectList:
            valueObjects.rect = createRectangle(x1, 
                                        260 - valueObjects.getValue(), 
                                        x2, 260, 
                                        valueObjects)
            x1 += 15
            x2 += 15
 

def initializeSearch(canvasItem: object, valueObjectList: list[object], searchAlgorithmClass: Callable):
    """Wrapper function to call several sub functions which initialize the search process."""

    try:
        deleteRectanglesUserInterface(valueObjectList, RECTANGLE_OBJECT_TAG)
    
    finally:
        displayRectangleUserInterface(valueObjectList)
        searchAlgorithmClass(valueObjectList)
        afterID = canvasItem.after(SORTING_SPEED, 
                                lambda: initializeSearch(canvasItem, 
                                                        valueObjectList, 
                                                        searchAlgorithmClass))

        if (searchAlgorithmClass.__name__ == "bubbleSortObjects") and (BubbleSort.getTotalRuns() == len(valueObjectList)):
            canvasItem.after_cancel(afterID)
            BubbleSort.setTotalRuns(0)
        
        elif (searchAlgorithmClass.__name__ == "insertionSortObjects"):
            canvasItem.after_cancel(afterID)

        elif (searchAlgorithmClass.__name__ == "mergeSortObjects"):
            canvasItem.after_cancel(afterID)

        elif (searchAlgorithmClass.__name__ == "quickSortObjects"):
            canvasItem.after_cancel(afterID)


def setUpUserInterface(valueObjectList: list[object]):
    """Function to initially set up the whole visual presentation of the programm."""

    root: object = Tk()
    root.title(ROOT_TITLE)
    root.geometry(GEOMETRY_MEASUREMENT)

    frame_array: list = [Frame(root) for _ in range(2)]
    
    for i in range(len(frame_array)):
        frame_array[i].pack(fill=BOTH)
    

    canv: object = Canvas(frame_array[1], bg= CANVAS_BACKGROUND_COLOR)
    canv.pack(fill=BOTH)
    
    for valueObject in valueObjectList:
        valueObject.setCanvasObject(canv)


    ttk.Button(frame_array[0], 
                command= lambda: implementNewValues(valueObjectList, values, RANDOM_SEED_START, RANDOM_SEED_END), 
                text="Display & create randomized values").grid(row= 0, column=0)
    ttk.Button(frame_array[0], 
                command= lambda: deleteRectanglesUserInterface(valueObjectList, "rect"), 
                text="Delete displayed values").grid(row= 0, column=1)
    ttk.Button(frame_array[0], 
                command= lambda: initializeSearch(canv, valueObjectList, BubbleSort.bubbleSortObjects),
                text="Start Bubble Sort").grid(row= 0, column= 2)
    ttk.Button(frame_array[0], 
                command= lambda: initializeSearch(canv, valueObjectList, InsertionSort.insertionSortObjects), 
                text="Start Insertion Sort", 
                state= NORMAL).grid(row= 0, column= 3)
    ttk.Button(frame_array[0], 
                command= lambda: initializeSearch(canv, valueObjectList, MergeSort.mergeSortObjects), 
                text="Start Merge Sort", 
                state= NORMAL).grid(row= 0, column= 4)
    ttk.Button(frame_array[0], 
                command= lambda: initializeSearch(canv, valueObjectList, QuickSort.quickSortObjects), 
                text="Start Quick Sort", 
                state= NORMAL).grid(row= 0, column= 5)

    root.mainloop()