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
            
            

            

def tts(input_text):
    text = input_text
    # path = 'Sounds'
    # myList = os.listdir(path)
    # soundNames=[]
    # print(myList)
    # for cur_sound in myList:
    #     soundNames.append(os.path.splitext(cur_sound)[0])
    # print(soundNames)
    # mp3_name=text+".mp3"

    # address=path+mp3_name
    # if input_text in soundNames:
    #     playsound(address)
    # else:
    language = 'en'
    os.remove('sound.mp3')
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save('sound.mp3')
    playsound('sound.mp3')
        # try:
        #     obj = gTTS(text=text, lang=language, slow=False)
        #     try:
        #         obj.save(address)
        #         playsound(address)
        #     except:
        #         os.remove(address)
        #         raise Exception("No internet")
                
        # except:
        #     print("No internet")
        #     tts("No internet")


if __name__ == '__main__':
    # stt('bruh')
    tts('bruh momentos unos')
