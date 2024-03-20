# Android Camera QR Code Scanner

## Introduction
This project showcases a simple yet powerful application that utilizes an Android device's camera to scan QR codes in real-time. By leveraging the OpenCV and Pyzbar libraries, the script processes the camera feed accessed via an IP webcam server and decodes QR codes present in the frame. This README guides you through setting up the project, dependencies required, and how to get the system running.

## Features
- **Real-Time QR Code Scanning**: Instantly decodes QR codes from the video stream.
- **Utilizes Android Camera**: Uses an Android device's camera as the video source through an IP webcam server.
- **Display Decoded Information**: Shows the decoded QR code data directly on the video feed.

## Prerequisites
To run this application, you'll need the following installed on your system:
- Python 3.x
- OpenCV library for Python
- Imutils library
- Pyzbar library
- An Android device with an IP Webcam app installed

## Installation

### Install Python Dependencies
First, ensure you have Python installed. Then, install the necessary Python libraries using pip:
```bash
pip install numpy opencv-python imutils pyzbar requests
