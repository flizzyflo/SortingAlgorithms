
import math


def splitArray(values: list[int]) -> list[int]:
    """Calculates a divider and splits the array in its half, returning a single value as soon as 
    the length of the passed argument is 1. This algorithm does not work in-place, but is stable."""

    if len(values) <= 1:
        return values

    else:
        divider: int = math.floor(len(values) / 2)
        # Calculate a divider in the middle of the passed in values array to split the array in its middle.
        # Pass both arrays into the recursive call, and split them again, and merge both values as soon as 
        # the recursive base condition is met.

        return mergeSort(splitArray(values[:divider]), splitArray(values[divider:]))
        

def mergeSort(leftValues: list[int], rightValues: list[int]) -> list[int]:     
    """Merge sorting algorithm, which zips together both of the two seperate lists.
    Takes two already sorted arrays as input and puts them together."""

    resultArray = []
    lenghtLeft = len(leftValues)
    lengthRight = len(rightValues)

    for _ in range(lenghtLeft + lengthRight):
        # overall run through the entire values of both arrays
        
        if len(leftValues) == 0:
            # if the left values array is empty, that means all values in
            # the rightValues array are bigger. Thus, they can be added to the result array

            for value in rightValues:
                resultArray.append(value)
            return resultArray
        
        elif len(rightValues) == 0:
            # if the rightValues array is empty, that means all values in
            # the leftValues array are bigger. Thus, they can be added to the result array

            for value in leftValues:
                resultArray.append(value)
            return resultArray

        if leftValues[0] <= rightValues[0]:
            # if the current value of the leftValues array is lower
            # than the current value of the right array, pass leftValue 
            # into the result array and pop it from leftValue array.

            resultArray.append(leftValues.pop(0))
            continue

        elif rightValues[0] < leftValues[0]:
            # if the current value of the rightValues array is lower
            # than the current value of the leftValues array, pass rightValue 
            # into the result array and pop it from rightValue array.

            resultArray.append(rightValues.pop(0))
            continue

    return resultArray

