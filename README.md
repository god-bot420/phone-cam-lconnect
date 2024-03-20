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
```
Setting Up the Android IP Webcam:
Install an IP Webcam app on your Android device. Many free options are available in the Google Play Store.
Open the app and start the server. Note the IP address and port displayed (e.g., http://192.168.29.122:8080).
Ensure your computer and Android device are connected to the same network.
Running the Application
Replace the url variable's value in the script with the IP address and port from your IP Webcam app:

```bash
url = "http://<Your_IP_Webcam_IP>:<Port>/shot.jpg"
```

Run the script with Python:
```bash
python android_cam_qr_code_scanner.py
```
Usage
Place QR codes in front of your Android device's camera to scan them.
The application window will display the camera feed and scanned QR code data.
Press the Esc key to exit the application.
Contributing
Feel free to fork this repository, contribute, or suggest improvements via pull requests and issues.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

Acknowledgments
OpenCV for the computer vision library.
Pyzbar for QR code and barcode decoding.
Imutils for basic image processing convenience functions.
Requests for HTTP requests in Python.
