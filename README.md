# Real-Time Mouse Cursor Control using MediaPipe

This project demonstrates how to control the mouse cursor in real time using MediaPipe, a popular library for computer vision and machine learning tasks. By utilizing hand tracking capabilities, the code allows you to move the mouse cursor on the screen by simply moving your index finger.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This code leverages the MediaPipe library to detect hand landmarks in real time using your webcam feed. By tracking the position of your index finger, it maps the finger's movement to control the mouse cursor on the screen. This project provides a simple and intuitive way to interact with your computer without the need for a physical mouse.

## Installation

To run this code, you need to have the following dependencies installed:

- mediapipe
- pyautogui
- opencv-python

You can install these dependencies using the following command:

pip install mediapipe pyautogui opencv-python


Once the dependencies are installed, you can run the script `mouse_cursor_control.py` to start controlling the mouse cursor in real time.

## Usage

1. Connect a webcam to your computer.
2. Run the script `mouse_cursor_control.py`.
3. Position your hand in front of the webcam, ensuring that it is well-illuminated.
4. Move your index finger to control the mouse cursor. The cursor will follow the movement of your finger.

To stop the program, press the 'q' key.

## Customization

You can customize the code to fit your specific requirements:

- Adjust the `min_detection_confidence` and `min_tracking_confidence` parameters in the code to enhance or relax the hand tracking accuracy threshold.
- Modify the gestures and finger movements to perform different actions, such as clicking, dragging, or scrolling.

Feel free to experiment with the code and tailor it to your needs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to contribute to this project. You can submit issues, fork the repository, or create pull requests.

## License

This project is licensed under the [MIT License](LICENSE).


