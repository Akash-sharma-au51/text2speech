import pyttsx3
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


text = open("text.txt")
result = text.read()
engine.say(result)
engine.runAndWait()
