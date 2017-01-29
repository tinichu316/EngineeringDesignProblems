#Forward kinematics
#calculate the x and y coordinates of a single jointed arm given theta1, theta2, L1, and L2

from math import cos, sin, pi

L1 = 2.5 #length in meters
theta1 = 1.2 #angle from horizontal in radians
L2 = 0.5
theta2 = 3 #angle from the line of action of the previous arm

L = [0,0] #L is a vector with 2 components, x and y coordinates

L[0] = L1*cos(theta1) + L2*cos(theta1 + theta2)
L[1] = L1*sin(theta1) + L2*sin(theta1 + theta2)

print("The x-coordinate of the endarm will be: %s m\nand the y-coordinate of the endarm will be: %s m " %(L[0], L[1]))


