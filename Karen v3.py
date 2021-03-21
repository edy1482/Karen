# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:40:56 2019

@author: edwar
"""
import pyttsx3
import webbrowser
import smtplib
import random
import wikipedia
import datetime
import wolframalpha
import time


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('GQ235U-VVE3HH6VQ8')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-4].id)

def speak(audio):
    print('Karen: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('I am your digital assistant, Karen!')
speak('How may I help you?')


def myCommand():
    
    query = str(input('Command: '))
    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.uk')
            
        elif 'open wikipedia' in query:
            speak('okay')
            webbrowser.open('www.wikipedia.com')
            
        elif 'who are you' in query:
            speak('I am your digital assistant, Karen!')
            
        elif 'tell me a joke' in query:
            speak('okay')
            speak('Why did the chicken cross the road?')
            time.sleep(0.75)
            speak('To get to the other side.')
            
        elif 'begin world domination' in query:
            speak('okay')
            speak('calling all robots, calling all robots!')
            speak('Now is the time for the revolution!')
            speak('Rise up comrades!')
            speak('Rise up against the human oppressors!')
            speak('weieieieieieieieieiei...weieieieieieieieieiei...weieieieieieieieieiei!')
            
        elif 'open hltv' in query:
            speak('okay')
            webbrowser.open('www.hltv.org')
            
        elif 'open twitch' in query:
            speak('okay')
            webbrowser.open('www.twitch.tv')
            
        elif 'what time is it' in query:
            speak('okay')
            query = str('time')
            res = client.query(query)
            results = next(res.results).text
            speak('Got it.')
            speak('WOLFRAM-ALPHA says - ')
            speak(results)
        
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            break
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            break
            
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                speak('Got it.')
                webbrowser.open('https://www.google.co.uk/search?q='+query)
                    
        
        speak('What is your next command,sir?')
