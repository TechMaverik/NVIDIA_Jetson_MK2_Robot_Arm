"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
import cv2
import matplotlib.pyplot as plt

import numpy as np
def calculate_cendroid(x, y, w, h):
    x1=int(w/2)
    y1=int(h/2)
    cx = x+x1
    cy=y+y1
    return cx, cy


camera=cv2.VideoCapture(0)
result,image=camera.read()
cv2.imwrite("RealInstance.jpg",image)
input_img = cv2.imread("RealInstance.jpg")
img = cv2.resize(input_img, (1280, 960))
# Make a copy to draw contour outline
input_image_cpy = img.copy()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# define range of green color in HSV
lower_green = np.array([40, 20, 50])
upper_green = np.array([90, 255, 255])

# define range of blue color in HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# create a mask for red color
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# create a mask for green color
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# create a mask for blue color
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# find contours in the red mask
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# find contours in the green mask
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# find contours in the blue mask
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.line(img, (552,677), (552,76), (0,0,255), 2) 
# cv2.line(img, (712,677), (712,79), (0,0,255), 2) 

# loop through the red contours and draw a rectangle around them
for cnt in contours_red:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)            
        cv2.putText(img, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
# loop through the green contours and draw a rectangle around them
for cnt in contours_green:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)            
        cv2.putText(img, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# loop through the blue contours and draw a rectangle around them
for cnt in contours_blue:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)            
        cv2.putText(img, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        cx,cy=calculate_cendroid(x,y,w,h)
        
        cv2.circle(img, (cx,cy), 1, (0,0,255), 2)
        print(cx,cy)
        # if(cx>552 and cx<712):
        #     print(cx,cy)
            # print("within")
            # if(cx>552 and cx<625):
            #     print("1st operation")
            # if(cx>625 and cx<635):
            #     print("2nd operation")
            # if(cx>635 and cx<665):
            #     print("3rd operation")
            # if(cx>665 and cx<675):
            #     print("4th operation")
            # if(cx>675 and cx<712):
            #     print("5th operation")
    # RPP.trigger_action()

# Display final output for multiple color detection opencv python
cv2.imshow('Color Engine Saves', img)
cv2.waitKey(0)
cv2.destroyAllWindows()