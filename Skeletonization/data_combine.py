import os

def rename_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the entry is a file
        if os.path.isfile(file_path):
            # Extract the file extension
            _, extension = os.path.splitext(filename)

            # New name (you can customize the new name as needed)
            if(filename.startswith("color_USB")):
                new_name = "t3_d3_input_" + filename
                new_file_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_file_path)

            elif(filename.startswith("skeleton_")):
                new_name = "t3_d3_output_" + filename
                new_file_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_file_path)

import os

def delete_files_starting_with(folder_path, prefix):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    count_deleted = 0

    for filename in os.listdir(folder_path):
        if filename.startswith(prefix):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            count_deleted += 1
            print(f"Deleted file: {filename}")

    print(f"Total files deleted: {count_deleted}")


def remove_string_from_filenames(folder_path, string_to_remove):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    count_renamed = 0

    for filename in os.listdir(folder_path):
        if string_to_remove in filename:
            # Replace the string with an empty string to remove it
            new_filename = filename.replace(string_to_remove, "")
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)

            os.rename(old_filepath, new_filepath)
            count_renamed += 1
            print(f"Renamed '{filename}' to '{new_filename}'.")

    print(f"Total files renamed: {count_renamed}")
       
if __name__ == "__main__":
    # folder_path1 ="/home/mt0/22CS60R40/UNet-Skeletonization/tatta1/Dancer1"#change the path everytime
   #to rename files with specific convention run this function otherwise comment
#    rename_files_in_folder(folder_path1)
   #select prefix or prfix2 whatever required
    # prefix = "depth"  # Prefix to match for file deletion
    # prefix2="USB-VID"
    #run this to delete depth and mat files
    #call this fucntion 2 times
    # delete_files_starting_with(folder_path1, prefix)
    folder_path="/home/mt0/22CS60R40/UNet-Skeletonization/Dataset/binary_input"
    st="_input_color"
    remove_string_from_filenames(folder_path,st)

