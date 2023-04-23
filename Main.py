import time
import cv2
import numpy as np
import face_recognition
import os
import keyboard
import openpyxl
import sys
from ElevenLabs import eleven_labs
from FaceSave import Capture
import concurrent.futures

import torch
from bot_test_gpt import bot_initialize,description

import sys
sys.path.append(r'C:\Users\Abdul Rasheed\OneDrive\Documents\GitHub\VisTech_CFI\psmove\bindings\python')
# import psmoveapi
import easyocr



def import_yolo():
    sys.path.append(r'C:\Users\Abdul Rasheed\OneDrive\Desktop\MainN\Vistech_CFI\yolov7')
    from  yolov7 import hubconf
    return hubconf

def YOLO():
    # load yolo v5 model
    model = torch.hub.load("ultralytics/yolov5","yolov5s",pretrained = True)
    # load yolo v7 model:
    # hubconf = import_yolo()
    # model = hubconf.custom(path_or_model='yolov7.pt')
    
    # vid= cv2.VideoCapture(0)
    running = True
    global OBJECTS
    fps=30.0
    while running:
        start_time = time.time()
        # success,img = vid.read()
        img_gpt = img.copy()
        results = model(img_gpt)
        objects=""
        for i in results.pandas().xyxy[0]["name"].values[:]:
            objects+=" "+i
        results.render()
        # find and affix fps using time module

        cv2.putText(img_gpt, f'FPS: {fps}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("ObjectDetection",img_gpt)
        cv2.waitKey(1)
        done_time = time.time()
        fps = 1/(done_time-start_time)
        fps = int(fps)
        OBJECTS = objects
        # print(OBJECTS)
        
        # if(Move.key=='T'):


        # if(Move.key=='BOX'):
        if(exiting):
            running = False
            return 0
        
        
          
def OCR():
    # easy ocr image
    text1=easyocr.Reader(['en']).readtext(img)

    # take only the phrases from easy ocr output
    text1 = [i[1] for i in text1] # type: ignore
    # join the phrases
    text1 = ' '.join(text1)


    # print the text
    print(text1)

    # add text to original image
    cv2.putText(img, text1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    list = [text1, img]
    
    return list
        

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
            encodeList.append(encode
                              )

    if encodeList:

        return encodeList
    else:
        print('couldnt find a single face, exiting....')
        exit()

def encodeRepeater():
    print('encorepeater Started')
    global encodesCurFrame
    encodesCurFrame=0
    Processor = concurrent.futures.ProcessPoolExecutor()
    while not exiting:

        future1 = Processor.submit(liveEncodings,img,facesCurFrame)

        encodesCurFrame= future1.result()

def locationsRepeater():
    print('locorepeater Started')
    global facesCurFrame
    Processor = concurrent.futures.ProcessPoolExecutor()
    while True:
        if (exiting):
            break
        future1 = Processor.submit(liveLoco,img)
        facesCurFrame= future1.result()


def snap(cap,initial_index):
    index = initial_index
    global img
    fps=30
    while True:
        # Switch camera
        if keyboard.is_pressed('r'):
            print('switching camera')
            index = index + 1
            cap.release()
            # Test if camera with new index works
            try:
                cap = cv2.VideoCapture(index)
                success, img = cap.read()
                cv2.imshow("Raw Capture", img)
                cv2.waitKey(1)
            except:
                if index == initial_index+1: # First change didnt work, meaning no other camera found
                    print('Unable to switch camera, no other camera found')
                print('switching to default camera')
                cap = cv2.VideoCapture(initial_index)
                index = initial_index
            print('switched camera to index: ', index)
        

        start_time = time.time()
        # Move.update()
        if(exiting):
            cv2.destroyAllWindows()
            break
    
        success, img = cap.read()
        # show the frame
        # affix framerate to image
        raw_img = img.copy()
        cv2.putText(raw_img, f'FPS: {fps}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("Raw Capture", raw_img)
        done_time = time.time()
        fps = 1/(done_time-start_time)
        fps = int(fps)
        cv2.waitKey(1)

def liveEncodings(imgS,facesCurFrame):

    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame,model="large")
    # print('LiveEncoded!!!!!!!!!!!!!!!!!!!!!!!!!')
    result = encodesCurFrame
    return result

def liveLoco(imgS):
    # print('locoing')
    facesCurFrame= face_recognition.face_locations(imgS)
    return facesCurFrame

def main(cap,initial_index):
    Threader = concurrent.futures.ThreadPoolExecutor()
    future_snap=Threader.submit(snap,cap,initial_index)

    global names,cName
    names=[]
    cName = ''

    
    print('***FACE RECOGNITION***')
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
    path = './Faces'
    images = []
    classNames = [] #names of captured images without extension
    myList = os.listdir(path)



    print('Loading Images')
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
    print('Images Loaded')
    print('Encoding Images')
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    # class RedTrigger(psmoveapi.PSMoveAPI):
    #     def __init__(self):
    #         super().__init__()
    #         self.quit = False

    #     def on_connect(self, controller):
    #         controller.connection_time = time.time()
    #         print('Controller connected:', controller, controller.connection_time)

    #     def on_update(self, controller):
    #         # print('Update controller:', controller, int(time.time() - controller.connection_time))
    #         # print(controller.accelerometer, '->', controller.color, 'usb:', controller.usb, 'bt:', controller.bluetooth)
    #         up_pointing = min(1, max(0, 0.5 + 0.5 * controller.accelerometer.y))
    #         controller.color = psmoveapi.RGB(controller.trigger, up_pointing, 1.0 if controller.usb else 0.0)
    #         self.key='NONE'
    #         if controller.now_pressed(psmoveapi.Button.PS):
    #             self.quit = True
    #         if controller.now_pressed(psmoveapi.Button.SQUARE):
    #             print('SQUARE')
    #             self.key='SQUARE'
    #         if controller.now_pressed(psmoveapi.Button.TRIANGLE):
    #             print('TRIANGLE')
    #             self.key='TRIANGLE'
    #         if controller.now_pressed(psmoveapi.Button.CIRCLE):
    #             self.key='CIRCLE'
    #         if controller.now_pressed(psmoveapi.Button.CROSS):
    #             self.key='CROSS'
    #         if controller.now_pressed(psmoveapi.Button.T):
    #             self.key='T'
    #         if controller.now_pressed(psmoveapi.Button.MOVE):
    #             self.key='MOVE'  
    #         if controller.now_pressed(psmoveapi.Button.PS):
    #             self.key='PS'  

                      


    #         def on_disconnect(self, controller):
    #             print('Controller disconnected:', controller)

    # global Move
    # Move = RedTrigger()
    
    print('Waiting for first frame...')
    while True:
        try:
            img
            print('...Recieved first frame')
            future_loco=Threader.submit(locationsRepeater)
            future_desc=Threader.submit(YOLO)
        except:
            continue

        print('Waiting for facesCurFrame...')
        while True:
            try:
                facesCurFrame
                print('...Recieved facesCurFrame')
                future_enco=Threader.submit(encodeRepeater)
                break
            except:
                continue
        break


    print('loops started**')


    fps=30
    while True:
        try:
            encodesCurFrame
            while True:
                start_time = time.time()
                # FACE RECOGNITION
                try:
                    # if (Move.key=='MOVE'):
                    if(keyboard.is_pressed('space')):
                        if not name == '':
                            print(name)
                            ELTTS.speech(name)
                        else:
                            print('No face detected')
                            ELTTS.speech('No face detected')
                except:
                    print('No face detected')
                    ELTTS.speech('no face detected')

                # TEXT TTS
                if(keyboard.is_pressed('q')):
                    text = OCR()[0]
                    if text == '':
                        text = 'No text detected'
                    print(f"\n\n OCR TEXT: {text} \n\n")

                    ELTTS.speech(text)

                # OCR display text and image
                if(keyboard.is_pressed('t')):
                    print('Freezing OBJECTS')
                    objects = OBJECTS
                    if objects == '':
                        objects = 'No objects detected'
                    print (f"Current objects: {objects}")
                    print('Acquiring text...')
                    text = OCR()[0]
                    if text == '':
                        text = 'No text detected'

                    print(f"OCR TEXT: {text}")

                    print('face detected: ',name)

                    prompt = f'Text: {text}, Objects: {objects}, Faces detected: {name}'
                    print (f"prompt: {prompt}")
                    print('Describing image...')


                    Description = description(BOT, prompt)
                    print(f"\n \nDescription: {Description}\n \n")
                    print('Speaking...')
                    ELTTS.speech(Description[1])
                    print('Done Speaking')


                    # cv2.imshow('OCR',Ocr_img) 
                    # cv2.waitKey(0)
                    # cv2.destroyWindow('OCR')


                

                # if (Move.key=='PS'):
                if(keyboard.is_pressed('esc')):
                    print('Exiting')
                    global exiting
                    exiting = True
                    while True:
                        if (future_enco.done() and future_loco.done() and future_snap.done() and future_desc.done()):
                            print('Threads Stopped')
                            exit(1)
                            # bug with destroyAllWindows and release- not destorying windows and stuck
                            cap.release()
                            cv2.destroyAllWindows()
                            print('IO exiting')
                img_fd=img.copy()
                # name=''
                for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):

                    matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                    #print(faceDis)
                    matchIndex = np.argmin(faceDis)
                    if matches[matchIndex]:
                        name = classNames[matchIndex].upper()
                        y1,x2,y2,x1 = faceLoc
                        y1, x2, y2, x1 = y1,x2,y2,x1
                        cv2.rectangle(img_fd,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img_fd,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img_fd,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                # find and affix framerate of 'img_fd'
                fps=int(fps)
                cv2.putText(img_fd, f'FPS: {fps}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow('FaceDetection',img_fd)
                done_time = time.time()
                if(done_time-start_time!=0):
                    fps = 1/(done_time-start_time)
                cv2.waitKey(1)

        except SystemExit:
            exit(1)
        except:
            continue
        
if __name__ == '__main__':
    ELTTS = eleven_labs.ElevenLabsSpeech()
    ELTTS.setup()
    ELTTS.speech('Speech has been setup')
    global exiting
    exiting=False
    initial_index = 0
    print('Starting camera...')
    ELTTS.speech('Starting camera')
    while True:
        cap = cv2.VideoCapture(initial_index)
        print('Trying camera at index: ',initial_index)
        success, img = cap.read()
        if success:
            print('Camera started')
            ELTTS.speech('Camera started')
            break
        else:
            print('Camera not found at index: ',initial_index)
            initial_index += 1
    

    global OBJECTS
    global BOT
    BOT = bot_initialize()
    print('BOT INITIALIZED')
    ELTTS.speech('bot INITIALIZED')
    test_string = 'Text: Shop, Objects: car'
    print('Testing BOT with string: ',test_string)
    ELTTS.speech('Testing bot with string: '+test_string)
    response = description(BOT,test_string)
    print(f"Response: {response}")
    ELTTS.speech('Response: '+str(response[1]))
    main(cap,initial_index)
