import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# adjust the speed
engine.setProperty('rate', 100)
engine.setProperty('volume',1)
engine.say("Hello this is acharya collage")
engine.runAndWait()