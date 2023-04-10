#from SpeechIO import tts
import torch
import numpy as np
from chatgpt_wrapper import ChatGPT
import cv2
from realsense_camera import *

#if ser.in_waiting:
#    packet = ser.readline()
#    print(packet.decode
# Load Realsense camera
rs = RealsenseCamera()
def main():

    model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained = True)
    #model = torch.hub.load("ultralytics/yolov5","custom",path ="./ringww.pt")
    # vid= cv2.VideoCapture(0)
    running = True
    x,y = 100,100
    while running:
	# Get frame in real time from Realsense camera
        ret, bgr_frame, depth_frame = rs.get_frame_stream()

        # Get object mask

        # Draw object mask
        # Show depth info of the objects
        resultss = model(bgr_frame)
        distance_mm = depth_frame[y,x]
        cv2.circle(bgr_frame,(x,y),8,(0,0,255),-1)

        detections = model(bgr_frame[..., ::-1])
        results = detections.pandas().xyxy[0].to_dict(orient="records")
        #resultss.render()
        for result in results:
            for i in resultss.pandas().xyxy[0]["name"].values[:]:
                con = result['confidence']
                cs = result['class']
                x1 = int(result['xmin'])
                y1 = int(result['ymin'])
                x2 = int(result['xmax'])
                y2 = int(result['ymax'])
                height,width,chn = bgr_frame.shape

                cv2.rectangle(bgr_frame,(x1,y1),(x2,y2),(255,0,0),2)
                # Do whatever you want
                cv2.circle(bgr_frame,(x1+100,y1+100),8,(0,0,255),-1)
                cv2.putText(bgr_frame,f"({x1},{x2}) | {distance_mm}mm" , (x1+100,y1+100),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
                print(x1,y1,distance_mm)
        cv2.imshow('somehting',bgr_frame)
        key = cv2.waitKey(1)
        if key == 27:
            running = False
            break
main()
rs.release()
cv2.destroyAllWindows()
