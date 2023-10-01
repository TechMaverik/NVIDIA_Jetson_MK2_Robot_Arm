"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
from MK2.MK2_Movement_Engine_UI import *

class ResetPositions():
    try:
        robot =RobotArmEngine("/dev/ttyUSB0")    
        robot.goto(90,80,72,90)
    except:
        print("Robot not connected")

    

   
