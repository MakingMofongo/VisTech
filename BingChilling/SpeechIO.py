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
    text = str(input_text)

    language = 'en'

    obj = gTTS(text=text, lang=language, slow=False)
    os.remove("welcome.mp3")
    obj.save("welcome.mp3")

    playsound('welcome.mp3')


if __name__ == '__main__':
    stt('bruh')