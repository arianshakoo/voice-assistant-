
import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init()

voices = engine.getProperty('voices')
new_voice_rate = 180
engine.setProperty('rate',new_voice_rate)
engine.setProperty('voice',voices[26].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def say_time():
    time_now = datetime.datetime.now().strftime("%I:%M:%S")
    hour , miniute , second = time_now.split(":")

    print(hour)
    speak(" ساعت "
     + hour
     + "او"
     + miniute
     + "دقیقه او"
     + second
     + "ثانیه")

def say_date():
    year_now = datetime.datetime.now().year
    month_now = datetime.datetime.now().month
    day_now = datetime.datetime.now().day
    
    print(year_now , month_now , day_now)
    speak("امروز "
     + str(day_now)
     + 'ام ه ماهه' 
     + str(month_now)
     + 'ه سال'
     + str(year_now))
    
def greeting():

    speak("سلام ی")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("صبحت بخیر")
    elif hour >= 12 and hour < 18:
        speak("ظهرت بخیر")
    elif hour >= 18 and hour <= 24:
        speak("عصرت بخیر")
    else:
        speak("شبت بخیر")


\
    
    

# welcome()

def bye():
    speak("روز خوبی داشته باشی")

def command_operator(command):


    switcher = {
        0: ['hi'],
        1: ["time"],
        2: ["date"],
        3: ['you' , 'who are you'],
        4: ['bye' , 'offline'],
    }

    if any(x in command for x in switcher[0]):
        greeting()
    elif any(x in command for x in switcher[1]):
        say_time()
    elif any(x in command for x in switcher[2]):
        say_date()
    elif any(x in command for x in switcher[3]):
        presentation()
    elif any(x in command for x in switcher[4]):
        bye()
        return 1

    else:
        speak('خب که چی')

    return 0





def start():

    
   
    speak("چه کاری از دستم برمیاد؟")
    is_end = 0
    
    while is_end == 0:
        command = take_command()
        if command != 1:
            is_end = command_operator(command)
        
        

