import speech_recognition as sr
import pyttsx3

import notion
import responses

name = 'arnold'

listener = sr.Recognizer()
listener.energy_threshold = 105 # use python -m speech_recognition
listener.dynamic_energy_threshold = True

tts = pyttsx3.init()
tts.setProperty('rate', 120)
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)

def output(input):
    tts.say(input)
    tts.runAndWait()

def awaitCommand():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening ..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command = command.replace(name, '')
                print(command)
                return command
            else:
                print(command)
    except:
        pass

def commandHandler(command):
    if 'notion' in command:
        if 'today' in command:
            data = notion.getTodayEvents()
            response = responses.todayEvents(data)
            output(response)

        if 'tomorrow' in command:
            data = notion.getTomorrowEvents()
            response = responses.tomorrowEvents(data)
            output(response)
        
        if 'when is' in command:
            # Returns anything after "when is"
            event = command.split("when is", 1)[1]
            
            # TODO error response if cmd is incorrect or no event
            dt, day = notion.getTimeEvent(event)
            response = responses.timeEvent(dt, day, event)
            output(response)

def main():
    command = awaitCommand()
    commandHandler(command)

if __name__ == "__main__":
    main()