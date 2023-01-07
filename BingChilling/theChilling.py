import time
import cv2
import numpy as np
import face_recognition
import os
import keyboard
import openpyxl
from SpeechIO import tts
from FaceSave import Capture
import concurrent.futures
import description

import torch
from chatgpt_wrapper import ChatGPT

def description():    
    bot = ChatGPT()

    model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained = True)
    # vid= cv2.VideoCapture(0)
    running = True
    while running:

        # success,img = vid.read()
        img_gpt = img
        results = model(img_gpt)
        stng = ""
        for i in results.pandas().xyxy[0]["name"].values[:]:
            stng+=" "+i
        results.render()
        cv2.imshow("ObjectDetection",img_gpt)
        k = cv2.waitKey(1)
        if(k==ord('s')):
            print("t")
            response = bot.ask(f"""
            {stng}
            frame a scene in a short sentence from the above information for a blind person 20 limit """)
            tts(response)  # prints the response from chatGPT
            running = False
        if(k==ord('q')):
            break
def findEncodings(images):
    encodeList = []

    n=-1 #counter used to find name of image if needed
    for img in images:
        n+=1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img,num_jitters=5,model="large")[0]
            
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

def encodeRepeater():
    print('encorepeater Started')
    global encodesCurFrame
    Processor = concurrent.futures.ProcessPoolExecutor()
    while not exiting:
        
        future1 = Processor.submit(liveEncodings,imgS,facesCurFrame)

        encodesCurFrame= future1.result()

def locationsRepeater():
    print('locorepeater Started')
    global facesCurFrame
    Processor = concurrent.futures.ProcessPoolExecutor()
    while True:
        if (exiting):
            break
        future1 = Processor.submit(liveLoco,imgS)
        facesCurFrame= future1.result()

def snap(cap):
    while True:
        if(exiting):
            break
        global img
        # print('globalled img')
        success, img = cap.read()
        # print('read image............')
        global imgS
        imgS = cv2.resize(img,(0,0),None,.5,.5)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

def liveEncodings(imgS,facesCurFrame):
    
    global encodesCurFrame
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame,model="large")
    print('LiveEncoded!!!!!!!!!!!!!!!!!!!!!!!!!')
    result = encodesCurFrame
    return result

def liveLoco(imgS):
    print('locoing')
    facesCurFrame= face_recognition.face_locations(imgS)
    return facesCurFrame
    
def main():

    global names,cName
    names=[]
    cName = ''
    global exiting
    exiting =False

    print('Press space to capture')
    timeout=5000
    t=0
    while t<timeout: 
        t1=time.time()
        try:
           if keyboard.is_pressed(' '):
                print('Snapping...')
                Capture()
                break
           elif keyboard.is_pressed('enter'):
                break 
        except:
            break
        finally:
            t2=time.time()
            t+=(t2-t1)* 10**3
            if not t<timeout:
                print('Timeout, continuing...')
                break

    global path,images,classNames,myList
    path = 'BingChilling/Faces/Captured'
    images = []
    classNames = [] #names of captured images without extension
    myList = os.listdir(path)

 


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
    Threader = concurrent.futures.ThreadPoolExecutor()
    future_snap=Threader.submit(snap,cap)
    
    while True:

        try:
            imgS
            future_loco=Threader.submit(locationsRepeater)
            future_desc=Threader.submit(description)
        except:
            continue

        while True:
            try:
                facesCurFrame
                future_enco=Threader.submit(encodeRepeater)
                break
            except:
                continue
        break
    

    print('loops started**')
    

    # with concurrent.futures.ProcessPoolExecutor() as executor:

    while True:
        try:
            encodesCurFrame
            while True:
                try:
                    if (keyboard.is_pressed('alt')):
                        print(name)
                        tts(name)
                except:
                    print('No face detected')
                    tts('no face detected')
                
                if (keyboard.is_pressed('escape')):
                    print('Exiting')
                    exiting = True
                    while True:
                        if (future_enco.done() and future_loco.done() and future_snap.done() ):
                            print('Threads Stopped')
                            cap.release()
                            cv2.destroyAllWindows()
                            print('IO exiting')
                            exit(1)
                for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                    
                    matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                    #print(faceDis)
                    matchIndex = np.argmin(faceDis)
                    img_fd=img
                    if matches[matchIndex]:
                        name = classNames[matchIndex].upper()
                        y1,x2,y2,x1 = faceLoc
                        y1, x2, y2, x1 = y1*2,x2*2,y2*2,x1*2
                        cv2.rectangle(img_fd,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img_fd,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img_fd,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                cv2.imshow('FaceDetection',img_fd)
                cv2.waitKey(1)
        
        except SystemExit:
            exit(1)
        except:
            continue

# if __name__ =='__main__':
#     main()
if __name__ == '__main__':
    main()