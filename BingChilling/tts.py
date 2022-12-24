from gtts import gTTS
import os


def TTS(input_text):
    text = str(input_text)

    language = 'en'

    obj = gTTS(text=text, lang=language, slow=False)

    obj.save("welcome.mp3")

    os.system("afplay welcome.mp3")