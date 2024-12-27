import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import wikipedia
import random
import pygame
import requests 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for female voice
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
pygame.init()

def speak(audio):   
    engine.say(audio)    
    engine.runAndWait()
def play_music():
    music_path = "C:\\Users\\ajith\\Downloads\\Believer(PagalWorld).mp3"
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")    
    elif 12 <= hour < 18:
        speak("Good Afternoon!")       
    else:
        speak("Good Evening!")      
        
    speak('Hello there. I am Siri, your virtual assistant. How may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# List of jokes or facts
jokes_or_facts = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Did you know that a group of crows is called a murder?",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"
    # Add more jokes or facts as needed
]

# Function to tell a joke or a fact
def tell_joke_or_fact():
    joke_or_fact = random.choice(jokes_or_facts)
    speak(joke_or_fact)
    print(joke_or_fact)

if __name__ == "__main__":
    wishMe()
    pygame.mixer.init() 
    flag = True
    while flag:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open times of india' in query:
            webbrowser.open("timesofindia.indiatimes.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print({strTime})
        elif 'how are you' in query:
            speak("I am fine, thank you. How can I help you today")
            print("I am fine, thank you. How can I help you today")
        elif 'joke' in query or 'fact' in query: 
             tell_joke_or_fact()
        elif 'play music' in query:
            speak("Sure! Playing music.")
            play_music()
        elif 'exit the program' in query:
            speak("Thank you, see you soon.")
            print("Thank you, see you soon.")
            flag = False

