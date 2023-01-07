import cv2
import torch
import numpy as np
import random
from theChilling import main

model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained = True)

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
        # self.video = cv2.resize(self.video,(840,640))
        # self.video = cv2.VideoCapture('carsnambu.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):

        success, image = self.video.read()
        results = model(image)
        car_counter, ambu_counter = 0,0
        for i in results.pandas().xyxy[0]["name"].values[:]:
            if "car" in results.pandas().xyxy[0]["name"].values[:]:
                car_counter+=1
            if "ambulance" in results.pandas().xyxy[0]["name"].values[:]:
                ambu_counter+=1


        a = np.squeeze(results.render())

        txt = cv2.putText(image,"Cars count: "+str(car_counter),(10,25),cv2.FONT_HERSHEY_PLAIN,2,(0,250,255),3)
        txt = cv2.putText(image,"Ambulance Count: "+str(ambu_counter),(10,55),cv2.FONT_HERSHEY_PLAIN,2,(0,250,255),3)
        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()
#particle -  loc,vel

#move from one location to other
#check collisions with road
#handle collisions

class Bing(object):
    def __init__(self):
        self.img = main()
    def draw(self):
        return self.img.tobytes()





