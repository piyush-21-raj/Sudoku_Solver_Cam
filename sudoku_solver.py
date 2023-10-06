import numpy as np

def check_valid_entry(grid, row, col, num):
    """returns boolen value after checking if the entry is valid or not"""
    # Check if the number is already present in the row
    if num in grid[row]:
        return False
    # Check if the number is already present in the column
    for i in range(n):
        if num == grid[i][col]:
            return False
    # Check if the number is already present in the subgrid
    subgrid_row = row//3
    subgrid_col = col//3
    for i in range(subgrid_row*3, subgrid_row*3 + 3):
        for j in range(subgrid_col*3, subgrid_col*3 + 3):
            if num == grid[i][j]:
                return False
    return True

def solve_sudoku(grid, row, col):
    """returns boolean value after solving the sudoku problem"""
    # Check if the last column has been reached
    if col == n:
        col = 0
        row += 1
        if row == n:
            return True # Sudoku has been solved
    
    # Check if the entry is already filled
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col+1)
    
    # Fill the entry
    for num in range(1,10):
        if check_valid_entry(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col+1):
                return True
        grid[row][col] = 0
    return False


# Input the dimension of the sudoku
n = int(input("Enter the dimension of the sudoku: "))
sudoku_problem = np.zeros((n,n))

# Input the sudoku problem
for i in range(n):
    for j in range(n):
        try:
            entry = int(input(f"Enter the value for row {i+1} and column {j+1}: "))
            if entry in np.arange(1,10):
                sudoku_problem[i][j] = entry
        except Exception as e:
            pass

# Solve the sudoku problem
if solve_sudoku(sudoku_problem, 0, 0):
    print("Sudoku has been solved")
    print(sudoku_problem)
else:
    print("Sudoku cannot be solved")