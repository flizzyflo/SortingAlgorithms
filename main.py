from valueBarChart import *
from userInterface import *

def create_random_values(min: int, max: int) -> list[int]:
    values = [] 
    for _ in range(min, max):
        values.append(randint(1, 250))
    
    return values



def main():
    values = create_random_values(1, 67)
    objects = create_rectangle_object(values)
    setUpUserInterface(objects)


if __name__ == "__main__":
    main()