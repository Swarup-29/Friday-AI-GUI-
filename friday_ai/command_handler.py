import webbrowser
import os
import wikipedia
from friday_ai.utils import get_current_time, get_joke
from friday_ai.gpt_chat import GPTChat

class CommandHandler:
    def __init__(self, speaker):
        self.speaker = speaker
        self.gpt_chat = GPTChat()

    def handle(self, query):
        if not query:
            return

        if "friday" not in query:
            self.speaker.speak("You didn't say 'Friday.' Am I not important enough?")
            return

        query = query.replace("friday", "").strip()

        if "wikipedia" in query:
            self.speaker.speak("Searching Wikipedia...")
            topic = query.replace("wikipedia", "").strip()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                self.speaker.speak(summary)
            except Exception:
                self.speaker.speak("Sorry, I couldn't find that on Wikipedia.")

        elif "time" in query:
            current_time = get_current_time()
            self.speaker.speak(f"The current time is {current_time}.")

        elif "open youtube" in query:
            self.speaker.speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            self.speaker.speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open github" in query:
            self.speaker.speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        elif "play music" in query or "play song" in query:
            music_dir = os.path.expanduser("~/Music")
            if os.path.isdir(music_dir):
                songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
                if songs:
                    song_path = os.path.join(music_dir, songs[0])
                    self.speaker.speak(f"Playing {songs[0]}")
                    if os.name == 'nt':
                        os.startfile(song_path)
                    else:
                        os.system(f"xdg-open '{song_path}'")
                else:
                    self.speaker.speak("No music files found in your Music directory.")
            else:
                self.speaker.speak("Music directory not found.")

        elif "joke" in query:
            self.speaker.speak(get_joke())

        elif any(x in query for x in ["chat", "talk", "gpt"]):
            self.speaker.speak("What would you like to talk about?")
            # To be implemented: Listen and then use GPTChat

        elif "who made you" in query or "who make you" in query:
            self.speaker.speak("I was crafted by a genius, sadly not Tony Stark, but close enough!")

        elif "exit" in query or "bye" in query:
            self.speaker.speak("Shutting down. Until next time!")
            exit(0)

        else:
            self.speaker.speak("I didn't quite get that. Could you say it again?")
