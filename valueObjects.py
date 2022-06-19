
class valueObjects: 

    """Main class which represents the values to be sorted as well as the coordinates
    of the respective values, which were used to represent them graphically."""


    def createValueObjects(values: list) -> list[object]:
        """Class Method which creates a list of valueObjects. These instances contain values and their coordinates within the canvas."""

        return [valueObjects(number) for number in values]


    def __init__(self, value: int) -> None:
        self.value: int = value
        self.item_selected: bool = False
        

    def __repr__(self) -> str:
        return str(self.value)


    def __str__(self) -> str:
        return str(self.value)
 

    def setCanvasObject(self, canvasObject: object) -> None:
        """Sets up the canvas object for any single value object instance."""

        self.canvas_Object: object = canvasObject


    def setCoordinates(self, x1:int,  x2: int, y1: int, y2: int) -> None:
        """Sets the coordinates of an object to enable displaying it."""

        self.x1: int = x1
        self.x2: int = x2
        self.y1: int = y1
        self.y2: int = y2


    def setSelectedStatus(self, isSelected: bool) -> None:
        """Sets the selected status of an object according to the boolean input."""

        self.item_selected: bool = isSelected


    def getSelectedStatus(self) -> bool:
        """Gets the selected status of an object according to the boolean status of the object."""

        return self.item_selected


    def setValue(self, value: int) -> None:
        """Sets the value of an object according to the input. The value is the foundation for the sorting itself."""

        self.value: int = value


    def getValue(self) -> int:
        """Gets the value of an object according to the input. The value is the foundation for the sorting itself."""

        return self.value


    def setX1Value(self, newX1CoordinateValue: int) -> None:
        """Sets the x1 coordinate of an object according to the input. This value is the upper left corner of the rectangle."""

        self.x1: int = newX1CoordinateValue


    def getX1Value(self) -> int:
        """Gets the x1 coordinate of an object according to the input. This value is the upper left corner of the rectangle."""

        return self.x1


    def swapRectangleCoordinates(self, valueObject: object) -> None:
        """Swaps coordinate data from two rectangles. This is for visualization of reodering the items."""

        old_x1: int = self.getX1Value()
        old_x1_compared_rect: int = valueObject.getX1Value()

        self.setX1Value(old_x1_compared_rect), valueObject.setX1Value(old_x1)
