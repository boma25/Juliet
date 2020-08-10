import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import random
import requests
import webbrowser
import pycountry as py
from conversation import *
import wolframalpha



def response(text):
    try:
        engine = pyttsx3.init()
    except ImportError:
        print('requested driver not found')
    except RuntimeError:
        print('driver fails to initialize')
        voices = engine.getProperty('voices')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()


def listen_to_me():
    speech = sr.Recognizer()
    while True:
        command = ''
        with sr.Microphone() as source:
            speech.pause_threshold = 1
            speech.adjust_for_ambient_noise(source, duration=1)
            audio = speech.listen(source)

        try:
            command = speech.recognize_google(audio)
            break

        except sr.UnknownValueError:
            response('sorry, come again!')
        except sr.RequestError:
            response('please check your network connection and try again ')
    return command.lower()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])


def greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greet = 'good morning'

    elif 12 <= hour < 18:
        greet = 'good after noon'

    else:
        greet = 'good evening'

    return greet


def time_tell():
    h = int(datetime.datetime.now().strftime("%I"))
    m = datetime.datetime.now().strftime("%M")
    p = datetime.datetime.now().strftime("%p")
    if m == '00':
        m = 'O\'clock'
        p = ''
    str_time = str(h) + " " + m + " " + p
    return str_time


def tell_date():
    d = datetime.datetime.now().strftime("%d")
    m = datetime.datetime.now().strftime("%A")
    i = datetime.datetime.now().strftime("%b")
    y = datetime.datetime.now().strftime("%Y")
    today = m + " the " + d + " of " + i + " " + y
    return today


def get_date(text):
    MONTHS = ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
    text = text.lower()
    today = tell_date()

    if text.count("today") > 0:
        return today
    today = datetime.datetime.now()
    day = -1
    day_of_the_week = -1
    month = -1
    year = today.year
    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        if word in DAYS:
            day_of_the_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

        if month < today.month and month != -1:
            year = year + 1
        if day < today.day and month == -1 and day != -1:
            month = month + 1
        if month == -1 and day == -1 and day_of_the_week != -1:
            current_day_of_week = today.weekday()
            dif = day_of_the_week - current_day_of_week
            if dif < 0:
                dif += 7
                if text.count("next") >= 1:
                    dif += 7
            return today + datetime.timedelta(dif)

    if month == -1 or day == -1:
        return None

    return datetime.date(month=month, day=day, year=year)


def awake():
    inp = "Hi"
    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    if results[results_index] >= 0.9:
        for tg in data["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]
        return random.choice(responses)


def talk(inp):
    while True:
        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        if results[results_index] >= 0.89:
            return tag
        else:
            response("i did not get you can you come again")
            break


def site(inp):
    word = inp.split()
    domain = ""
    for o in word:
        if o != "open":
            domain = o

    prefix = [".com", ".co", ".za", ".org", ".ag", ".edu.ng"]
    for i in prefix:
        url = 'https://www.' + domain
        url = url + i
        try:
            requests.get(url)
            webbrowser.open(url)
            response('it is open')
            break
        except:
            response('hold on, i am coming')
        response('Web site does not exist')


def jokes():
    res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    if res.status_code == requests.codes.ok:
        response(str(res.json()['joke']))


def news():
    country = 'nigeria'
    cunt = py.countries.search_fuzzy(country)
    cunt = cunt.pop(0)
    cunt = cunt.alpha_2
    try:
        url = ('https://newsapi.org/v2/top-headlines?'
               'country=' + cunt + '&'
                                   'apiKey=9d39bf75c22142bbafefab76e14dccb7')
        feedback = requests.get(url)
        news = feedback.json()
    except:
        response("please check your internet connection and try again")
    for new in news['articles']:
        response(str(new['title']))
        response(str(new['description']))


def search(text):
    question = text
    app_id = 'XEVKA5-6KGXVYWRY7'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text 
    response(answer)
