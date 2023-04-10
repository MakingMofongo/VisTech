
from SpeechIO import tts
import torch
import numpy as np
from chatgpt_wrapper import ChatGPT
import cv2
from realsense_camera import *
from mask_rcnn import *


# Load Realsense camera
rs = RealsenseCamera()
mrcnn = MaskRCNN()
def main():

    bot = ChatGPT()

    model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained = True)
    # vid= cv2.VideoCapture(0)
    running = True
    x,y =100,100
    while running:
	# Get frame in real time from Realsense camera
        ret, bgr_frame, depth_frame = rs.get_frame_stream()

	    # Get object mask
        boxes, classes, contours, centers = mrcnn.detect_objects_mask(bgr_frame)

	    # Draw object mask
        bgr_frame = mrcnn.draw_object_mask(bgr_frame)
	    # Show depth info of the objects
        mrcnn.draw_object_info(bgr_frame, depth_frame)
        distance_mm = depth_frame[x,y]
        cv2.circle(bgr_frame,(x,y),8,(0,0,255),-1)
        cv2.putText(bgr_frame,f"{distance_mm}mm",(x,y-10),0,1,(0,0,255),2)
        key = cv2.waitKey(1)
        if key == 27:
            break

rs.release()
cv2.destroyAllWindows()
