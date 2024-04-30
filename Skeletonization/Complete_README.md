
# Comprehensive Pose Detection and Image Processing System

This repository encompasses a robust system for pose detection integrated with advanced image and data processing techniques to facilitate detailed analysis and processing of pose data.

## Modules

### Pose Detection
1. **model1.py**: Defines the neural network model for initial pose estimation.
2. **poseModule.py**: Utilities for handling pose detection tasks using pre-trained models.
3. **pose_post.py**: Post-processing of pose detection outputs to enhance results.
4. **skeletonize.py**: Converts detected poses into skeleton formats for further analysis.

### Data Handling
5. **data_process.py**: Manages initial data processing tasks like normalization and augmentation.
6. **data_separation.py**: Handles the separation of data into training, testing, and validation sets.
7. **data_preprocess_yolo.py**: Specific preprocessing steps for data to be used with YOLO object detection.
8. **data_combine.py**: Combines various data sources and formats for streamlined processing.

### Image and Signal Processing
9. **cross_corr.py**: Applies cross-correlation techniques for signal analysis.
10. **conversion.py**: Handles conversion between different data and image formats.
11. **UNet_Thick.py**: Implements a U-Net architecture for detailed image segmentation tasks.

### Utilities
12. **basics.py**: Basic utility functions used throughout the system.
13. **utils1.py**: Includes file handling and data manipulation utilities.
14. **metrics.py**: Calculates and outputs performance metrics for the system.
15. **two_stage_pipeline.py**: Orchestrates the entire pipeline, linking all modules for seamless operation from input to output.

## Setup and Installation

1. **Clone the repository**:
```bash
git clone https://github.com/your_username/pose-detection-system.git
```
2. **Install dependencies**:
```bash
pip install opencv-python numpy scikit-image imageai tensorflow keras
```
3. **Run the application**:
```bash
python two_stage_pipeline.py
```


