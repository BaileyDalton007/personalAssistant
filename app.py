import speech_recognition as sr
import pyttsx3

import notion
import responses

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
            print(command)
            return command

    except:
        pass

def commandHandler(command):
    if command != None:
        if 'notion' in command:
            if 'today' in command:
                data = notion.getTodayEvents()
                response = responses.todayEvents(data)
                output(response)

            if 'tomorrow' in command:
                data = notion.getTomorrowEvents()
                response = responses.tomorrowEvents(data)
                output(response)

def main():
    command = awaitCommand()
    commandHandler(command)

if __name__ == "__main__":
    main()