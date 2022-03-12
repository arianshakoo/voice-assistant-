def tashkhis_mozoo(a):
    if 'باز کن' in a:
        return 'applications'
    elif 'سرچ کن' in a or 'جست و جو کن' in a:
        return 'search'
import os
import time
import speech_recognition as sr
from gtts import gTTS
from hazm import *
import playsound
import webbrowser as wb
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


a=str(input())
b=[]
if tashkhis_mozoo(a)=='applications':
    a=a.replace('باز کن','')
if tashkhis_mozoo(a)=='search':
    if 'سرچ کن' in a:
        a=a.replace('سرچ کن','')
    elif 'جست و جو کن' in a:
        a=a.replace('جست و جو کن','')
#    wb.open_new_tab(a)
normalizer = Normalizer()
c=normalizer.normalize(a)
c=c.split()
print(c)
stemed=[]
for i in range(len(c)):
    stemmer=Stemmer()
    stemed.append(stemmer.stem(c[i]))
print(stemed)
