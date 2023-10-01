"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""

import cv2
import numpy as np
from Mathematical_Models.motion_planning import MotionPlanning
from MotionDriver.generic_driver import GenericDriver
 
class ColorEngine_Static_Camera:

    def __init__(self):
        self.Flag=0

    def calculate_cendroid(self,x, y, w, h):
        x1=int(w/2)
        y1=int(h/2)
        cx = x+x1
        cy=y+y1
        return cx, cy

    def take_picture(self):
        GenericDriver().scan()
        camera=cv2.VideoCapture(0)
        result,image=camera.read()
        cv2.imwrite("Processed_Image/color_body_source.jpg",image)

    def process_selected_image(self):
        input_img = cv2.imread("Processed_Image/color_body_source.jpg")
        img = cv2.resize(input_img, (1280, 1024))          
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
        # loop through the red contours and draw a rectangle around them

        cv2.line(img, (2,250), (1276,250), (0,0,255), 2) 
        cv2.line(img, (456,695), (456,1), (255,255,0), 2) 
        cv2.line(img, (858,703), (858,1), (255,255,0), 2)      
        

        # loop through the blue contours and draw a rectangle around them
        for cnt in contours_blue:            
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                cx,cy=self.calculate_cendroid(x,y,w,h)
                cv2.circle(img, (cx,cy), 1, (0,0,255), 2)
                if(cy>250):
                    print(cx,cy)
                    mPEngine=MotionPlanning()
                    theta1,theta2=mPEngine.auto_motion_algorithm(cy)
                    print(theta1,theta2)
                    GenericDriver().trigger_motion("Blue",theta1,theta2)
        cv2.imwrite("Processed_Image/tracked_color_object.jpg",img)
        print("[MK2 ROBOT VISION WAITING ...]")


class ColorEngine_Dynamic_Camera:

    def __init__(self):
        self.Flag=0

    def calculate_cendroid(self,x, y, w, h):
        x1=int(w/2)
        y1=int(h/2)
        cx = x+x1
        cy=y+y1
        return cx, cy

    def take_picture(self):        
        camera=cv2.VideoCapture(0)
        result,image=camera.read()
        cv2.imwrite("Processed_Image/color_body_source.jpg",image)

    def process_selected_image(self,base_angle):
        arm_return_status=False
        input_img = cv2.imread("Processed_Image/color_body_source.jpg")
        img = cv2.resize(input_img, (1280, 1024))          
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
        # loop through the red contours and draw a rectangle around them
    
        cv2.line(img, (2,300), (1276,300), (0,0,255), 2) 
        cv2.line(img, (18,1), (18,1024), (255,255,0), 2) 
        cv2.line(img, (1143,1), (1143,1024), (255,255,0), 2)        

        status=False
        # loop through the blue contours and draw a rectangle around them
        for cnt in contours_blue:            
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                cx,cy=self.calculate_cendroid(x,y,w,h)
                cv2.circle(img, (cx,cy), 1, (0,0,255), 2)
                if(cy>300 and cx>75 and cx <1151):
                    print("cx:",str(cx),"cy:",str(cy))                    
                    mPEngine=MotionPlanning()
                    try:
                        theta1,theta2=mPEngine.auto_motion_algorithm_dynamic_camera(cy)
                        print("Theta1",theta1,"Theta2",theta2)
                        GenericDriver().trigger_motion("Blue",theta1,theta2,base_angle)
                        status=True
                    except:
                        print("[MK2 Beyond Reach. Kindly RESET and start over the application]")
        
    
        # loop through the green contours and draw a rectangle around them
        for cnt in contours_green:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)            
                cv2.putText(img, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cx,cy=self.calculate_cendroid(x,y,w,h)
                cv2.circle(img, (cx,cy), 1, (0,0,255), 2)
                if(cy>300 and cx>75 and cx <1151):
                    print("cx:",str(cx),"cy:",str(cy))                    
                    mPEngine=MotionPlanning()
                    try:
                        theta1,theta2=mPEngine.auto_motion_algorithm_dynamic_camera(cy)
                        print("Theta1",theta1,"Theta2",theta2)
                        GenericDriver().trigger_motion("Green",theta1,theta2,base_angle)
                        status=True
                    except:
                        print("[MK2 Beyond Reach. Kindly RESET and start over the application]")


        for cnt in contours_red:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)            
                cv2.putText(img, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                cx,cy=self.calculate_cendroid(x,y,w,h)
                cv2.circle(img, (cx,cy), 1, (0,0,255), 2)
                if(cy>300 and cx>75 and cx <1151):
                    print("cx:",str(cx),"cy:",str(cy))                    
                    mPEngine=MotionPlanning()
                    try:
                        theta1,theta2=mPEngine.auto_motion_algorithm_dynamic_camera(cy)
                        print("Theta1",theta1,"Theta2",theta2)
                        GenericDriver().trigger_motion("Red",theta1,theta2,base_angle)
                        status=True
                    except:
                        print("[MK2 Beyond Reach. Kindly RESET and start over the application]")


        cv2.imwrite("Processed_Image/tracked_color_object.jpg",img)
        print("[MK2 ROBOT VISION DYNAMIC CAMERA WAITING ...]")
        return (status)

