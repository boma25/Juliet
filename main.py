from command import *

response(greetings() + " sir, " + awake())
wake = "juliet"
while True:
    text = input('type here:')
    if text.count(wake) > 0:
        response("i am here sir ready for your next command")

    command(text)
