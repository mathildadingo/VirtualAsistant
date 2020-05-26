# Also installed dependencies: 'pyaudio', 'pyobjc'
import speech_recognition as sr # pip3 install SpeechRecognition
from gtts import gTTS #pip3 install gTTS
from playsound import playsound #pip3 install playsound
import random
import os
import json

class VirtualAsistant:

    def __init__(self, owner, language):
        self.owner = owner
        self.language = language
        self.listen = False
        self.name = 'Alexa'

        import json
        with open(self.language + ".json") as responses:
            self.responseData = json.load(responses)

    def speak(self, voice):
        tts = gTTS(voice, lang=self.language.split("-", 1)[0])
        randomNumber = random.randint(1, 10000)
        voiceFile = "audio-" + str(randomNumber) + ".mp3"
        tts.save(voiceFile)
        playsound(voiceFile)
        os.remove(voiceFile)

    def response(self, voice):
        if "nasılsın" in voice:
            self.speak('iyiyim')
        if "kendini kapat" == voice:
            self.speak(self.responseData["shut_down"].format(self.owner))
            self.listen = False

    def stt(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            voice = ''
            try:
                voice = recognizer.recognize_google(audio, language=self.language).lower()
                print(voice) # print voice in terminal for debug
                if self.listen != True:
                    if len(voice) == 5 and self.name.lower() in voice:
                        self.listen = True
                        self.speak(self.responseData["ready"].format(self.owner))
                    else:
                        return

            except sr.UnknownValueError:
                if self.listen:
                    self.speak(self.responseData["error_dont_understand"].format(self.owner))
            except sr.RequestError:
                if self.listen:
                    self.speak(self.responseData["error_request_fail"].format(self.owner))

        if self.listen:
            self.response(voice)