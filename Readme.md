# Search Algorithm Visualization

## Work in progress 

This programm will visualize different sorting algorithms and how they work. 
The sorting will be presented within a tkinter canvas. Different sort algorithms are going to be implemented.
Program consists out of several classes to perform all the tasks required. The separate folder contain the files as follows:

### Rectangles 
Class to create and manage the rectangles, which will represent the values on the canvas GUI of the tool.
Class as well takes care of the values list itself to ensure that the values are not just sorted visually, but in the list in reality as well.

### GraphicalUserInterface
Represents the tkinter Gui and manages everything related with it.

### Sorting Algorithms (not a class, but a folder)
Contains the single sorting algorithms which were used in this tool, stored in a separate file each. Furthermore, the folder contains a testing file as well as a random array creator. Will be updated with more and more sorting algorithms over time.

### Settings
Guess thats clear... File contains several constants which are used all over the whole programm. Bundled in this file to keep the other files more clear as well as to have anything in a central, separate file.
