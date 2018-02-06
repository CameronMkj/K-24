import speech_recognition as sr
import subprocess, time
from pynput.keyboard import Key, Controller
import keyboard, webbrowser
import mkj_pkg.main as mkj

keyboardTwo = Controller()
mkj.important("PLEASE MAKE SURE YOU HOLD DOWN THE 'INS' KEY FOR THE WHOLE DURATION OF SPEECH")
# print("-" * 60)
# print("!!!PLEASE MAKE SURE YOU HOLD DOWN 'INS' FOR THE WHOLE TIME YOU SPEAK!!!")
# print("-" * 60)

while True:
    while keyboard.is_pressed('ins'):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening... ")
            audio = r.listen(source)
            ########REMOVE LATER########
            BING_KEY = "901ff8bec4f04c679b9680be6ebf10f0"  #API KEY HERE
            word = r.recognize_bing(audio, key=BING_KEY)
            wordS = word.lower()
            print(wordS)

        if "league" in wordS or "legends" in wordS or "lol" in wordS:
            mkj.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
            time.sleep(1.5)
            mkj.press(Key.alt_gr)
            mkj.press(Key.tab)
            mkj.release(Key.alt_gr)
            mkj.release(Key.tab)
            time.sleep(0.01)
            mkj.press(Key.alt_gr)
            mkj.press(Key.shift_l)
            mkj.press(Key.tab)
            time.sleep(0.01)
            mkj.release(Key.tab)
            mkj.release(Key.shift_l)
            mkj.release(Key.alt_gr)
            mkj.press(Key.enter)
            mkj.release(Key.enter)
            time.sleep(2.5)
            mkj.type("LEAGUEPASSWORD")
            mkj.press(Key.enter)
            mkj.release(Key.enter)
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
            mkj.type("Play support, no previous IQ or role experience needed.")
            mkj.press(Key.enter)
            mkj.release(Key.enter)
            mkj.type("Pick Janna NOW! ")
            mkj.press(Key.enter)
            mkj.release(Key.enter)
            mkj.type("Achieve High eLO Today.")
            mkj.press(Key.enter)
            mkj.release(Key.enter)
            #
        elif "firefox" in wordS:
            webbrowser.open("www.google.com", new=1, autoraise=True)
        elif "chrome" in wordS:
            mkj.call(['C:\Program Files\Mozilla Firefox\Firefox.exe'])
        elif "visual studio code" in wordS or "vsc" in wordS or "code" in wordS:
            mkj.call(['C:\Program Files\Microsoft VS Code\code.exe'])
        elif "youtube" in wordS:
            try:
                webbrowser.open("https://www.youtube.com", new=1, autoraise=True)
                break
            except:
                webbrowser.open("https://www.youtube.com", new=1, autoraise=True)

        elif "steam" in wordS:
            mkj.call(['C:\Program Files (x86)\Steam\steam.exe'])
        elif "tilted" in wordS:
            try:
                webbrowser.open("https:www.giphy.com/search/cute-animals", new=1, autoraise=True)
                break
            except:
                webbrowser.open("https:www.giphy.com/search/cute-animals", new=1, autoraise=True)