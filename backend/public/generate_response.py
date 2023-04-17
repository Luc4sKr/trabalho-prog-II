import json
from flask import Response

def generate_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if (message):
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
