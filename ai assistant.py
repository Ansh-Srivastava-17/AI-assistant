import pyttsx3                              #pip install pyttsx3
import speech_recognition as sr             # pip install speechRecognition
import datetime
import wikipedia                            #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
#for female [1] and for male [0]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Gooood Morning!")

    elif hour>=12 and hour<18:
        speak("Gooood Afternoon!")

    else:
        speak("Gooood Evening!")

    speak("hello sir i am your friend mranal . Please tell me how may I help you")
#
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("can u repeat please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anjusri01@gmail.com', 'ansi@1705')
    server.sendmail('anjusri01@@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
     # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ' youtube' in query:
            webbrowser.open("youtube.com")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif ' google' in query:
            webbrowser.open("google.com")

        elif ' stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open vs code' in query:
            codePath2 = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath2)

        elif 'email to papa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "avisri01@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend  I am not able to send this email")





























































