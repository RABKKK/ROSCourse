from robot_control_class import RobotControl
#Additional libraries that may be used (try not use so many libraries) only what is required to ensure the program has minimum requirements

def findmin_max(laser_full):
  ##
  #Code to calculate minimum and maximum values and return it
  ##

rc = RobotControl()

#Refere to Lab 2 task to understand how Methods are called. Alos check the class defined in robot_control_class.py file

#Minimum distance to avoid collision
cutoff_dist=0.5

#Step 1: Obtain laser scan data

#Step 2 Find maximum and minimum values by callinng the defined function

#Step 3:Print the values of Maximum and minimum values in the format Maximum is xxx and minimum is xxx

# Step 4: Write a loop to do steps 1 to 3 inside a loop. A move the robot in a straigth line using the suitable methods in the class RobotControl. Check and ensure that the value of minimum distance is less than that of cutoff cutoff_dist defined earlier.
 
# Step 5: Stop the robot using the suitable function in the class RobotControl.
