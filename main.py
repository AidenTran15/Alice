import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia 
import datetime
import wolframalpha
import os
import sys
import requests
import json

user = 'Aiden'

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jason: ' + audio )
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH  < 12:
        print(f"Good Morning {user} !")
    
    if currentH >= 12 and currentH < 18:
        print(f"Good Evening {user} !")
    
    if currentH > 18 and currentH != 0:
        print(f"Good evening {user} !")

greetMe()


speak(f"Hello {user}, I am your digital assistant, my name is Jason")
speak(f"How may I help you {user}")


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak(f"Sorry {user}! I didnt get that! Try typing the command!")
        query = str(input('Command: '))

    return query


def getWeatherJSONData():
    res = requests.get('https://api.ipify.org')
    ip = res.text
    send_url = 'http://api.ipstack.com/'+ip+'?access_key=7e5ea1fda803cb076716badc347f0885&output=json&legacy=1'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longtitude']
    response = requests.get('https://api.darksky.net/forecast/24cd61bddf35c80d5e2ff15663b50ec8/'+str(lat)+','+str(lon)+'')
    jsonWeather = json.loads(response.text)
    return jsonWeather


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()
        

                        # --OPEN WEBSITE--

        if "open youtube" in query:
            speak('yes sir')
            webbrowser.open('www.youtube.com')

        elif "open instagram" in query:
            speak('yes sir')
            webbrowser.open('www.instagram.com')

        elif "open facebook" in query:
            speak('yes sir')
            webbrowser.open('www.facebook.com')

        elif "open messenger" in query:
            speak('yes sir')
            webbrowser.open('www.messenger.com')

        elif "open movie" in query:
            speak('yes sir')
            webbrowser.open('www.netflix.com')

        elif "tesla" in query:
            speak('Yes sir, let enjoy it')
            webbrowser.open('www.tesla.com')
        
        elif "shopping" or "phone" or "ipad" or "laptop" in query:
            speak('What do you want to buy')
            if 'technology' in query:
                speak('okay, i will take you to jb hifi')
                webbrowser.open('www.jbhifi.com')
            elif "cloth" in query:
                speak('what brand do you want')
                if "gucci" in query:
                    speak('Yes sir')
                    webbrowser.open('www.gucci.com')
                elif "h and m" in query:
                    speak('Yes Sir')
                    webbrowser.open('www.hm.com')

        else:
            query