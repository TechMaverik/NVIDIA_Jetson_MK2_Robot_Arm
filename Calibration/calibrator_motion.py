"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
from Mathematical_Models.motion_planning import MotionPlanning
from MK2.MK2_Movement_Engine_UI import *
vMotionPlanning=MotionPlanning()

class MotionCalibration():

    try:
        robot =RobotArmEngine("/dev/ttyUSB0")    
    except:
        print("Cant Connect")
    for pan1 in range(89,130):
        pan2=vMotionPlanning.auto_motion_algorithm_all_points(pan1)
        print("0",pan1,pan2,"90")
        try:
            robot.goto(0,pan1,pan2,90)
        except:
            print("Failed")
    pan1=130
    while pan1 >=90:
        pan1=pan1-1
        pan2=vMotionPlanning.auto_motion_algorithm_all_points(pan1)
        print("0",pan1,pan2,"90")
        try:
            robot.goto(0,pan1,pan2,90)
        except:
            print("Failed")

    for pan1 in range(89,130):
        pan2=vMotionPlanning.auto_motion_algorithm_all_points(pan1)
        print("180",pan1,pan2,"90")
        try:
            robot.goto(180,pan1,pan2,90)
        except:
            print("Failed")
    pan1=130
    while pan1 >=90:
        pan1=pan1-1
        pan2=vMotionPlanning.auto_motion_algorithm_all_points(pan1)
        print("180",pan1,pan2,"90")
        try:
            robot.goto(180,pan1,pan2,90)
        except:
            print("Failed")

    for pan1 in range(89,130):
        pan2=vMotionPlanning.auto_motion_algorithm_all_points(pan1)
        print("90",pan1,pan2,"90")
        try:
            robot.goto(90,pan1,pan2,90)
        except:
            print("Failed")
    pan1=130
    while pan1 >=90:
        pan1=pan1-1
        pan2=vMotionPlanning.auto_motion_algorithm_all_points(pan1)
        print("90",pan1,pan2,"90")
        try:
            robot.goto(90,pan1,pan2,90)
        except:
            print("Failed")

    robot.goto(90,80,72,90)