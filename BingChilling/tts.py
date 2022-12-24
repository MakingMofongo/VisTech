from gtts import gTTS
import os
from playsound import playsound


def TTS(input_text):
    text = str(input_text)

    language = 'en'

    obj = gTTS(text=text, lang=language, slow=False)

    obj.save("welcome.mp3")

    playsound('welcome.mp3')

TTS('hiiiii')