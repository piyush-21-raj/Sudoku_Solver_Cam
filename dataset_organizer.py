import os
import shutil

# Define the path to the folder containing the dataset
dataset_folder = 'D:\Sudoku_Solver\SOLUTION\dataset'

# Iterate over all the files in that folder
for filename in os.listdir(dataset_folder):
    # Skip directories, only process files
    if os.path.isfile(os.path.join(dataset_folder, filename)):
        # Get the first character of the file name
        first_number = filename[0]
        
        # Define the path to the new folder based on the first number
        new_folder = os.path.join(dataset_folder, first_number)
        
        # Create the new folder if it doesn't exist
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        
        # Move the file to the new folder
        shutil.move(os.path.join(dataset_folder, filename), os.path.join(new_folder, filename))

print("Files have been successfully moved.")
