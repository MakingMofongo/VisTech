import os
import sys
import time

BASE = os.path.join(os.path.dirname(__file__), '..', '..')

if 'PSMOVEAPI_LIBRARY_PATH' not in os.environ:
    os.environ['PSMOVEAPI_LIBRARY_PATH'] = os.path.join(BASE, 'build')

sys.path.insert(0, os.path.join(BASE, 'bindings', 'python'))

import psmoveapi
import pygame
import OpenGL.GL as gl
import math

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.OPENGL|pygame.DOUBLEBUF)



class RedTrigger(psmoveapi.PSMoveAPI):
    global i
    i=0
    def __init__(self):
        super().__init__()
        self.quit = False
        self.key = False
        self.i=0
        self.a,self.b,self.c=0.1,0.1,0.1
        self.amax,self.bmax,self.cmax=0,0,0
        self.xmax,self.ymax,self.zmax=0,0,0

    def on_connect(self, controller):
        controller.connection_time = time.time()
        print('Controller connected:', controller, controller.connection_time)

    
    def on_update(self, controller):
        # print('Update controller:', controller, int(time.time() - controller.connection_time))
        
        
        def buttons():        
            if controller.now_pressed(psmoveapi.Button.CIRCLE):
                disp_battery()
                
            if controller.still_pressed(psmoveapi.Button.T):
                # print('pressed')
                self.key=('True')
                # print(controller.trigger)
                
                controller.rumble = controller.trigger
            if controller.now_released(psmoveapi.Button.T):
                controller.rumble = 0.0
                
            if controller.now_pressed(psmoveapi.Button.PS):
                controller.rumble=0
                controller.color=psmoveapi.RGB(0,0,0)
                self.quit = True
        
        def render(self):
            # Clear the screen and set the background color
            gl.glClearColor(0, 0, 0, 1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

            # Get the controller's position and orientation
            av3 = controller.accelerometer # acceleration vector
            gv3 = controller.gyroscope # gyroscope vector
            pos = (av3.x,av3.y,av3.z) 
            ori = (gv3.x,gv3.y,gv3.z)
            # take only 2 decimnals from pos
            # pos = [round(num, 2) for num in pos]
            # ori = [round(num, 2) for num in ori]
            # print(pos)
            # print(ori)
            x_pointing = min(1, max(0, 0.5 + 0.5 * controller.gyroscope.x))
            y_pointing = min(1, max(0, 0.5 + 0.5 * controller.gyroscope.y))
            z_pointing = min(1, max(0, 0.5 + 0.5 * controller.gyroscope.z))
            # print(x_pointing,y_pointing,z_pointing)
            a,b,c = x_pointing,y_pointing,z_pointing

            # pos = pos[0]+8,pos[1]+4,pos[2]+7
            # ori = ori[0]+36,ori[1]+43,ori[2]+45
            # # divide ori by 10
            # ori = [round(num/10, 2) for num in ori]






            # print(pos)
            # print(ori)
            
            def max_values(self):
                # find max values of pos and ori
                if (pos[0]>self.xmax):
                    self.xmax = pos[0]
                if (pos[1]>self.ymax):
                    self.ymax = pos[1]
                if (pos[2]>self.zmax):
                    self.zmax = pos[2]
                



                if (ori[0]>self.amax):
                    self.amax = ori[0]
                if (ori[1]>self.bmax):
                    self.bmax = ori[1]
                if (ori[2]>self.cmax):
                    self.cmax = ori[2]
                
                # print and erase from terminal current amax,bmax,cmax, xmax,ymax,zmax in 2 lines
                print(f"amax={self.amax} bmax={self.bmax} cmax={self.cmax} xmax={self.xmax} ymax={self.ymax} zmax={self.zmax}", end="\r")
            # max_values(self)
            

            x,y,z = 0,0,0
            # print(f"x={x} y={y} z={z}", end="\r")
            # a,b,c = ori[0],ori[1],ori[2]
            print(f"a={a} b={b} c={c}", end="\r")
            # a,b,c = 0,0,0

            # testing values
            # a,b,c = 0.5,0.5,0.5
            # self.a,self.b,self.c=self.a*-1,self.b,self.c
            # a,b,c = self.a,self.b,self.c
            # print (a,b,c)


            # angle = math.atan2(ori[1], ori[0])
            angle = 90
            angle = math.degrees(angle)
            # only 2 decimals
            angle = round(angle, 2)
            # print(angle)


            # Draw the controller using the position and orientation data
            gl.glPushMatrix()
            gl.glTranslatef(x,y,z)
            gl.glRotatef(angle,a,b,c)

            gl.glBegin(gl.GL_LINES)
            gl.glColor3f(1, 0, 0)
            gl.glVertex3f(0, 0, 0)
            gl.glVertex3f(1, 0, 0)
            gl.glColor3f(0, 1, 0)
            gl.glVertex3f(0, 0, 0)
            gl.glVertex3f(0, 1, 0)
            gl.glColor3f(0, 0, 1)
            gl.glVertex3f(0, 0, 0)
            gl.glVertex3f(0, 0, 1)
            gl.glEnd()
            gl.glPopMatrix()

            # Update the screen
            pygame.display.flip()

        def color():
            # print(controller.color)
            up_pointing = min(1, max(0, 0.5 + 0.5 * controller.accelerometer.y))

            controller.color = psmoveapi.RGB(controller.trigger, up_pointing, 1.0 if controller.usb else 0)
            
            if self.i>=1.0:
                self.i=0

            # self.i=self.i+0.0005
            # print(f"rumble={self.i+.25}")
            # controller.rumble = .250+self.i  #Values - 0.251 - 1.000
            # controller.rumble = .7
            pass

        def disp_battery():
            if controller.battery>10:
                print("Charging by USB")
            else:
                print(f"Battery: {controller.battery*10}%")

        buttons()
        color()
        render(self)

    def on_disconnect(self, controller):
        print('Controller disconnected:', controller)

i=0
api = RedTrigger()
while not api.quit:
    api.update()
    