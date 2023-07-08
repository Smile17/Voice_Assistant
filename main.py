import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import os.path  # required to fetch the contents from the specified folder/directory
import smtplib  # required to work with queries regarding e-mail

import browser_assistant as ba
import explorer_assistant as ea

engine = pyttsx3.init('sapi5')  # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')  # gets you the details of the current voices
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice


def speak(audio):  # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()  # without this command, the assistant won't be audible to us


def wishme():  # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour > 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Friday')


def takecommand():  # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:  # error handling
        print('Recognizing...')
        query = r.recognize_google(audio)  # using google for voice recognition
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')  # 'say that again' will be printed in case of improper voice
        return 'None'
    return query


def sendemail(to, content):  # function to send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senders_eamil@gmail.com', 'senders_password')
    server.sendmail('senders_email@gmail.com', to, content)
    server.close()


if __name__ == '__main__':  # execution control
    wishme()
    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        # The whole logic for execution of tasks based on user asked query

        browser = 'chrome'
        if 'firefox' in query:
            browser = 'firefox'

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif 'open' in query:
            for key in ba.urls:
                if key in query:
                    bas = ba.BrowserAssistant(ba.urls[key], browser)
                    bas.open_page()

            for key in ea.program_pathes:
                if key in query:
                    eas = ea.ExplorerAssistant()
                    eas.open_program(key)

        elif 'search' in query:
            data = query.split(" ")
            ba.GoogleAssistant(browser).search_google(data[1:])
        elif 'where is' in query:
            data = query.split(" ")
            ba.GoogleAssistant(browser).find_location(data[2:])
        elif 'translate' in query:
            data = query.split(" ")
            ba.GoogleAssistant(browser).translate(data[1:])

        elif 'play music' in query:
            speak('okay boss')
            music_dir = r'C:\Users\kam\Documents\Baby\My_Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')

        elif 'email' in query:
            try:
                speak('what should i write in the email?')
                content = takecommand()
                to = 'reciever_email@gmail.com'
                sendemail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry, I am not able to send this email')

        elif 'exit' in query:
            speak('okay boss, please call me when you need me')
            quit()

