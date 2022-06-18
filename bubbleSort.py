

from time import sleep


def bubble_sort(objectList: list[object]) -> None:
    
    for index, object in enumerate(objectList):

        object.set_selected(True)

        if index + 1 == len(objectList):
            break

        if object.get_Value() > objectList[index + 1].get_Value():
            
            object.swap_rectangle_coordinates(objectList[index + 1])
            object.swap_object_list(objectList, index, index + 1)
        
        object.set_selected(False)

