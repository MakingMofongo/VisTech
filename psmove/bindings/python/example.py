import os
import sys
import time

BASE = os.path.join(os.path.dirname(__file__), '..', '..')

if 'PSMOVEAPI_LIBRARY_PATH' not in os.environ:
    os.environ['PSMOVEAPI_LIBRARY_PATH'] = os.path.join(BASE, 'build')

sys.path.insert(0, os.path.join(BASE, 'bindings', 'python'))

import psmoveapi


class RedTrigger(psmoveapi.PSMoveAPI):
    global i
    i=0
    def __init__(self):
        super().__init__()
        self.quit = False
        self.key = False
        self.i=0
        

    def on_connect(self, controller):
        controller.connection_time = time.time()
        print('Controller connected:', controller, controller.connection_time)

    
    def on_update(self, controller):
        # print('Update controller:', controller, int(time.time() - controller.connection_time))
        print(controller.color)
        up_pointing = min(1, max(0, 0.5 + 0.5 * controller.accelerometer.y))

        controller.color = psmoveapi.RGB(controller.trigger, up_pointing, 1.0 if controller.usb else 0)
        
        if self.i>=1.0:
            self.i=0


        # self.i=self.i+0.0005
        # print(f"rumble={self.i+.25}")
        # controller.rumble = .250+self.i  #Values - 0.251 - 1.000
        # controller.rumble = .7

        def disp_battery():
            if controller.battery>10:
                print("Charging by USB")
            else:
                print(f"Battery: {controller.battery*10}%")
        
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



    def on_disconnect(self, controller):
        print('Controller disconnected:', controller)

i=0
api = RedTrigger()
while not api.quit:
    api.update()
    