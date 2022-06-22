import math

def splitArray(values: list[int]) -> list[int]:
    
    """Calculates a divider and splits the array in its half, returning a single value as soon as 
    the length of the passed argument is 1. This algorithm does not work in-place, but is stable."""

    if values == []:
        return

    if 0 < len(values) <= 1:
        return values

    else:
        arrayDivider: int = math.floor(len(values) / 2)
        # Calculates a divider in the middle of the passed in values array to split the array in its middle.
        # Pass both arrays into the recursive call, and split them again, and merge both values as soon as 
        # the recursive base condition is met.

        return mergeArrays(splitArray(values[:arrayDivider]), splitArray(values[arrayDivider:]))
        

def mergeArrays(leftValuesArray: list[int], rightValuesArray: list[int]) -> list[int]:

    """Main merge sorting algorithm, which zips together both of the two seperate lists.
    Takes two already sorted arrays as input and puts them together."""

    resultArray = []
    lenghtLeftArray = len(leftValuesArray)
    lengthRightArray = len(rightValuesArray)

    for _ in range(lenghtLeftArray + lengthRightArray):
        # overall run through the entire values of both arrays
        
        if (len(leftValuesArray) == 0) and (len(rightValuesArray) > 0):
            # if the left values array is empty, that means all values in
            # the rightValues array are bigger. Thus, they can be added to the result array

            for value in rightValuesArray:
                resultArray.append(value)
            return resultArray
        
        elif (len(rightValuesArray) == 0) and (len(leftValuesArray) > 0):
            # if the rightValues array is empty, that means all values in
            # the leftValues array are bigger. Thus, they can be added to the result array

            for value in leftValuesArray:
                resultArray.append(value)
            return resultArray

        if leftValuesArray[0] <= rightValuesArray[0]:
            # if the current value of the leftValues array is lower
            # than the current value of the right array, pass leftValue 
            # into the result array and pop it from leftValue array.

            resultArray.append(leftValuesArray.pop(0))
            continue

        elif rightValuesArray[0] < leftValuesArray[0]:
            # if the current value of the rightValues array is lower
            # than the current value of the leftValues array, pass rightValue 
            # into the result array and pop it from rightValue array.

            resultArray.append(rightValuesArray.pop(0))
            continue

  
    return resultArray
