import speech_recognition as sr
import subprocess, time
from pynput.keyboard import Key, Controller
import keyboard, webbrowser

keyboardTwo = Controller()
print("-" * 60)
print("!!!PLEASE MAKE SURE YOU HOLD DOWN 'INS' FOR THE WHOLE TIME YOU SPEAK!!!")
print("-" * 60)

while True:
    while keyboard.is_pressed('ins'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening... ")
            audio = r.listen(source)
            BING_KEY = ""  #API KEY HERE
            word = r.recognize_bing(audio, key=BING_KEY)
            wordS = word.lower()
            print(wordS)


        if "league" in wordS or "legends" in wordS or "lol" in wordS:
            subprocess.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
            time.sleep(1.5)
            keyboardTwo.press(Key.alt_gr)
            keyboardTwo.press(Key.tab)
            keyboardTwo.release(Key.alt_gr)
            keyboardTwo.release(Key.tab)
            time.sleep(0.01)
            keyboardTwo.press(Key.alt_gr)
            keyboardTwo.press(Key.shift_l)
            keyboardTwo.press(Key.tab)
            time.sleep(0.01)
            keyboardTwo.release(Key.tab)
            keyboardTwo.release(Key.shift_l)
            keyboardTwo.release(Key.alt_gr)
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            time.sleep(2.5)
            keyboardTwo.type("LEAGUEPASSWORD")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            #
        elif "github" in wordS:
            try:
                webbrowser.open("http://www.github.com/cameronmkj", new=1, autoraise=True)
                break
            except ValueError:
                webbrowser.open("http://www.github.com/cameronmkj", new=1, autoraise=True)
            #
        elif "email" in wordS or "gmail" in wordS:
            try:
                webbrowser.open("http://www.gmail.com", new=1, autoraise=True)
                break
            except ValueError:
                webbrowser.open("http://www.gmail.com", new=1, autoraise=True)
            #
        elif "gg" in wordS:
            try:
                webbrowser.open("http://euw.op.gg/summoner/userName=mukhanics", new=1, autoraise=True)
                break
            except ValueError:
                webbrowser.open("http://euw.op.gg/summoner/userName=mukhanics", new=1, autoraise=True)
            #
        elif "flame" in wordS:
            keyboardTwo.type("Play support, no previous IQ or role experience needed.")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            keyboardTwo.type("Pick Janna NOW! ")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            keyboardTwo.type("Achieve High eLO Today.")
            keyboardTwo.press(Key.enter)
            keyboardTwo.release(Key.enter)
            #
        elif "firefox" in wordS:
            webbrowser.open("www.google.com", new=1, autoraise=True)
        elif "chrome" in wordS:
            subprocess.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
        elif "visual studio code" in wordS or "vsc" in wordS or "code" in wordS:
            subprocess.call(['C:\Program Files\Microsoft VS Code\code.exe'])
        elif "youtube" in wordS:
            try:
                webbrowser.open("https://www.youtube.com", new=1, autoraise=True)
                break
            except:
                webbrowser.open("https://www.youtube.com", new=1, autoraise=True)

        elif "steam" in wordS:
            subprocess.call(['C:\Program Files (x86)\Steam\steam.exe'])
        elif "tilted" in wordS:
            try:
                webbrowser.open("https:www.giphy.com/search/cute-animals", new=1, autoraise=True)
                break
            except:
                webbrowser.open("https:www.giphy.com/search/cute-animals", new=1, autoraise=True)