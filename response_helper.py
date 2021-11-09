from flask import make_response, jsonify


def successful_response(data: dict = None, status_code: int = 200):
    if str(status_code)[0] not in ['2', '3']:
        raise ValueError('The status_code is not valid as an ok response')
    return make_response(jsonify({'status': 'ok', 'data': data}), status_code)


def error_response(data: str = None, status_code: int = 400):
    if str(status_code)[0] not in ['4', '5']:
        raise ValueError('The status_code is not valid as an error response')
    return make_response(jsonify({'status': 'error', 'data': data}), status_code)
