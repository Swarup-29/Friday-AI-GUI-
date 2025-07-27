import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening... (Say your command)")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                query = self.recognizer.recognize_google(audio)
                print(f"You said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return ""
            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return ""
