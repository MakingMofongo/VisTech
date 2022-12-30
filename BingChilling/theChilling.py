import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time

from SpeechIO import stt,tts
from FaceSave import Capture

import threading
import queue

# import multiprocessing as mp
# from multiprocessing import Process



from PIL import ImageGrab

path = 'BingChilling/Faces/Captured'
images = []
classNames = [] #names of captured images without extension
myList = os.listdir(path)


def findEncodings(images):
    encodeList = []

    n=-1 #counter used to find name of image if needed
    for img in images:
        n+=1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            
        except IndexError:
            print(f"Couldnt detect {classNames[n]}'s face, Skipping...")
            continue
        if encode.any:
            print(f'encoding {myList[n]}')
            encodeList.append(encode)

    if encodeList:
        return encodeList
    else:
        print('couldnt find a single face, exiting....')
        exit()


def snap(cap):
    while True:
        print('finna snap')
        global img
        success, img = cap.read()
        global imgS
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

def liveEncodings():
    while True:

        global facesCurFrame
        facesCurFrame= face_recognition.face_locations(imgS)
        
        global encodesCurFrame
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    
def main():

    Capture()


    print(myList)
    n=-1
    for cl in myList:
        n+=1
        curImg = cv2.imread(f'{path}/{cl}')
        if curImg.all:
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
            print(classNames[n])
        else:
            print(f'Couldnt read {cl}') 
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    
    cap = cv2.VideoCapture(0)

    thread = threading.Thread(target=liveEncodings)
    thread2 = threading.Thread(target=snap,args=(cap,))
    thread2.start()
    time.sleep(1)
    thread.start()
    time.sleep(1)
    while True:



        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
        
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                #print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

        cv2.imshow('Webcam',img)
        cv2.waitKey(1)

if __name__=='__main__':
 main()
    
