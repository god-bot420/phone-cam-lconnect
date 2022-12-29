
# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import pyzbar.pyzbar as pyzbar
url = "http://192.168.29.122:8080/shot.jpg"
font = cv2.FONT_HERSHEY_PLAIN
# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1080, height=2420)
    decodedObjects = pyzbar.decode(img)
    for obj in decodedObjects:
        print("Data", obj.data)
        cv2.putText(img, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
    cv2.imshow("Android_cam", img)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
