import datetime
import json

def getCurrentTime():
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }
    json_string = json.dumps(body)
    return json_string


