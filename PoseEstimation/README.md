
# Pose Detection System

This repository contains the Python code for a real-time pose detection system using OpenCV and pre-trained Caffe models.

## Modules

1. **main.py**: The main execution script that allows users to select between different detection modes (Full Body Detection and Hand Detection). It utilizes multithreading to handle video capture and pose estimation simultaneously.
   
2. **detector.py**: Contains the `PoseEstimator` class that loads the specified pre-trained model and performs pose detection. It processes video frames to locate points of interest (joints) and connects them to form the detected pose.

3. **camera.py**: Implements the `CameraThread` class, a threaded video capture mechanism that ensures smooth frame acquisition from the default or specified video source. It manages frame reading within its own thread to prevent video capture delays from affecting pose detection.

## Features

- **Mode Selection**: Users can choose the type of pose detection at runtime:
  - `1` for Full Body Detection
  - `2` for Hand Detection
- **Multithreading**: Utilizes threading to handle video capture and processing efficiently.
- **Real-Time Detection**: Processes and displays the pose detection in real-time.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/pose-detection-system.git
   ```
2. **Install dependencies**:
   ```bash
   pip install opencv-python
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```

Ensure you have the necessary Caffe model files in a `models/` directory as outlined in `main.py`:

- Full Body Model: `models/pose/pose_deploy_linevec_faster_4_stages.prototxt` and `models/pose/pose_iter_160000.caffemodel`
- Hand Model: `models/hand/pose_deploy.prototxt` and `models/hand/pose_iter_102000.caffemodel`
