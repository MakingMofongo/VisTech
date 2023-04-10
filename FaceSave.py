import cv2
from time import sleep
from SpeechIO import stt,tts

def Capture():
    cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`

    while(True):
        cv2.imshow('img1',frame) #display the captured image

        cv2.waitKey(1000)
        name = stt('who dat')
        print(f'name is {name}')

        cv2.imwrite(f'./Faces/{name}.jpeg',frame)
        cv2.destroyAllWindows()
        break

    cap.release()

if __name__ == '__main__':
    Capture()