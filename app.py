import speech_recognition as sr

name = 'arnold'

listener = sr.Recognizer()
listener.energy_threshold = 105 # use python -m speech_recognition
listener.dynamic_energy_threshold = True

try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print("listening ..")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if name in command:
            print(command)
except:
    pass