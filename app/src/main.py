from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts

recognizer = speech_recognition.Recognizer()
recognizer.dynamic_energy_threshold = True

speaker = tts.init()
speaker.setProperty('rate', 150)

def greeting():
    global recognizer

    speaker.say("Hola, mi nombre es AIde soy la asistente virtual de Camilo, ¿Con quién tengo el gusto de hablar?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, )
                message = recognizer.recognize_google(audio, language="es-CO")
                message = message.lower()

                print(2, message)
                caller = message.split(" ")[-1]

                speaker.say(f"Mucho gusto {caller}, el señor Camilo no te puede atender en este momento pero si gustas yo puedo darle tu mensaje")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio, language="es-CO")
                message = message.lower()

                print(3, message)

                speaker.say("¿Algo más?")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio, language="es-CO")
                message = message.lower()

                print(4, message)
                if message.__contains__("no"):
                    speaker.say(f"Está bien {caller}, le daré tu mensaje")
                    speaker.runAndWait()
                    done = True
        except speech_recognition.UnknownValueError:
            speaker.say("Perdona, no entendí lo que dijiste, por favor repítelo")
            speaker.runAndWait()
            continue

def goodbye():
    speaker.say("Hasta luego, que tengas un buen día")
    speaker.runAndWait()

mappings = {
    "greeting": greeting,
    "goodbye": goodbye
}

assistant = GenericAssistant('app/resources/intents.json', intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio, language="es-CO")
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()