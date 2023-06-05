from gtts import gTTS
import os
import io
import eel

eel.init('web')

@eel.expose
def generate_speech(data):
	language = 'en'
	output= gTTS(text=data,lang=language,slow=False)
	output.save("output.mp3")
	os.system("start output.mp3")
	
eel.start('index.html',size=(750, 800))