import datetime
import pyjokes

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_joke():
    return pyjokes.get_joke()
