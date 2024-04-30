import os
import shutil

# Function to copy a file to a specified folder
def copy_file_to_folder(file_path, folder_path):
    try:
        shutil.copy(file_path, folder_path)
        print(f"Copied {file_path} to {folder_path}")
    except shutil.Error as e:
        print(f"Error: {e}")

# Define the file paths and folder paths

# file_paths = "/home/mt0/22CS60R40/UNet-Skeletonization/Dancer1" 
file_paths="/home/mt0/22CS60R40/UNet-Skeletonization/tatta3/Dancer3"
# print("love u ")
# listt=["t1_d1_input",""]
for file_path in os.listdir(file_paths):
    print(file_path)
    if("input" in file_path):
        copy_file_to_folder(os.path.join(file_paths,file_path), "/home/mt0/22CS60R40/UNet-Skeletonization/Dataset/rgb_input")
    elif("output" in file_path):
        copy_file_to_folder(os.path.join(file_paths,file_path),"/home/mt0/22CS60R40/UNet-Skeletonization/Dataset/rgb_output")
        
