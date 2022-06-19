
def insertionSort(values = list[int]) -> None:
   """Implementation of insertion sort. This approach compares a value with the former value. If the former value 
   is bigger than the current value, both are swapped. This algorithm works in-place and is stable."""      

   for i, value in enumerate(values, 1):
      # overall run through the entire values array

      j = i - 1
      # j is second search index to grab former value. Set to i - 1 to always grab the value before the current value

      while (j >= 0):

         if values[j] > value:
            # if current value is smaller than the former value, swap both.
           
            temp = values[j]
            values[j] = value
            values[j+1] = temp
           
         # Counter to move backwards within the array. If j == 0 is reached, the beginning of the array is reached and the loop restarts, since
         # there is nothing to compare anymore.
         j -= 1
