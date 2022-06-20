
from random import randint
from typing import Callable


def insertionSort(values: list[int], createRectangles: Callable) -> None:

   """Implementation of insertion sort. This approach compares a value with the former value. If the former value 
   is bigger than the current value, both are swapped. This algorithm works in-place and is stable."""      


   if len(values) == 0:
      return

   for forwardCounter, currentValue in enumerate(values, 1):
      # overall run through the entire values array

      backwardCounter = forwardCounter - 1
      # j is second search index to grab former value. Set to i - 1 to always grab the value before the current value

      while (backwardCounter >= 0):

         if values[backwardCounter] > currentValue:
            # if current value is smaller than the former value, swap both.
           
            #temporaryValue = values[backwardCounter]
            values[backwardCounter], values[backwardCounter+1] = currentValue, values[backwardCounter]
            #values[backwardCounter+1] = temporaryValue
           
            createRectangles(values)
            # updates the GUI, according to the current values of the values list
         

         backwardCounter -= 1
         # Counter to move backwards within the array. If j == 0 is reached, the beginning of the array is reached and the while loop ends. 
         # Returns to the for loop, increases i, meaning grabbing the next value in the array and restart overall sorting.

