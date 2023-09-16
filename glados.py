from datetime import datetime
from time import time
from tokenize import Special
import subprocess
import webbrowser
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import pywhatkit
import os
from playsound import playsound
import wikipedia
import pyautogui
import requests
import keyboard
import pyjokes
from googletrans import Translator
from pytube import YouTube
# from pyDictionary import pyDictionary

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[1].id)
Assistant.setProperty('rate', 200)


def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f":{audio}")
    print("  ")
    Assistant.runAndWait()


def takecommand():
    Command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        Command.pause_threshold = 1
        audio = Command.listen(source)

        try:
            print("Recognizing.......")
            query = Command.recognize_google(audio, language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()

def TaskExe():

    Speak("Hello , I  am glados")
    Speak("How can I help You?")

    def OpenApps():
        Speak("Ok Sir , Wait s second!")

        if 'code' in query:
            os.startfile(
                "C:\\Users\\asus\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'chrome' in query:
            os.startfile(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'calculatoer' in query:
            os.startfile(
                "search-ms:displayname=Search%20Results%20in%20Program%20Files%20(x86)&crumb=location:C%3A%5CProgram%20Files%20(x86)\\Calculatorz")
        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        Speak("Your command has been completed sir!")

    def Music():
        Speak("Tell me the name of the song!")
        musicName = takecommand()

        if 'kesariya' in musicName:
            os.startfile('D:\\WEB\\project\\spotify\\songs\\kesariya.mp3')
        elif 'dil galti kar baitha hai' in musicName:
            os.startfile(
                'D:\\WEB\\project\\spotify\\songs\\dil galti kar baitha hai.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy")

    def screenshot():
        Speak("Ok sir , What should I name that file?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "D:\\Project\\Jarvis\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\Project\\Jarvis")
        Speak("Here is your Screenshot")

    def greeting():
        hour = datetime.datetime.now().hour
        if hour >= 6 and hour < 12:
            Speak("good morning sir!")
        elif hour >= 12 and hour < 18:
            Speak("good afternoon sir!")
        elif hour >= 18 and hour < 24:
            Speak("good evening sir!")
        else:
            Speak("good night sir!")

    def time():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        Speak(Time)

    def Temp():
        search = "temperature in agra"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        Speak(f"The Temperature Outside is {temperature} ")

    def SpeedTest():
        import speedtest
        Speak("checking speed.........")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The Uploading Speed is {correctUpload} mbp s")
        elif 'downloading' in query:
            Speak(f"The downloading Speed is {correctDown} mbp s")
        else:
            Speak(
                f"The Downloading is {correctDown} and the Uploading speed is {correctUpload} mbp s")

    def CloseApps():
        Speak("OK Sir , Wait a second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")
        elif 'resso' in query:
            os.system("TASKKILL /F /im resso.exe")

        Speak("Your command has been succesfully completed!")

    def YoutubeAuto():
        Speak("Whats Your Command?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')

        Speak("Done  Sir !")

    def ChromeAuto():
        Speak("Chrome Automation started! ")
        Command = takecommand()

        if 'close this tab' in Command:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in Command:
            keyboard.press_and_release('ctrl +t')
        elif 'open new window' in Command:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in Command:
            keyboard.press_and_release('ctrl + h')

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir , I am Glados.")
            Speak("Your personal AI Assistant!")
            Speak("How May I help You?")

        elif 'how are you' in query:
            Speak("I am Fine sir  !")
            Speak("What's about You?")
        elif 'kaisa ho' in query:
            Speak("badhiya sir ap batyu")

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            break

        elif 'tell me my friends name' in query:
            Speak("Your friends name is urvashi , Kunal , nausheen ")

        elif 'youtube search' in query:
            Speak("Ok , sir  This is what I found for your search !")
            query = query.replace("imo", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            Speak("Done sir")

        elif 'google search' in query:
            Speak("ok , sir this is what I found for your search !")
            query = query.replace("imo", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak("done sir")
        elif 'website' in query:
            Speak("ok , sir , launching.......")
            query = query.replace("imo", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Lauched!")
        elif 'launch' in query:
            Speak("Tell me The name of the website !")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("done sir")
        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia......")
            query = query.replace("imo", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"According To wikipedia : {wiki}")
        elif 'open facebook' in query:
            OpenApps()
        elif 'open instagram' in query:
            OpenApps()
        elif 'open code' in query:
            OpenApps()
        elif 'open chrome' in query:
            OpenApps()
        elif 'open youtube' in query:
            OpenApps()
        elif 'open calcultor' in query:
            OpenApps()

        elif 'close facebook' in query:
            CloseApps()
        elif 'close instagram ' in query:
            CloseApps()
        elif 'close code' in query:
            CloseApps()
        elif 'close resso' in query:
            CloseApps()
        elif 'close youtube' in query:
            CloseApps()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'youtube tool' in query:
            YoutubeAuto()
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl +t')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'screenshot' in query:
            screenshot()
        elif 'time' in query:
            time()
        elif 'greet' in query:
            greeting()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
        elif 'repeat my words' in query:
            Speak("speak Sir!")
            jj = takecommand()
            Speak(f"you said : {jj}")
        elif 'my location' in query:
            Speak("Ok Sir , Wait A second!")
            webbrowser.open(
                'https://www.google.com/maps/@27.1830143,78.2704681,8.61z')

        elif 'temperature' in query:
            Temp()
        elif 'downloading' in query:
            SpeedTest()
        elif 'uploading speed' in query:
            SpeedTest()
        elif 'internet speed' in query:
            SpeedTest()
        elif 'alarm' in query:
            Speak("Enter the time!")
            time = input(": Enter the Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up sir!")
                    playsound("D:\\WEB\\project\\spotify\\songs\\kesariya.mp3")
                    Speak("Alarm Closed!")

                elif now > time:
                    break

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("imo", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            Speak("This is what I found on the web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 5)
                Speak(result)
            except:
                Speak("no speakable data Available!")

        elif 'bye' in query:
            Speak("Ok Sir , Bye!")
            break


TaskExe()
