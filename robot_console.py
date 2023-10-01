"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
from auto_engine import ColorEngine_Static_Camera,ColorEngine_Dynamic_Camera
from MotionDriver.generic_driver import GenericDriver
import os,sys

class RobotConsole:

    def __init__(self):
        sys.path.append(os.path.abspath(os.path.join('..', 'Calibration')))
        
        self.coverage_angle=[]
        self.driver=GenericDriver()
        for angle in range(0,180,10):
            self.coverage_angle.append(angle)

    def automation_static_camera(self):
        count=0
        while count <10:
            count +=1
            engine=ColorEngine_Static_Camera()
            engine.take_picture()
            engine.process_selected_image()
        print("automation stopped .....")

    def automation_dynamic_camera(self):        
        while True:           
            self.driver.scan(0)
            status=False
            for angle in self.coverage_angle:  
                if status==True:          
                    self.driver.scan(angle)
                    break
                self.driver.move_base(angle)           
                engine=ColorEngine_Dynamic_Camera()
                engine.take_picture()
                status=engine.process_selected_image(angle)
            print("automation stopped .....")        
            self.driver.reset()
            if angle==170:
                break

    def menu_display(self):
        
        while True:            
            os.system('clear')
            print("[**********MK2 ROBOTIC ARM MODEL CONSOLE**********]")
            print("MENU:")
            print("1. Start Search and Sort Automation")            
            print("2. Caliberate Dynamic Camera")
            print("3. Motion Tesing")            
            print("4. Reset Position")
            print("5. Exit")
            selection=int(input("Enter your selection ... :"))
            if selection==3:
                from Calibration import calibrator_motion
                calibrator_motion.MotionCalibration()           
            if selection==2:
                self.driver.scan(90)
                from Calibration import calibrator_vision_dynamic_camera
                from Calibration import reset
                calibrator_vision_dynamic_camera.VisionCalibrator()                  
                reset.ResetPositions()
            if selection==1:
                self.automation_dynamic_camera()
            if selection==4:
                from Calibration import reset
                reset.ResetPositions()
            if selection==5:
                print("[**********APPLICATION CLOSED**********]")
                exit()


if __name__=="__main__":
    console=RobotConsole()
    console.menu_display()
