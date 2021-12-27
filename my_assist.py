import pywhatkit
import speech_recognition as sc
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import time



listener = sc.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say("Welcome User!")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_commands():
    try:
        with sc.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            command = command.lower()
            if "jennie" in command:
                command = command.replace('jennie', '')
    except:
        pass
    return command


def run_jennie():
    command = take_commands()
    print(command)

    if 'hai' in command:
        reply = "Hi! How can I help you?"
        print(reply)
        talk(reply)
    elif 'your name' in command:
        reply = " Hi ! I am Jennie..."
        print(reply)
        talk(reply)
    elif 'how are you' in command:
        reply = "I am Fine, thank you" \
                "\nHow are you ?"
        print(reply)
        talk(reply)
    elif 'fine' in command:
        reply = "That sounds great!!!"
        print(reply)
        talk(reply)

        # current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M  %p')
        print(time)
        talk('Current time is' + time)

        # current date
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d : %m : %y')
        print(date)
        talk('Current time is' + date)


        # play YouTube video
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

        # wikipedia
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

        # google search
    elif 'what is' in command:
        person = command.replace('what is', '')
        url = "https://google.com/search?q=" + person
        webbrowser.get().open(url)
        talk("Here is what I found for" + person + "on google")

        # joke
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

        # google search
    elif 'search for' in command:
        search = command.replace('search for', '')
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        talk("Here is what I found for" + search + "on google")

        # current weather condition
    elif "weather" in command:
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        talk("Here is what I found for on google")

        # Current location as per Google Maps
    elif "location" in command:
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        talk("You must be somewhere near here, as per Google maps")

        # exit
    elif "bye" in command:
        print("bye")
        talk("bye")
        exit()

        # if voice command is not recognised
    else:
        print("Can you repeat it again?")
        talk("Can you repeat it again?")


while True:
    run_jennie()
    time.sleep(2)
