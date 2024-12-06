'''print("Twinkle Twinkle littlte start")
for n in range(5):
    print(5*n)
    n = n+1
'''

import pyttsx3
engine = pyttsx3.init()
engine.say("Hindi mei bolo aur aache se bolo")
engine.runAndWait()