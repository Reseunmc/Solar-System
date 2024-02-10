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
