import cv2
from time import sleep
from SpeechIO import stt,tts

def Capture():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`

    while(True):
        cv2.imshow('img1',frame) #display the captured image

        sleep(.3)
        print('Who:')
        tts('Who is it?')
        name = stt()
        print(f'name is {name}')

        cv2.imwrite(f'Faces/Captured/{name}.png',frame)
        cv2.destroyAllWindows()
        break

    cap.release()