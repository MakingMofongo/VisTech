from SpeechIO import tts
import cv2
import torch
import numpy as np
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()

model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained = True)
vid= cv2.VideoCapture(1)
running = True
while running:
    success,img = vid.read()
    results = model(img)
    stng = ""
    for i in results.pandas().xyxy[0]["name"].values[:]:
        stng+=" "+i
    results.render()
    cv2.imshow("something",img)
    k = cv2.waitKey(0)
    if(k==ord('s')):
        print("t")
        response = bot.ask(f"""
        {stng}
        frame a scene in a short sentence from the above information for a blind person 20 limit """)
        tts(response)  # prints the response from chatGPT
        running = False
    if(k==ord('q')):
        break
