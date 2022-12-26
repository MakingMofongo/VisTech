import cv2
from time import sleep
# from SpeechIO import stt,tts

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret, frame = cap.read() # return a single frame in variable `frame`

cv2.imshow('face',frame) #display the captured image

cv2.waitKey(1000)
print("BRUH MOMENTOS UNOS")
# print('Who:')
# tts('Who is it?')
# name = stt()
# print(f'name is {name}')

cv2.imwrite('BingChilling/Faces/Captured/tester.png',frame)
cv2.destroyAllWindows()
cap.release()
