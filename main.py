from ValueObjects import *
from UserInterface import *
from SortTesting import *


def main():

    # for _ in range(1, 150):
    #     testBubbleSort()
    
    randomValues: list = createNewRandomValues(RANDOM_SEED_START, RANDOM_SEED_END)
    valueObjectList: list[object] = valueObjects.createValueObjects(randomValues)

    setUpUserInterface(valueObjectList= valueObjectList)


if __name__ == "__main__":
    main()