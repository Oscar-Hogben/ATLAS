import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import subprocess
import sys
from gtts import gTTS
from time import ctime
import pyttsx3
import requests
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api

print("Program Started")

def load_config():
    with open('config.json') as json_file:
        data = json.load(json_file)
    return data

load_config()

def atlas_speak1(audio_string):
    engine = pyttsx3.init() # object creation

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(audio_string)
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()


def record_audio(ask = False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            atlas_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            r.adjust_for_ambient_noise(source)
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            
            time.sleep(1)
            print("Sorry I didn't get that")
        except sr.RequestError:
            
            time.sleep(1)
            print('Sorry, my speach service is down')
        return voice_data


def atlas_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + ('.mp3')
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    

def respond(voice_data):

    if 'atlas' in voice_data or 'Atlas' in voice_data:
        if 'Atlas' in voice_data:
            position = voice_data.find('Atlas')
        elif 'atlas' in voice_data:
            position = voice_data.find('atlas')
        else:
            atlas_speak("An unexpected error occurred")
            os.execv(sys.executable, ['python'] + sys.argv)
            exit()
        voice_data = voice_data[position:]
        print(position)
        if 'stop' in voice_data:
            print("Ok")

        elif voice_data == 'atlas exit' or 'atlas Exeter' == voice_data:
            exit()

        elif voice_data == 'atlas initiate gaming mode':
            url = 'https://www.youtube.com/watch?v=U9FzgsF2T-s'
            webbrowser.get().open(url)
            atlas_speak('Gaming mode initiated!')

        elif voice_data == 'atlas hello' or voice_data == 'atlas hi':
            atlas_speak("Hello there")

        elif 'your name' in voice_data:
            atlas_speak("My name is ATLAS")

        elif ' time ' in voice_data:
            var1 = ctime().find(':')
            hour = ctime()[var1-3:var1]
            mins = ctime()[var1+1:var1+3]
            if ':' in mins:
                mins = mins[:1]

            if int(hour) > 12:
                hour = int(hour) - 12
                timeRn = str(hour) + ':' + mins + ' pm'

            elif int(hour) <= 12:
                timeRn = hour + ':' + mins + ' am'
            
            final = 'The time is: ' + timeRn
            atlas_speak(str(final))

        elif 'search' in voice_data or ('look' in voice_data and 'up' in voice_data):
            search = record_audio('What do you want to search for?')
            if 'stop' in search:
                print("Ok")
            else:
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                var = 'Here is what I found for ', search
                atlas_speak(str(var))

        elif 'find' in voice_data or 'locate' in voice_data:
                location = record_audio('What do you want to locate?')
                if 'stop' in location:
                    print("Ok")
                else:
                    url = 'https://google.nl/maps/place/' + location + '/&ampl;'
                    webbrowser.get().open(url)
                    var = 'Here is the location of ', location
                    atlas_speak(str(var))
        
        elif 'open Gmail' in voice_data or 'open email' in voice_data:
            url = 'https://mail.google.com/'
            webbrowser.get().open(url)
            atlas_speak("Here is your gmail")

        elif 'play my main playlist' in voice_data:
            url = 'https://open.spotify.com/playlist/5rpqS0ZzdDiBff0NTaFXdM'
            webbrowser.get().open(url)
            atlas_speak("Here is your main playlist on spotify")

        elif 'open ROBLOX studio' in voice_data or 'start ROBLOX studio' in voice_data:
            subprocess.Popen('C:\\Users\\oscar\\AppData\\Local\\Roblox\\Versions\\version-03afb53edcef4231\\RobloxStudioLauncherBeta.exe')
            atlas_speak("Starting Roblox Studio beta")

        elif 'my' in voice_data and ('video' in voice_data or "video's" in voice_data) and 'YouTube' in voice_data:
            url = 'https://studio.youtube.com/channel/UCtiZnUOVq6tIhF1sBqmzXHg/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'
            webbrowser.get().open(url)
            atlas_speak("Here is your youtube videos on your channel.")

        elif 'YouTube' in voice_data:
            url = 'https://www.youtube.com'
            webbrowser.get().open(url)
            atlas_speak("Here is your home page on Youtube")

        elif 'you created' in voice_data:
            atlas_speak("I was first created on the 27th of December 2020")

        elif 'open Steam' in voice_data or 'start Steam' in voice_data:
            subprocess.Popen('D:\\ProgramFiles\\steam.exe')
            atlas_speak("Opening Steam")

        elif 'ROBLOX' in voice_data:
            url = 'https://www.roblox.com/home'
            webbrowser.get().open(url)
            atlas_speak("Here is your home page on roblox")

        elif 'open Kerbal' in voice_data or 'start Kerbal' in voice_data:
            subprocess.Popen('D:\\ProgramFiles\\steamapps\\common\\Kerbal Space Program\\Launcher.exe')
            atlas_speak("Opening Kerbal Space Program")

        elif 'reminder' in voice_data:
            config = load_config()
            print(config["ifttt_api_key"])

            find = voice_data.find('reminder')
            reminder = voice_data[find+9:]
            print(reminder)
            atlas_speak("Setting reminder now")
        
        elif 'set' and 'timer' in voice_data:
            length = record_audio('How long would you like the timer to be?')
            seconds = 0

            hours = length.find('hour')
            plural = False
            if int(hours) == -1:
                hours = length.find('hours')
                plural = True
            
            if int(hours) != -1:
                hours = length[0:int(hours)-1]
                print(str(hours) + " hours")
                hours = int(hours)
                seconds = hours * 3600 + seconds
                if plural == False:
                    length = length[(length.find('hour'))+6:]
                elif plural == True:
                    length = length[(length.find('hours'))+7:]
                print(length)
            
            mins = length.find('minutes')
            plural = True
            if int(mins) == -1:
                mins = length.find('minute')
                plural = False
            
            if int(mins) != -1:
                mins = length[0:int(mins)-1]
                print(str(mins) + " mins")
                mins = int(mins)
                seconds = mins * 60 + seconds
                if plural == False:
                    length = length[(length.find('minute'))+7:]
                elif plural == True:
                    length = length[(length.find('minutes'))+8:]
                print(length)

            secs = length.find('seconds')
            plural = True
            if int(secs) == -1:
                secs = length.find('second')
                plural = False
            
            if int(secs) != -1:
                secs = length[0:int(secs)-1]
                print(str(secs) + " secs")
                secs = int(secs)
                seconds = secs + seconds
                if plural == False:
                    length = length[(length.find('second'))+8:]
                elif plural == True:
                    length = length[(length.find('seconds'))+9:]
                print(length)
            print(seconds)

            timeEnding = seconds + time.time()

            ending = open("timerEnding", "w")
            ending.write(str(timeEnding))
            ending.close()

            timerOn = open("timerOn", "w")
            timerOn.write("True")
            timerOn.close()

            atlas_speak('Starting your timer now')
            

            
            
            
        elif 'play Spotify' in voice_data:
            config = load_config()
            resp = requests.get('https://maker.ifttt.com/trigger/spotify/with/key/' + config["ifttt_api_key"])
            atlas_speak("Playing your spotify")
            print(resp)
        
        elif 'pause Spotify' in voice_data:
            config = load_config()
            resp = requests.get('https://maker.ifttt.com/trigger/spotifypause/with/key/' + config["ifttt_api_key"])
            atlas_speak("Pausing your spotify")
            print(resp)

        elif '+' in voice_data:
            var = voice_data.find('+')
            num1 = float(voice_data[6:var])
            num2 = float(voice_data[var+1:var+999999999999])
            num3 = num1 + num2
            final = str(num1) + " plus " + str(num2) + " equals " + str(round(num3,2))
            print(final)
            atlas_speak(final)


        elif '-' in voice_data:
            var = voice_data.find('-')
            num1 = float(voice_data[6:var])
            num2 = float(voice_data[var+1:var+999999999999])
            num3 = num1 - num2
            final = str(num1) + " minus " + str(num2) + " equals " + str(round(num3,2))
            print(final)
            atlas_speak(final)

        elif 'restart' in voice_data:
            if '1968' in voice_data:
                atlas_speak("Restarting")
                atlas_speak("Warning, restarting may create errors in further restarting or the exit command")
                os.execv(sys.executable, ['python'] + sys.argv)
                exit()
            else:
                atlas_speak("You must include the admin password")


        elif ' x ' in voice_data:
            var = voice_data.find('x')
            num1 = float(voice_data[6:var])
            num2 = float(voice_data[var+1:var+999999999999])
            num3 = num1 * num2
            final = str(num1) + " times " + str(num2) + " equals " + str(round(num3,2))
            print(final)
            atlas_speak(final)


        elif '/' in voice_data:
            var = voice_data.find('/')
            num1 = float(voice_data[6:var])
            num2 = float(voice_data[var+1:var+999999999999])
            num3 = num1 / num2
            final = str(num1) + " devided by " + str(num2) + " equals " + str(round(num3,2))
            print(final)
            atlas_speak(final)

        

        elif 'goodnight' in voice_data:
            atlas_speak("Goodnight sir!")
            
            



        else:
            atlas_speak("Sorry, I don't know that")

    



time.sleep(1)
loop = 0

while 1:
    r = sr.Recognizer()
    print("How can I help you?")
    loop = loop + 1
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
    
    timerEndingFile = open("timerEnding", "r")
    timerOnFile = open("timerOn", "r")

    timerEnding = float(timerEndingFile.read())
    timerOn = timerOnFile.read()
    

    if timerEnding <= time.time() and timerOn == "True":
        atlas_speak("Timer finished!")
        timerOnFile.close()
        timerEndingFile.close()
        timerOn = open("timerOn", "w")
        timerOn.write("False")
        timerOn.close()
    
