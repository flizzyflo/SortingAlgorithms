from random import randint

def createRandomArray(desiredArraySize: int, seedStart: int = 1, seedEnd: int = 1_000_000) -> list[int]:

    """This function creates an array containing 'desiredArraySize' integer within the range of 
    'seedStart' and 'seedEnd'."""

    randomArray = [] 
      
    for _ in range (desiredArraySize):
        randomArray.append(randint(seedStart, seedEnd))
    
    return randomArray