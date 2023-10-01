"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
from MK2.MK2_Movement_Engine_UI import *

class GenericDriver:
    
    def __init__(self):
        try:
            self.robot =RobotArmEngine("/dev/ttyUSB0")   
            self.base_error=25 
            self.pan1_error=-10
            print("[Connected to Jetson]")
        except:           
            print("[Couldn't Connect]")

    def trigger_motion(self,color,pan1,pan2,base):
        """trigger motion on the basis of color and sort"""        
        
        if (color=="Blue"):
            try:
                """GOTO Default Take Blue"""
                print("Operation Blue Executing")
                self.robot.goto(base+self.base_error,80,72,90)
                self.robot.goto(base+self.base_error,80,pan2,90)
                self.robot.goto(base+self.base_error,pan1+self.pan1_error,pan2,90)
                self.robot.goto(base+self.base_error,pan1+self.pan1_error,pan2,0)                
                self.robot.goto(base+self.base_error,80,72,0)
                self.robot.goto(180,80,72,0)
                self.robot.goto(180,80,72,90)
            except:
                print("Coudnt Send Data to Pyfirmata")

        if (color=="Green"):
            try:
                """GOTO Default Take Green"""
                print("Operation Blue Executing")
                self.robot.goto(base+self.base_error,80,72,90)
                self.robot.goto(base+self.base_error,80,pan2,90)
                self.robot.goto(base+self.base_error,pan1+self.pan1_error,pan2,90)
                self.robot.goto(base+self.base_error,pan1+self.pan1_error,pan2,0)                
                self.robot.goto(base+self.base_error,80,72,0)
                self.robot.goto(0,80,72,0)
                self.robot.goto(0,80,72,90)
            except:
                print("Coudnt Send Data to Pyfirmata")

        if (color=="Red"):
            try:
                """GOTO Default Take Red"""
                print("Operation Blue Executing")
                self.robot.goto(base+self.base_error,80,72,90)
                self.robot.goto(base+self.base_error,80,pan2,90)
                self.robot.goto(base+self.base_error,pan1+self.pan1_error,pan2,90)
                self.robot.goto(base+self.base_error,pan1+self.pan1_error,pan2,0)                
                self.robot.goto(base+self.base_error,80,72,0)
                self.robot.goto(120,80,72,0)
                self.robot.goto(120,80,72,90)
            except:
                print("Coudnt Send Data to Pyfirmata")

    def scan(self,Theta):        
        """scan position""" 
        self.robot.goto(Theta,80,140,90)        

    def move_base(self,Theta):
        """ move base of the robotic arm"""           
        self.robot.single_base_movement(Theta)        

    def reset(self):     
        """ reset to home position"""   
        self.robot.goto(90,80,72,90)
         
