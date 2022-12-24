import speech_recognition as sr


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            r.adjust_for_ambient_noise(source)
            print("Please say something...")
            audio = r.listen(source)

            try:
                print(f"You have said: {r.recognize_google(audio)}")
                if r.recognize_google(audio) == "stop":
                    quit()
            except Exception as e:
                print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()