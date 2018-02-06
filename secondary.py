import speech_recognition as sr
import subprocess, time
from pynput.keyboard import Key, Controller
import keyboard

keyboardTwo = Controller()

while True:
    while keyboard.is_pressed('ins'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            BING_KEY = ""  #API KEY HERE
            word = r.recognize_bing(audio, key=BING_KEY)
            wordS = word.lower()
            print(wordS)

        if "league" in wordS or "legends" in wordS or "lol" in wordS:
            subprocess.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
            time.sleep(5)
            keyboardTwo.type("LEAGUEPASSWORD")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
        elif "github" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
            time.sleep(1.5)
            keyboardTwo.type("www.github.com/cameronmkj")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
        elif "email" in wordS or "gmail" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
            time.sleep(1.5)
            keyboardTwo.type("www.gmail.com")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
        elif "gg" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
            time.sleep(1.5)
            keyboardTwo.type("http://euw.op.gg/summoner/userName=mukhanics")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter) 
        elif "flame" in wordS:
            keyboardTwo.type("Play support, no previous IQ or Role experience needed. Achieve high elo TODAY.")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            keyboardTwo.type("Pick Janna, Get Elo.")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            keyboardTwo.type("Achieve High Elo TODAY! LOCK THAT +21lp champion pls god.")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            keyboardTwo.type("I do the big right click, you do the big e!")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
        elif "firefox" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
        elif "chrome" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
        elif "visual studio code" in wordS or "vsc" in wordS or "code" in wordS:
            subprocess.call(['C:\Program Files\Microsoft VS Code\code.exe'])
        elif "youtube" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
            time.sleep(1.5)
            keyboardTwo.type("www.youtube.com")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
        elif "steam" in wordS:
            subprocess.call(['C:\Program Files (x86)\Steam\steam.exe'])
        elif "tilted" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
            time.sleep(1.5)
            keyboardTwo.type("https://www.google.co.uk/search?q=cute+pictures+of+dogs&client=firefox-b-ab&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQ6uanlpHZAhUPXMAKHVclCTwQ_AUICigB&biw=2560&bih=1342")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)