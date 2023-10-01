"""
Author:Akhil Jacob
Robot:MK2
TechMaverik
"""
class MotionPlanning:

    def __init__(self):
        self.pan1_angle_list=[]
        self.pan2_angle_list=[]
        self.points_list=[]
        self.selected_point_list=[]

    def auto_motion_algorithm_all_points(self,required_pan1_angle):

        for pan_angle1 in range(89,131):
            self.pan1_angle_list.append(pan_angle1)
        for pan_angle2 in range(49,93):
            self.pan2_angle_list.append(pan_angle2)      
        for pan1_angle in self.pan1_angle_list:
            if pan1_angle==required_pan1_angle:
                hit_index=self.pan1_angle_list.index(required_pan1_angle)
        pan2_angle=self.pan2_angle_list[hit_index]        
        return pan2_angle

    def auto_motion_algorithm(self,y_axis):

        for pan_angle1 in range(89,131):
            self.pan1_angle_list.append(pan_angle1)
        for pan_angle2 in range(49,93):
            self.pan2_angle_list.append(pan_angle2)  
        for position in range(350,996):
            self.points_list.append(position)    
        for position in range(350,996,16):
            self.selected_point_list.append(position)  
        print(self.selected_point_list)
        total_count=len(self.selected_point_list)
        count=0
        pan1_angle=80
        pan_angle2=72
        while count < total_count-1:            
            limit1=self.selected_point_list[count]
            limit2=self.selected_point_list[count+1]
            # print(ypos,limit1,limit2)                
            if(limit1<y_axis<=limit2):
                print("HIT",limit2)
                hit_index=self.selected_point_list.index(limit2)
                pan1_angle=self.pan1_angle_list[hit_index]
                pan_angle2=self.pan2_angle_list[hit_index]
                
            count=count+1                
        return(pan1_angle,pan_angle2)   
    
    def auto_motion_algorithm_dynamic_camera(self,y_axis):

        for pan_angle1 in range(89,131): #len=42
            self.pan1_angle_list.append(pan_angle1)
        for pan_angle2 in range(49,93):
            self.pan2_angle_list.append(pan_angle2)  
        for position in range(0,1020): #len =1014
            self.points_list.append(position)    
        for position in range(0,1020,24):
            self.selected_point_list.append(position)  
        #print(self.selected_point_list)
        total_count=len(self.selected_point_list)
        count=0
        pan1_angle=80
        pan_angle2=72
        while count <= total_count-2:            
            limit1=self.selected_point_list[count]
            limit2=self.selected_point_list[count+1]
            # print(y_axis,limit1,limit2)                
            if(limit1<y_axis<=limit2):
                print("HIT",limit2)
                hit_index=self.selected_point_list.index(limit2)
                pan1_angle=self.pan1_angle_list[hit_index]
                pan_angle2=self.pan2_angle_list[hit_index]
                
            count=count+1                
        return(pan1_angle,pan_angle2)   


# engine=MotionPlanning()
# import time
# for i in range (6,1023):
#     result=engine.auto_motion_algorithm_dynamic_camera(i)
#     # time.sleep(0.5)
#     print(i,result)