
def bubbleSort(values: list[int]) -> None:
    """Implementation of bubble sort. This sorting algorithm grabs a number an swithces it with the next number, if the next one is less. The grabed number
    "marches" through the list until a number bigger than itself is found. Then,the biggest number is at the end of the array and the process is repeated
    until the whole array is sorted. This algorithm works in-place and is stable."""

    for run in range(len(values)):
        # overall run through the entire values array

        for index, value in enumerate(values):

            if (index + 1) > len(values) - 1:
                continue

            if values[index] > values[index + 1]:  
                # If next value is smaller than current value, swap both.

                temporary_object: object = values[index + 1]
                values[index + 1] = value
                values[index] = temporary_object
                
            else:
                continue

