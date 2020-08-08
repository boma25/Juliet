from functions import *
NOTE_STR = ["make a note", "write this down", "take this down", "take note"]
calender_str = ["what do i have", "do i have plans", "am i busy", "am i free"]


def command (text):
    for phrase in calender_str:
        if phrase in text:
            response('hi')

    for phrase in NOTE_STR:
        if phrase in text:
            response("what would you like me to write down")
            note_t = listen_to_me()
            note(note_t)
            response("your note has been sucsessfully saved")

    talk(text)