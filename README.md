# Hand Gesture Control using MediaPipe and PyAutoGUI

This code allows you to control your mouse cursor using hand gestures captured from a webcam. It utilizes the MediaPipe library for hand detection and tracking, and the PyAutoGUI library for mouse control.

## Introduction

Hand gesture control is an emerging technology that enables users to interact with computers and devices in a more intuitive and natural way. This project utilizes the MediaPipe library, developed by Google, for real-time hand detection and tracking. The detected hand landmarks are then used to perform mouse cursor control operations using the PyAutoGUI library.

The code provides a user-friendly interface where hand gestures are recognized and mapped to specific mouse actions. By closing the index finger and thumb, users can perform a click action, while moving the index finger controls the movement of the mouse cursor. This allows for hands-free control of the computer interface, offering an alternative input method.

## Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

Before running the code, make sure you have the following libraries installed:

- OpenCV (cv2)
- MediaPipe (mediapipe)
- PyAutoGUI (pyautogui)

You can install these libraries using pip:

pip install opencv-python mediapipe pyautogui


## Usage

1. Connect a webcam to your computer.

2. Run the code using the Python interpreter:


3. A window will open showing the live webcam feed with hand landmarks and mouse cursor control.

4. Place your hand in front of the webcam. The index finger and thumb gestures are recognized.

5. Close your index finger and thumb to perform a click action.

6. Move your index finger while keeping the thumb open to move the mouse cursor.

7. Press the 'q' key to exit the program.

## Configuration

You can adjust the following parameters in the code:

- `max_num_hands`: Maximum number of hands to detect (default: 1).
- `min_detection_confidence`: Minimum confidence value for hand detection (default: 0.5).
- `min_tracking_confidence`: Minimum confidence value for hand tracking (default: 0.5).

Feel free to modify these parameters to achieve the desired performance and accuracy.

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
