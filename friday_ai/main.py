import sys

def main_cli():
    from friday_ai.tts import Speaker
    from friday_ai.speech_recognizer import SpeechRecognizer
    from friday_ai.command_handler import CommandHandler

    speaker = Speaker()
    recognizer = SpeechRecognizer()
    handler = CommandHandler(speaker)

    speaker.speak("Good day! I am Friday, your AI assistant.")

    try:
        while True:
            query = recognizer.listen()
            if query:
                handler.handle(query)
    except KeyboardInterrupt:
        speaker.speak("Shutting down. Bye!")
        sys.exit(0)

def main_gui():
    import tkinter as tk
    from friday_ai.gui import FridayGUI

    root = tk.Tk()
    app = FridayGUI(root)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("--gui", "gui"):
        main_gui()
    else:
        main_cli()
