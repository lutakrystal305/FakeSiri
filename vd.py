import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

kyoshiro = pyttsx3.init()
voice = kyoshiro.getProperty('voices')
kyoshiro.setProperty('voice', voice[1].id)

def speak(audio):
    print('Kyoshiro said: ' + audio)
    kyoshiro.say(audio)
    kyoshiro.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 10:
        speak('Good morning Boss')
    elif hour >= 10 and hour <13:
        speak('Good lunch Boss')
    elif hour >= 13 and hour < 18:
        speak('Good afternoon Boss')
    elif hour >= 18 and hour < 22:
        speak('Good evening Boss')
    else:
        speak('Good midnight Boss')
def solve():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_theshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Otama: " + query)
    except sr.UnknownValueError:
        print('Hi sir, Please repeat!')
        query = input('Your order is: ')
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = solve().lower()
        if "google" in query:
            speak("What do you search on google?")
            search=solve().lower()
            url = f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak("This is thing that you searched")
        elif "youtube" in query:
            speak("What do you search on youtube?")
            search=solve().lower()
            url = f'https://www.youtube.com/search?q={search}'
            wb.get().open(url)
            speak("This is thing that you searched")
        elif "facebook" in query:
            url = 'https://www.facebook.com/'
            wb.get().open(url)
            speak("Okay")
        elif "boss" in query:
            url = 'https://www.facebook.com/lutakrystal305/'
            wb.get().open(url)
            speak("Hi Boss")
        elif "time" in query or "what time is it" in query:
            time()
        elif "Photoshop" in query:
            dir = r"C:\Program Files\Adobe\Adobe Photoshop 2021\photoshop"
            os.startfile(dir)
        elif "quit" in query:
            speak("Kyoshiro is coming to Wano, bye Boss")
            quit()
