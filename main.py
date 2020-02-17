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


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Alice: ' + audio )
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH  < 12:
        speak(f"Good Morning Aiden !")
    
    if currentH >= 12 and currentH < 18:
        speak(f"Good Evening Aiden !")
    
    if currentH > 18 and currentH != 0:
        speak(f"Good evening Aiden  !")

greetMe()


speak(f"Hello Aiden, I am your digital assistant, my name is Alice")
speak(f"How may I help you Aiden ")


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
        speak("Sorry Aiden ! I didnt get that! Try typing the command!")
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

        user = "Aiden"

        query = myCommand()
        query = query.lower()


        #                       ----- GREETING -----

        if "hello" or "good" in query:
            speak('Hello {}'.format(user))

        elif "how are you" in query or "how are you going":
            speak('I am fine, I can do 100 pushs up if I have hand') 




        #                       ----- OPEN WEBSITE -----
               
            
        elif "open youtube" in query:
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
                    print('Yes sir')
                    webbrowser.open('www.gucci.com')
            


        #                           ----- WEATHER NOW -----


        elif 'weather' in query and 'now' in query or 'today' in query:
            json_data = getWeatherJSONData()

            summary = json_data['currently']['summary']
            # Calculate F to C
            temC = (json_data['currently']['temperature']-32)*5/9
            speak("the weather is {} and the temperature is {} degree celcius".format(summary,str(round(temC,2))))


        #                           ----- WEATHER TOMMOROW -----

        elif "weather tommorow" in query:
            json_data = getWeatherJSONData()

            summary = json_data['daily']['data'][0]['summary']
            # calculate F to C
            temMinC = (json_data['daily']['data'][0]['temperatureMin']-32)*5/9
            temMaxC = (json_data['daily']['data'][0]['temperatureMax']-32)*5/9
            speak("the weather tommorow is {} and the temperature is about {} to {} degree celcius".format(summary,str(round(temMinC,2)),str(round(temMaxC))))


        #                           ----- QUIT PROGRAM -----


        elif "bye" in query:
            speak('good bye {}'.format(user))
            sys.exit()
        
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')




        speak('Next Command! Sir!')



        