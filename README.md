# Face Detection

This project demonstrates real-time face detection using OpenCV and a Haar Cascade classifier.

## Prerequisites

- Python 3.x
- OpenCV library

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd Face Detection
    ```

2. Install the required Python packages:
    ```sh
    pip install opencv-python
    ```

3. Ensure you have the Haar Cascade XML file (`haarcascade_frontalface_default.xml`) in the project directory.

## Usage

Run the face detection script:
```sh
python face_detection.py
```

The script will open your webcam and start detecting faces in real-time. Press the Esc key to exit the application.

## Project Structure

```
Face Detection/
├── face_detection.py
├── haarcascade_frontalface_default.xml
└── test.py
```

## How It Works

- The script initializes the Haar Cascade classifier with the haarcascade_frontalface_default.xml file.
- It opens the webcam and starts capturing frames.
- Each frame is converted to grayscale.
- The classifier detects faces in the grayscale image.
- Detected faces are highlighted with rectangles in the original frame.
- The frame is displayed in a window.
- Press the Esc key to exit the application.
