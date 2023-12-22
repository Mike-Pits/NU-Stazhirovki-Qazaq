import os

import cv2

image_path = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/runs/detect/m_59592/crops/10 Items Table/5959.jpg'
output_path = "/home/mikepi/Coding/Excs/OpenCV/samples/img.jpg"
# image_path = '/home/mikepi/Coding/NU/Stazhirovki/Qazaq_Stroy/scripts/Yolov8/runs/detect/m_59592/crops/10 Items Table/5949.png'
img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 3500:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        x1, y1, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv2.namedWindow('normal', cv2.WINDOW_NORMAL)
cv2.resizeWindow('normal', 1000, 2000)
cv2.imshow('normal', img)
cv2.imwrite(output_path, img)
# cv2.imshow('thresh', thresh)
cv2.waitKey(0)