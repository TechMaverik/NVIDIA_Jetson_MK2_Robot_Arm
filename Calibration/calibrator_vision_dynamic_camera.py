"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
import cv2
import numpy as np

class VisionCalibrator:
    cam = cv2.VideoCapture(0)

    def calculate_cendroid(x, y, w, h):
            x1=int(w/2)
            y1=int(h/2)
            cx = x+x1
            cy=y+y1
            return cx, cy

    while True:
        
        check, frame = cam.read()
        frame = cv2.resize(frame, (1280, 960))
        cv2.line(frame, (2,300), (1276,300), (0,0,255), 2) 
        cv2.line(frame, (200,1), (200,1024), (255,255,0), 2) 
        cv2.line(frame, (800,1), (800,1024), (255,255,0), 2) 

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([130, 255, 255])
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
        for cnt in contours_blue:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)            
                cv2.putText(frame, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                cx,cy=calculate_cendroid(x,y,w,h)           
                cv2.circle(frame, (cx,cy), 1, (0,0,255), 2)

                if(cy>300):
                    print(cx,cy)

        cv2.imshow('Calibrator', frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cam.release()
    cv2.destroyAllWindows()