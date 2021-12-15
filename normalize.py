from hazm import *
import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source :
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio, language= 'fa-IR')
			print(said)
		except Exception as e:
			print("Exception :" + str(e))
	return said


text = get_audio()
normalizer = Normalizer()
c=normalizer.normalize(text)
c=c.split()
print(c)
stemed=[]
for i in range(len(c)):
    stemmer=Stemmer()
    stemed.append(stemmer.stem(c[i]))
print(stemed)
