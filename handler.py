import json
import requests


def hello(event, context):

    response = requests.get('https://httpbin.org/ip')
    public_ip = response.json()['origin']

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "ip": public_ip
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
