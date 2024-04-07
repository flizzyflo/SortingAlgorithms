from random import randint
from typing import List


def create_random_numbers(desiredArraySize: int, seedStart: int = 100, seedEnd: int = 1_000_000) -> List[int]:

    """This function creates an array containing 'desiredArraySize' integer within the range of 
    'seedStart' and 'seedEnd'."""

    randomArray = [] 
      
    for _ in range (desiredArraySize):
        randomArray.append(randint(seedStart, seedEnd))
    
    return randomArray