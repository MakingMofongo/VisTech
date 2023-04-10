#wrtie the template for midas depth estimation

import numpy as np
import cv2
import torch

import matplotlib.pyplot as plt


# Download the MiDaS
midas = torch.hub.load('intel-isl/midas','MiDaS_small') 
midas.to('cuda')
midas.eval()
# Input transformation pipeline
transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')
transform = transforms.small_transform

running = True

cap = cv2.VideoCapture(0)
``
cv2.namedWindow('result')

cv2.createTrackbar('lR', 'result', 0, 255, lambda x: None)
cv2.createTrackbar('lG', 'result', 0, 255, lambda x: None)


cv2.createTrackbar('lB', 'result', 0, 255, lambda x: None)

cv2.createTrackbar('uR', 'result', 0, 255, lambda x: None)
cv2.createTrackbar('uG', 'result', 0, 255, lambda x: None)
cv2.createTrackbar('uB', 'result', 0, 255, lambda x: None)

while running:
    ret, frame = cap.read()
    b,g,r =cv2.split(frame)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Input image
    input_batch = transform(frame).to('cuda')


    # Inference
    with torch.no_grad():
        prediction = midas(input_batch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=frame.shape[:2],
            mode='bicubic',
            align_corners=False,
        ).squeeze()

    # Save results
    output = prediction.cpu().numpy()
    plt.imsave('result.png',output)
    #read result.png
    result = cv2.imread('result.png')
    #change color to rgb from bgr
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    #add individual sliders to change red, green, blue values of result
    # create tracker
    #get the values of the sliders
    lr = cv2.getTrackbarPos('lR', 'result')
    lg = cv2.getTrackbarPos('lG', 'result')
    lb = cv2.getTrackbarPos('lB', 'result')

    ur = cv2.getTrackbarPos('uR', 'result')
    ug = cv2.getTrackbarPos('uG', 'result')
    ub = cv2.getTrackbarPos('uB', 'result')

    print(lr,ur,lg,ug,lb,ub)

    #create masks for each rgh value and mask it from the result
    lower_red = np.array([lb,lg,lr])
    upper_red = np.array([ub,ug,ur])

    mask = cv2.inRange(result, lower_red, upper_red)
    masked_img = cv2.bitwise_and(result, result, mask=mask)

   # Threshold the image using the lower and upper RGB values

    #show result
    cv2.imshow('result', masked_img)
    cv2.imshow('result2', result)

    #read pixel value of center of result

    plt.pause(0.00001)

    if cv2.waitKey(1) == ord('q'):
        running =False
        break

