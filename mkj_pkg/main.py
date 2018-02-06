import subprocess
from pynput.keyboard import Key, Controller
keyboard = Controller()

def p(string):
    print(string)

def important(important):
    print("-" * 80)
    print("!!! " + important + " !!!")
    print("-" * 80)

def call(path):
    subprocess.call([path])

def type(string):
    keyboard.type(string)

def press(button):
    keyboard.press(button)

def release(button):
    keyboard.release(button)

