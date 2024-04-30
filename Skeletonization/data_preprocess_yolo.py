import cv2 as cv
from imageai.Detection import ObjectDetection
from tensorflow.keras.layers import BatchNormalization
import numpy as np
import requests as req
import os as os
import random
# peopleImages = os.listdir("people")
# randomFile = peopleImages[random.randint(0, len(peopleImages) - 1)]
import cv2
import shutil

    
def foreground_extraction(input_folder,detector):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png'))]
    i=0
    for file_name in image_files:
        i+=1
        image_path = os.path.join(input_folder, file_name)
        detectedImage, detections = detector.detectObjectsFromImage(output_type="array", input_image=image_path, minimum_percentage_probability=30)
        convertedImage = cv2.cvtColor(detectedImage, cv2.COLOR_RGB2BGR)
        
        for eachObject in detections:
            xmin, ymin, xmax, ymax = eachObject["box_points"]

        # Crop the image using the bounding box coordinates
            cropped_image = convertedImage[ymin:ymax, xmin:xmax]

        # Save or display the cropped image
        if (i<5000):
            cv2.imwrite('/home/mt0/22CS60R40/UNet-Skeletonization/my_version/yolo_converted_input1/{}'.format(file_name), cropped_image)
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            print(i)
            print("--------------------------------")
        else:
            break
        
        
def copy_and_rename_file(original_path, original_filename, new_filename, destination_folder):
    original_file_path = os.path.join(original_path, original_filename)
    new_file_path = os.path.join(destination_folder, new_filename)
    shutil.copy(original_file_path, new_file_path)
    
    
def corresponding_skeleton(input_folder1,input_folder2,output_path):
    image_files1 = [f for f in os.listdir(input_folder1) if f.endswith(('.png'))]
    image_files2 = [f for f in os.listdir(input_folder2) if f.endswith(('.png'))]
    # image_files3 = [f for f in os.listdir(output_path) if f.endswith(('.png'))]
   
    new=[]
    i=0
    for file_names1 in image_files1:
        new=file_names1.split("input_")
        print(file_names1)
        l=new[1].split("_color_")
        # print(l[0]+'_'+l[1])
        name1=l[0]+'_'+l[1]
        for file_names2 in image_files2:
            new=file_names2.split("_binary")
            name2=new[0]+".png"
            if(name1==name2):
                i+=1
                print(i)
                file_path = os.path.join(output_path, name2)
                copy_and_rename_file(input_folder2,file_names2,name2,output_path)


from PIL import Image

def convert_jpg_to_png(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter JPG files
    jpg_files = [file for file in files ]
    print(len(jpg_files))
    # Convert each JPG file to PNG
    # for jpg_file in jpg_files:
    #     # Construct the paths
    #     jpg_path = os.path.join(folder_path, jpg_file)
    #     print(jpg_file.split(".jpg")[0])
    #     png_file = jpg_file.split(".jpg")[0] + '.png'  # change the extension to PNG
    #     png_path = os.path.join(folder_path, png_file)
        
    #     # Open and convert the image
    #     image = Image.open(jpg_path)
    #     image.save(png_path, format='PNG')
        
    #     print(f"Converted {jpg_file} to {png_file}")   
    


if __name__ == "__main__":
    print("ENTER VALUE OF n:\n")
    n=int(input())
    if n==1:
        detector = ObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath('/home/mt0/22CS60R40/UNet-Skeletonization/my_version/yolov3.pt')
        detector.loadModel()
        foreground_extraction("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/input",detector)
    elif n==2:
        corresponding_skeleton("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/yolo_converted_input1","/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/binary_output","/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/yolo_converted_output1")
    elif n==3:
        convert_jpg_to_png("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/binary_input_yolo")
    elif n==4:
        img=Image.open("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/input/input_2_natta_1_Dancer2_color_USB-VID_045E&PID_02BF-0000000000000000_658.png")
        img.save("/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/input_2_natta_1_Dancer2_color_USB-VID_045E&PID_02BF-0000000000000000_658.png",format='PNG')
        
        
    
