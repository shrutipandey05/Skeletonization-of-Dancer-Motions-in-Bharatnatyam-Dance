from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
def rename_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for file_name in files:
       
        new_file_name = file_name
        new_file_name = new_file_name[9:]
        new_file_name = 'color_' +new_file_name


        # Construct the full paths for old and new file names
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {file_name} to {new_file_name}")
        
        
def new_images():
    input_dir = '/home/mt0/22CS60R40/UNet-Skeletonization/Dataset/binary_input'  # Replace with your input directory containing images

# Target dimensions for resizing
    target_width = 256
    target_height = 256

    # Iterate through each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):  # Check if it's an image file
            input_path = os.path.join(input_dir, filename)

            # Open the image
            img = Image.open(input_path)

            # Resize the image
            resized_img = img.resize((target_width, target_height))

            # Overwrite the original image with the resized image
            resized_img.save(input_path)
def convert_rgb_to_binary(input_folder, output_folder):
    print("1111")
    image_files = [f for f in os.listdir(input_folder)]
    print(image_files)
    for file_name in image_files:
        image_path = os.path.join(input_folder, file_name)
        if os.path.exists(image_path):
            img = Image.open(image_path)
            grayscale_img = img.convert('L')
            threshold=60
            # Threshold the grayscale image to create a binary image
            binary_img = grayscale_img.point(lambda p: p > threshold and 255)

            # Save the binary image to the output folder
            output_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}_binary.jpg')
            print("saving")
            binary_img.save(output_path)
        # image_path = os.path.join(input_folder, file_name)
        # img = Image.open(image_path)
        # binary_img = img.convert('1')

        # # Save the binary image to the output folder
        # output_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.png')
        # binary_img.save(output_path)

def foreground_extraction(input_folder, output_folder):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png'))]

    for file_name in image_files:
        image_path = os.path.join(input_folder, file_name)
        
        rgb_image =io.imread(image_path)
        print(rgb_image.shape)
        reshaped_image = np.reshape(rgb_image, (-1, 3))

        # Perform PCA
        pca = PCA(n_components=3)
        pca.fit(reshaped_image)

        # Choose components
        selected_components = pca.components_[:8]

        # Project data onto selected components
        projected_data = np.dot(reshaped_image, selected_components.T)

        # Apply K-means clustering
        kmeans = KMeans(n_clusters=5, random_state=0)
        kmeans.fit(projected_data)

        # Get labels and reshape to original image shape
        segmented_image = np.reshape(kmeans.labels_, rgb_image.shape[:2])

        # Separate foreground and background based on clustering labels
        foreground = (segmented_image == kmeans.labels_[0]) * 255
        background = (segmented_image == kmeans.labels_[1]) * 255
        output_path = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}_binary.png')
        print("saving")
        # foreground.save(output_path)
        io.imsave(output_path, foreground.astype(np.uint8))
    
if __name__ == "__main__":
    # Input folder containing RGB images
    input_folder = '/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/yolo_converted_output1'
    print("2222")
    # # Output folder where binary images will be saved
    output_folder = '/home/mt0/22CS60R40/UNet-Skeletonization/my_version/Dataset/binary_output_yolo'
    print("33333")
    # # Convert RGB images to binary and save them to the output folder
    convert_rgb_to_binary(input_folder, output_folder)
    # foreground_extraction(input_folder,output_folder)
    print("4444")
    # rename_files_in_folder('/home/mt0/22CS60R40/UNet-Skeletonization/dataset/binary_output')
    # new_images()