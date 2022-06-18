from valueObjects import *
from userInterface import *
from random import randint

def create_random_values(min: int, max: int) -> list[int]:
    values = [] 
    for _ in range(min, max):
        values.append(randint(1, 250))
    
    return values


def main(objectsList: list[object]):
    setUpUserInterface(objectsList= objectsList)


if __name__ == "__main__":
    values = create_random_values(1, 67)
    objects = createValueObjects(values)
    main(objectsList= objects)