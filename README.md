# Face Recognition System using OpenCV

## Overview
A real-time face recognition system developed using Python and OpenCV that detects and recognizes faces through a webcam. The project utilizes the Haar Cascade algorithm for face detection and the LBPH (Local Binary Patterns Histograms) algorithm for face recognition.

## Features
- Real-time face detection using a webcam
- Face dataset collection and image preprocessing
- Face recognition using the LBPH algorithm
- Displays the recognized user's name in real time
- Ability to identify unknown faces

## Technologies Used
- Python
- OpenCV
- NumPy
- Haar Cascade Classifier
- LBPH Face Recognizer

## Project Structure
- `capture.py` – Captures and stores facial images.
- `train.py` – Trains the face recognition model and generates the trained data file.
- `recognize.py` – Performs real-time face recognition using the trained model.

## How to Run
1. Run `capture.py` to collect facial images.
2. Run `train.py` to train the recognition model.
3. Run `recognize.py` to perform real-time face recognition.

## Future Enhancements
- Multi-user face recognition support
- Database integration for storing user information
- Improved accuracy using deep learning-based face recognition models

## Author
**Shahaana**
