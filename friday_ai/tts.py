import platform
import os

class Speaker:
    def __init__(self):
        self.os_name = platform.system()
        if self.os_name == "Windows":
            try:
                import pyttsx3
                self.engine = pyttsx3.init()
                voices = self.engine.getProperty('voices')
                female_voice = None
                for voice in voices:
                    name = voice.name.lower()
                    if "female" in name or "zira" in name or "com" in name:
                        female_voice = voice.id
                        break
                if female_voice:
                    self.engine.setProperty('voice', female_voice)
                else:
                    self.engine.setProperty('voice', voices[0].id)
            except ImportError:
                print("pyttsx3 not installed. Please run 'pip install pyttsx3'.")
                self.engine = None
        else:
            self.engine = None  # Use festival in speak()

    def speak(self, text):
        print(f"Friday says: {text}")
        if self.os_name == "Windows" and self.engine:
            self.engine.say(text)
            self.engine.runAndWait()
        elif self.os_name != "Windows":
            safe_text = text.replace("'", "'\\''")
            os.system(f'echo "(voice_rab_diphone) (SayText \\"{safe_text}\\")" | festival --pipe')
        else:
            print("Speech engine not available.")
