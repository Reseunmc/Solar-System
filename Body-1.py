__author__ = 'Re'
from cs1lib import *

class Body:
    #constructor,taking the planets mass, the x coordinate in meters, velocity in meters pixel radius of the body and
    #the color
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass=mass
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.pixel_radius=pixel_radius
        self.r=r
        self.g=g
        self.b=b

#update position takes the self,x and incriments it by the velocity value
    def update_position(self, timestep):
        self.x=self.x+self.vx*(timestep)
        self.y=self.y+self.vy*(timestep)

#the update velocity chances the velocity by incrementing it by the acceleration
    def update_velocity(self,ax,ay,timestep):
        self.vx=self.vx + ax*(timestep)
        self.vy=self.vy + ay*(timestep)

#draw function scales the inputted y and x values by pixels_per meter and updates
# the value by cy and cx before producing the circle image
    def draw(self,cx,cy,pixels_per_meter):
        draw_y=(self.y* pixels_per_meter)
        draw_x=(self.x* pixels_per_meter)
        draw_y=draw_y + cy
        draw_x=draw_x + cx
        enable_smoothing()
        disable_stroke()
        set_fill_color(self.r,self.g,self.b)
        draw_circle(draw_x,draw_y,self.pixel_radius)

#get methods to return the values
    def get_mass(self):
        return self.mass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
