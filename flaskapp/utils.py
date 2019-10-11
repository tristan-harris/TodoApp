from flask import make_response, jsonify

def json_error_response(message_contents, error_code=500):
    return make_response(jsonify({"message":message_contents}), error_code)
