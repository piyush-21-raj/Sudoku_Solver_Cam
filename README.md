Welcome to my repository about my self project dubbed (albeit not so originally) as the **Live Sudoku Solver**.

Through this project, I aim to learn and apply techniques for data extraction from images, making a neural net to classify printed numbers and then finally, to solve the ever cumbersome problem of the unsolved daily newspaper puzzle!!

### How does this project work
This project can divided into **3 major tasks**:
- Stage 1: **EXTRACTION**
  * identify the presence of a **sudoku puzzle** from a live feed or from an uploaded image
  * identify the puzzle boundaries and **extract individual boxes** of the puzzle
  * pull and **preprocess the image** of each box **sequentially**
 
- Stage 2: **IDENTIFY and SOLVE**
  * train a CNN classifier to **idetify digits** with reasonable speed and accuracy
  * pass each box image and **re-construct the puzzle** locally in arrays
  * use a **backtracking** algorithm to return the solved puzzle

- Stage 3: **DISPLAY**
  * use the solved array to **fill the empty boxes** in the extracted puzzle image
  * **warp the extracted image back onto the video feed** for a live display of the solution
