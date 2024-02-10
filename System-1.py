__author__ = 'Re'
from cs1lib import*
from Body import Body
from math import *

class System:
#system constructor comprised of an empty list of bodies
    def __init__(self, body_list):
        self.body_list=body_list

#draw function loops through the list and applies the body draw function on each element.
    def draw(self, cx, cy, pixels_per_meter):
        for i in range (0,len(self.body_list)):
            self.body_list[i].draw(cx,cy,(pixels_per_meter))

#update function to update both the accelerations in each component and velocities for each
#list element
    def update(self,timestep):
        for n in range (0,len(self.body_list)):
            (ax,ay)= self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax,ay,timestep)
            self.body_list[n].update_position(timestep)
#computes the acceleration for each item in the list based on the other items
    def compute_acceleration(self,n):
        ax=0.0
        ay=0.0
        for i in range (0,len(self.body_list)):

#checks if the body in question has the same index as the current iteration index and returns False
#if true, will continue. Allows the loop to ignore the body in question when adding acceleration
            if n!=i:
#G= gravitational constant
                G=6.67384e-11

#r=distance between the body in question and the body iteration in the loop
                r=sqrt((self.body_list[n].get_x() - self.body_list[i].get_x())**2 + (self.body_list[n].get_y() - self.body_list[i].get_y())**2 )

#a=acceleration based on G, mass, and r
                a=(G*(self.body_list[i].get_mass()))/(r**2)

#dx,dy= distance in the x direction and distance in the y between the body in question and
# the iteration body
                dx=(self.body_list[i].get_x())-(self.body_list[n].get_x())
                dy=(self.body_list[i].get_y())-(self.body_list[n].get_y())

#ax,ay= the accelerations in the x and y directions as based on a,dx, and r
                ax+=(a*dx/r)
                ay+=(a*dy/r)

#returns a tuple (dual value of ax and ay
        return(ax,ay)

