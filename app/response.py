from flask import jsonify


def error_message(message: str, status_code: int=400):
    return jsonify({'msg': message}), status_code


def json_response(message: dict, status_code: int=200):
    return jsonify(message), status_code
