import cv2
from realsense_camera import *
from mask_rcnn import *

# Load Realsense camera and Mask R-CNN
rs = RealsenseCamera()
mrcnn = MaskRCNN()
while True:
    # Get frame in real time from Realsense camera
    ret, bgr_frame, depth_frame = rs.get_frame_stream()
    print(depth_frame)
    point_x, point_y = 250, 100
    distance_mm = depth_frame[point_x, point_y]

    cv2.circle(bgr_frame, (point_x, point_y), 8, (0,0,255), -1)

    cv2.imshow("brehu",bgr_frame)
    cv2.waitKey(1)


