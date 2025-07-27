import tkinter as tk
from friday_ai.tts import Speaker
from friday_ai.command_handler import CommandHandler

class FridayGUI:
    def __init__(self, master):
        self.master = master
        master.title("Friday AI - Iron Man Mode")
        master.configure(bg="#121d2b")

        self.speaker = Speaker()
        self.handler = CommandHandler(self.speaker)

        self.input_var = tk.StringVar()

        self.input_entry = tk.Entry(master, textvariable=self.input_var, width=40,
                                    font=("Consolas", 14), bg="#23395d", fg="#00ffff", insertbackground="#00ffff")
        self.input_entry.pack(pady=(10, 5))
        self.input_entry.bind('<Return>', self.process_input)

        self.send_button = tk.Button(master, text="Send", command=self.process_input,
                                     font=("Consolas", 12), bg="#0f3057", fg="#fff", activebackground="#00adb5",
                                     activeforeground="#fff")
        self.send_button.pack(ipadx=20, pady=2)

        self.output_box = tk.Text(master, height=18, width=57, state='disabled',
                                 font=("Consolas", 11), bg="#212121", fg="#39ff14", wrap='word')
        self.output_box.pack(padx=14, pady=10)

        self.speaker.speak("Friday AI Iron Man mode, GUI loaded.")

    def process_input(self, event=None):
        user_input = self.input_var.get()
        self.input_var.set("")
        self.display_message(f"You: {user_input}")

        if user_input:
            self.handler.handle(user_input)

    def display_message(self, message):
        self.output_box.config(state='normal')
        self.output_box.insert(tk.END, message + '\n')
        self.output_box.config(state='disabled')
        self.output_box.see(tk.END)
