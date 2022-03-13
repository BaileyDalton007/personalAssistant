import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

import notion
import responses

# activation word for the assistant, all lowercase
NAME = 'mirror'

listener = sr.Recognizer()
listener.energy_threshold = 105 # use python3.7 -m speech_recognition
listener.dynamic_energy_threshold = True

def output(input):
    mp3_fp = BytesIO()
    tts = gTTS(input, lang="en", tld="com")
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    song = AudioSegment.from_file(mp3_fp, format="mp3")
    play(song)

def awaitCommand():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening ..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if NAME in command:
                return command
            else:
                return 1
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
    else:
        output("Command is not recognized")

def main():
    command = awaitCommand()

    if command != 1:
        commandHandler(command)

if __name__ == "__main__":
    while True:
        main()