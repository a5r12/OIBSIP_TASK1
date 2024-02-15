import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    elif  hour>=18 and hour<20:
        speak("Good Evening!") 

    else:
        speak("Good Night!")

    speak(' i am  iirra ')

def inputcommand():
    i = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        speak('listening')
        i.pause_threshold =1
        audio = i.listen(source)

    try:
        print('processing...')
        query = i.recognize_google(audio , language='en-in')
        print(f" user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        speak("say that again please...")
        return "None"
    return query

 
greeting()   
while True:
    query = inputcommand()
    query= query.lower()
    
    question =["the time","who are you","the date"]
    hour= datetime.datetime.now().strftime("%H")
    minute= datetime.datetime.now().strftime("%M")
    sec= datetime.datetime.now().strftime("%S")
    date=datetime.datetime.now().strftime("%Y-%m-%d ")
    answer = [f"the time is {hour} hour , {minute} minutes and {sec} seconds"," i am iira ..your voice assistant",f"today is the {date}"]

    if question[0] in query:
        print(answer[0])
        speak(answer[0])

    elif question[1] in query:
        print(answer[1])
        speak(answer[1])

    elif question[2] in query:
        print(answer[2])
        speak(answer[2])

    elif "hello" in query:
        print(" hello .., how may i help you")
        speak("hello .., how may i help you ")

    elif 'wikipedia' in query:
        speak("serching  wikipedia")
        query= query.replace('wikipedia', ' ')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
        
    elif 'open google' in query:
        speak("opening google")
        webbrowser.open('google.com')

    elif 'open facebook' in query:
        speak("opening facebook")
        webbrowser.open('facebook.com')

    elif 'open instagram' in query:
        speak("opening instagram")
        webbrowser.open('instagram.com')

    elif 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")
    else:
        speak('no result found')

    
        
        
    

   