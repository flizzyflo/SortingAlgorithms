
from typing import Callable
from bubbleSort import bubble_sort
from insertionSort import insertionSort
from mergeSort import mergeSort
from valueObjects import *
from tkinter import *
from tkinter import ttk

COLUMSPAN = 5


def delete_rectangles_ui(objectsList: object, tag: str):
    """Function to delete all rectangle items presented on the screen."""

    for object in objectsList:
        object.canvas_Object.delete(tag)


def createValueObjects(values: list) -> list[object]:
    """Creates a list of valueObjects, which contain values and coordinates within the canvas."""

    return [valueObjects(number) for number in values]


def display_rectangles_ui(objectsList: list[object]):
    """Function to create and display the rectangles."""

    x1, x2 = 5, 15 
    for object in objectsList:
            object.create_rect(x1, 260 - object.get_Value(), x2, 260)
            x1 += 15
            x2 += 15


def move_rectangle(originalItem: object, valueObjectToCompare: object) -> None:
    """Function to move the graphical presentation of the rectangles and switch positions.
    Used to visualize the sorting process."""

    originalItem.swap_rectangle_coordinates(valueObjectToCompare)
    movement_amount = originalItem.get_movement_amount(valueObjectToCompare)
    originalItem.canvas_Object.move(originalItem.rect, movement_amount, 0)
    valueObjectToCompare.canvas_Object.move(valueObjectToCompare.rect, -movement_amount, 0)
 

def initialize_search(canvasItem: object, objectsList: list[object], searchAlgorithm: Callable):
    """Wrapper function to call several sub functions which initialize the search process."""

    try:
        delete_rectangles_ui(objectsList, "rect")
    
    finally:
        display_rectangles_ui(objectsList)
        searchAlgorithm(objectsList)
        canvasItem.after(125, lambda: initialize_search(canvasItem, objectsList, searchAlgorithm))
      

def setUpUserInterface(objectsList: list[object]):
    """Function to initially set up the whole visual presentation of the programm."""

    root = Tk()
    root.title("Search Algorithm Presentation")
    root.geometry("1000x300")

    frame_array = [Frame(root) for _ in range(2)]
    for i in range(len(frame_array)):
        frame_array[i].pack(fill=BOTH)

    ttk.Button(frame_array[0], command= lambda: delete_rectangles_ui(objectsList, "rect"), text="Delete Rectangles").grid(row= 0, column=1)
    ttk.Button(frame_array[0], command= lambda: display_rectangles_ui(objectsList), text="Display Rectangles").grid(row= 0, column=0)
    ttk.Button(frame_array[0], text="Start Insertion Sort", command= lambda: initialize_search(canv, objectsList, insertionSort), state= DISABLED).grid(row= 0, column=2)
    ttk.Button(frame_array[0], text="Start Bubble Sort", command= lambda: initialize_search(canv, objectsList, bubble_sort)).grid(row= 0, column=3)
    ttk.Button(frame_array[0], text="Start Merge Sort", command= lambda: initialize_search(canv, objectsList, mergeSort), state= DISABLED).grid(row= 0, column=4)

    canv = Canvas(frame_array[1], bg= "white")
    canv.pack(fill=BOTH)
    for object in objectsList:
        object.set_canvas_object(canv)

    root.mainloop()