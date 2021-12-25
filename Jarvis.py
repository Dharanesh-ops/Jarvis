import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 <= hour < 12:
        speak('Good Morning')

    elif hour > 12 <= hour < 17:
        speak('Good Afternoon')

    elif hour > 20 <= hour < 24:
        speak('Good Night')


speak('Iam Jarvis sir,Please tell me how may i help you')


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query[1] = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        print(e)
        print('Say that again please...')  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print('results')
            speak('results')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
        elif 'open time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')
