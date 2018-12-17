from gtts import gTTS
import os

class speechuk:
    def __init__(self,text):
        tts = gTTS(text=text, lang='en-uk')
        tts.save("D:/wordshurikenuk.mp3")
        os.system("start D:/wordshurikenuk.mp3")
class speechus:
    def __init__(self,text):
        tts = gTTS(text=text, lang='en-us')
        tts.save("D:/wordshurikenus.mp3")
        os.system("start D:/wordshurikenus.mp3")

