import json
import datetime
import BestEndpoint

def endpoint(event, context):

    response = {
        "statusCode": 200,
        "body": BestEndpoint.getCurrentTime()
    }

    return response
