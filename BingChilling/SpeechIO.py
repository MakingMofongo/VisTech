import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def stt(prompt):
    r = sr.Recognizer()

    with sr.Microphone() as source:

            while True:
                print('adjusting for ambient noise')
                r.adjust_for_ambient_noise(source)
                try:
                    print("Please say something...")
                    tts(prompt)
                    audio = r.listen(source,timeout=3,phrase_time_limit=3)
                    break
                except sr.WaitTimeoutError:
                    print('timeout error, say it again')
                    continue



            try:
                said=r.recognize_google(audio)
                print(f"You have said: {said}")
                # if r.recognize_google(audio) == "stop":
                #     quit()
            except Exception as e:
                print(f"STT Error: {str(e)}")
                return stt(prompt)
            except :
                return stt(prompt)
            finally:
                del r
                del source
            
            return said
    
def snap(cap):
    while True:
        Move.update()
        if(exiting):
            break
        global img
        # print('globalled img')
        success, img = cap.read()
        # print('read image............')
        global imgS
        imgS = cv2.resize(img,(0,0),None,.5,.5)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            
            

            

def tts(input_text):
    text = input_text
    language = 'en'
    try:
        os.remove('sound.mp3')
    except:
        pass
    
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save('sound.mp3')
    playsound('sound.mp3')

if __name__ == '__main__':
    # stt('bruh')
    tts('bruh momentos unos')
