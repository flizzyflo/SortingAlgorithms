from time import sleep
from typing import Callable
from bubbleSort import bubble_sort
from insertionSort import insertionSort
from mergeSort import mergeSort
from valueBarChart import *
from tkinter import *
from tkinter import ttk

COLUMSPAN = 5
global counter
global colour
colour = "red"
counter = 0


def delete_rectangles_ui(objectsList: object, tag: str):
    for object in objectsList:
        object.canvas_Object.delete(tag)

def create_rectangle_object(values: list) -> list[object]: 
    return [ValueBarChart(number) for number in values]

def display_rectangles_ui(objectsList: list[object]):
    x1, y1, x2 = 5, 5, 15 
    for object in objectsList:
            object.create_rect(x1, 260 - object.get_Value(), x2, 260)
            x1 += 15
            x2 += 15

def print_rect_values(objectsList: list[object]) -> None:
    print([f"{item}" for item in objectsList])

def change_color(comparable_one: object, comparable_two: object):

    if comparable_one.compare_rectangle_values(comparable_two):
        comparable_one.move_rectangle(comparable_two)
        
    else:
        comparable_one.canvas_Object.itemconfig(comparable_one.rect, fill="green")

def move_rectangle(InitialItem: object, ValueBarChartComparable: object) -> None:
        InitialItem.swap_rectangle_coordinates(ValueBarChartComparable)
        movement_amount = InitialItem.get_movement_amount(ValueBarChartComparable)
        InitialItem.canvas_Object.move(InitialItem.rect, movement_amount, 0)
        ValueBarChartComparable.canvas_Object.move(ValueBarChartComparable.rect, -movement_amount, 0)
 
def runThroughObjects(objectsList: list[object]):
    global counter, colour

    if counter == 0:
        objectsList[len(objectsList) - 1].canvas_Object.itemconfig(objectsList[len(objectsList) - 1].rect, fill="#40E0D0")

    if counter > 0:
        objectsList[counter - 1].canvas_Object.itemconfig(objectsList[counter - 1].rect, fill="#40E0D0")

    objectsList[counter].canvas_Object.itemconfig(objectsList[counter].rect, fill=colour)
    counter += 1

    if counter == len(objectsList):
        counter = 0
        colour = "blue"


def initialize_search(canvasItem: object, objectsList: list[object], searchAlgorithm: Callable):

    try:
        delete_rectangles_ui(objectsList, "rect")
    
    finally:
        display_rectangles_ui(objectsList)
        searchAlgorithm(objectsList)
      
        canvasItem.after(125, lambda: initialize_search(canvasItem, objectsList, searchAlgorithm))
      
def setUpUserInterface(objectsList: list[object]):
    root = Tk()
    root.title("Search Algorithm Presentation")
    root.geometry("1000x1000")

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