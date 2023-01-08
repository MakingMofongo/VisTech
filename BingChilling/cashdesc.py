from SpeechIO import tts
import cv2
import torch
import numpy as np
from chatgpt_wrapper import ChatGPT
import keyboard

def main():

    bot = ChatGPT()
    model = torch.hub.load("BingChilling/yolov5","custom",path ='BingChilling/newbest.pt',source = "local")
    vid= cv2.VideoCapture(0)
    running = True
    while running:
        success,img = vid.read()
        results = model(img)
        stng = ""
        for i in results.pandas().xyxy[0]["name"].values[:]:
            stng+=" "+i
        results.render()
        cv2.imshow("something",img)
        k = cv2.waitKey(1)
        if(keyboard.is_pressed('c')):
            print("cash")

        if(keyboard.is_pressed('esc')):
            running = False
            return 0
main()
