from command import *


def entry(text):
    response(greetings() + " sir, " + awake())
    wake = "juliet"
    while True:
        if text.count(wake) > 0:
            response("i am here sir ready for your next command")

        command(text)
