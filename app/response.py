from flask import jsonify


def error_message(message: str, status_code: int=400):
    return jsonify({'message': message}), status_code


def json_response(message: dict):
    return jsonify(message), 200
