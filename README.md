Welcome to my repository about my self project dubbed (albeit not so originally) as the **Live Sudoku Solver**. Through this project, I aim to learn and apply techniques for data extraction from images, making a neural net to classify printed numbers and then finally, to solve the ever cumbersome problem of the unsolved daily newspaper puzzle!!

### What does this project do
This project is defined in **2 stages**:
- Stage 1 involves
  * development and training of a neural network that is able to **idetify the digits** from an uploaded image of a **printed sudoku puzzle**
  * peicing together the image to **reconstruct the puzzle**
  * utilize an algorithm to solve the puzzle then display the final solved grid
 
- Stage 2 involves
  * rework the program to take in **live camera feed** as its input, identify the digits from the feed itself
  * the **puzzle gets constructed** based on the data proccesed from live feed
  * the puzzle is then solved and the solution is then **superimposed on the live feed image** and display on the computer screen
  * the result would a **modified camera live feed** with the empty boxes of the puzzle filled with the current number

**NOTE -** Stage 2 is subject to change as the project progresses

### The To-Do list
- construct an algorithm (preferable on your own) to solve a given sudoku (which is given as input from the console)
  * write algorithm in Python and C++
- construct a neural network that can identify the **individual boxes** and classify **printed digits** with a sufficient enough accuracy
  * identify the complete puzzle's outer boundaries
  * identify **individual boxes** of numbers and correctly classify the number within with good enough accuracy
- reconstruct the puzzle in the algorithm appropriate format
  * correctly detect the ordering of the elements to reproduce the sudoku
- solve the sudoku and display it as an output

Article that inspired this project - Sudoku Solver using Computer Vision and Deep Learning [Part 1](https://aakashjhawar.medium.com/sudoku-solver-using-opencv-and-dl-part-1-490f08701179) [Part 2](https://aakashjhawar.medium.com/sudoku-solver-using-opencv-and-dl-part-2-bbe0e6ac87c5)  
Tracking Progress via a [doc](https://docs.google.com/document/d/1kK3xpeCEI2OSuNLdxyedZndlmpJeOXm3psKB9WDqKms/edit?usp=sharing) that is the primary update log for this project  
