import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshhold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Command:  {query}\n")

    except Exception:
        print("Sorry! say again please...")
        return "None"
    return (query)


if __name__ == "__main__":
    while True:

        query = Commands().lower()

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open pycharm' in query:
            pycharmPath = '"C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.3\\bin\\pycharm64.exe"'
            os.open(pycharmPath)

        elif 'bye' in query:
            speak('Thank you! have a good day')
            exit()

