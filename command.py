from functions import *
calender_str = ["what do i have", "do i have plans", "am i busy", "am i free"]


def command (text):
    tag = talk(text)
    conversation = ["greeting", "goodbye", "name", "age", "complements"]
    request = ["time", "date", "joke", "news", "web", "search", "note"]
    classification = ""
    for con in conversation:
        if tag == con:
            classification = "conversation"
            break
        else:
            classification = "request"
            break
            
    if classification == "conversation":
        for tg in data["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]
                ans = random.choice(responses)
                response(ans)
                break
    if classification == "request":
        offline = ["time", "date", "note"]
        online = ["joke", "news", "web", "search"]

        for o in online:
            if o == tag:
                try:
                    requests.get("https://www.google.com")
                except:
                    response("you are offline, you cannot access such features")
                    break
            else:
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg["responses"]
                        ans = random.choice(responses)
                        if tag == "date":
                            response(ans + tell_date())
                        elif tag == "time":
                            response(ans + time_tell())
                        elif tag == "news":
                            response(ans)
                            news()
                        elif tag == "joke":
                            response(ans)
                            jokes()
                        elif tag == "web":
                            site(text)
                        elif tag == "search":
                            response(ans)
                            search(text)
                        else:
                            response("i have no response for that input yet")
                        break
                break



