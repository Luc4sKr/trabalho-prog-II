from flask import Response, jsonify

def generate_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if (message):
        body["message"] = message

    return Response(jsonify(body), status=status, mimetype="application/json")
