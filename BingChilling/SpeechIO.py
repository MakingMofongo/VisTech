import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def stt(prompt):
    r = sr.Recognizer()

    with sr.Microphone() as source:
            print('adjusting for ambient noise')
            r.adjust_for_ambient_noise(source)

            print("Please say something...")
            tts(prompt)
            audio = r.listen(source)

            try:
                said=r.recognize_google(audio)
                print(f"You have said: {said}")
                # if r.recognize_google(audio) == "stop":
                #     quit()
            except Exception as e:
                print(f"STT Error: {str(e)}")
                return stt()
            
            return said
            
            

            

def tts(input_text):
    text = str(input_text)

    language = 'en'

    obj = gTTS(text=text, lang=language, slow=False)

    obj.save("BingChilling/welcome.mp3")

    playsound('BingChilling/welcome.mp3')