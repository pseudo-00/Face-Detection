# pip install opencv-python
# haarcascade_frontalface_default.xml

import cv2

haarcascade_file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while True:
    c_rec, d_image = webcam.read()
    grey_image = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = haarcascade_file.detectMultiScale(grey_image, 1.3,6)

    for (x1,y1, w1,h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1+w1, y1+h1), (0,255,0), 2)

    cv2.imshow('img', d_image)
    wait_key = cv2.waitKey(40) & 0xff

    if wait_key == 40:
        break

webcam.release()
cv2.destroyAllWindows()