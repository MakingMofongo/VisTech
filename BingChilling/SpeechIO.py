import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def stt():
    r = sr.Recognizer()

    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Please say something...")
            audio = r.listen(source)

            try:
                said=r.recognize_google(audio)
                print(f"You have said: {said}")
                # if r.recognize_google(audio) == "stop":
                #     quit()
            except Exception as e:
                print(f"Error: {str(e)}")
            
            return said
            
            

            

def tts(input_text):
    text = str(input_text)

    language = 'en'

    obj = gTTS(text=text, lang=language, slow=False)

    obj.save("BingChilling/welcome.mp3")

    playsound('welcome.mp3')