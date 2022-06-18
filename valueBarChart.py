from random import randint




class ValueBarChart: 

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.item_selected: bool = False
        
    def set_canvas_object(self, canvas_Object: object) -> None:
        self.canvas_Object = canvas_Object

    def initialize_coordinates(self, x1:int,  x2: int, y1: int, y2: int) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def set_selected(self, is_selected: bool) -> None:
        self.item_selected = is_selected

    def get_selected(self) -> bool:
        return self.item_selected

    def create_rect(self, x1: int, y1: int, x2: int, y2: int) -> None:

        self.initialize_coordinates(x1, x2, y1, y2)
        self.rect = self.canvas_Object.create_rectangle(self.x1, self.y1 , self.x2, self.y2, tags= "rect", fill="#40E0D0")

    def get_Value(self) -> int:
        return self.value

    def set_x1_value(self, new_x1: int) -> None:
        self.x1 = new_x1

    def get_x1_value(self) -> int:
        return self.x1

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)


    def swap_object_list(self, objectList: list[object], BiggerNumber: int, indexNumberToSwap: int) -> None:
        temporary_object = objectList[indexNumberToSwap]
        objectList[indexNumberToSwap] = self
        objectList[BiggerNumber] = temporary_object


    def swap_rectangle_coordinates(self, ValueBarChart: object) -> None:
        """Swaps coordinate data from two rectangles. This is for visualization of reodering the items."""

        old_x1 = self.get_x1_value()
        old_x1_compared_rect = ValueBarChart.get_x1_value()

        self.set_x1_value(old_x1_compared_rect), ValueBarChart.set_x1_value(old_x1)


    def compare_rectangle_values(self, ValueBarChart: object) -> bool:
        if self.get_Value() >= ValueBarChart.get_Value():
            return True
        else:
            return False

    
