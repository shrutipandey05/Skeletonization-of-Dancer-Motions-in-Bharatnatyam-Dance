import os
list1=['1_tatta','2_natta','3_pakka','4_kuditta_mettu','5_kuditta_nattal','6_kuditta_tattal','7_paikkal','8_tei_tei_dhatta','9_katti_kartari','10_uttsanga','11_mandi','12_sarrikal','13_tirmana']
list2=['1','2','3','4','5','6','7','8']
list3=['Dancer1','Dancer2','Dancer3']
import shutil

# Function to copy a file to a specified folder
def copy_file_to_folder(file_path, folder_path):
    try:
        shutil.copy(file_path, folder_path)
        print(f"Copied {file_path} to {folder_path}")
    except shutil.Error as e:
        print(f"Error: {e}")
def rename_files_in_folder(folder_path,new_name):
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
                n_name = "input_"+new_name+"_"+ filename
                new_file_path = os.path.join(folder_path, n_name)
                print(n_name)
                os.rename(file_path, new_file_path)

            elif(filename.startswith("skeleton_")):
                n_name ="output_"+new_name+"_"+ filename
                new_file_path = os.path.join(folder_path, n_name)
                print(n_name)
                os.rename(file_path, new_file_path)
def separate_files(folder_path):
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
            if(filename.startswith("input")):
                print("copying input")
                copy_file_to_folder(file_path,"/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/input")
            elif(filename.startswith("output")):
                print("copying output")
                copy_file_to_folder(file_path,"/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/output")
    
def read_lists():
    const_path="/home/mt0/22CS60R40/UNet-Skeletonization/new_data/Session_1_Data"
    for i in list1:
        path1=os.path.join(const_path,i)
        # print(path1)
        if os.path.isdir(path1):
            for j in list2:
                path2=os.path.join(path1,j)
                
                if os.path.isdir(path2):
                    # print(path2)
                    for k in list3:
                        path3=os.path.join(path2,k)
                        if os.path.isdir(path3):
                            new_name=i+"_"+j+"_"+k
                            separate_files(path3)
                            # rename_files_in_folder(path3,new_name)


def alter_skeleton_names():
    path="/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/binary_output"
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Check if the entry is a file
        if os.path.isfile(file_path):
            l=[]
            l=filename.split("_skeleton_")
            # print(l[0]+'_'+l[1])
            new_name=l[0]+'_'+l[1]
            new_name=new_name.split("output_")[1]
            print(new_name)
            new_file_path = os.path.join(path, new_name)
            # print(n_name)
            os.rename(file_path, new_file_path)
            
def alter_color_names():
    path="/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/binary_input"
    # path="/home/mt0/22CS60R40/UNet-Skeletonization/my_version/yolo_converted_input1"
    i=0
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Check if the entry is a file
        if os.path.isfile(file_path):
            l=[]
            l=filename.split("_color_")
            # print(l[0]+'_'+l[1])
            # print(l)
            new_name=l[0]+'_'+l[1]
            # print(new_name)
            new_name=new_name.split("input_")[1]
            # print(new_name)
            new_file_path = os.path.join(path, new_name)
            os.rename(file_path, new_file_path) 
            i+=1
            print(i) 
 
if __name__=="__main__":
    # read_lists()
    # alter_skeleton_names()
    alter_color_names()
                        
                    
                
            
            
