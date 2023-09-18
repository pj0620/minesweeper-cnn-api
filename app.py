from flask import Flask, request, jsonify
import json

from validator.recs_input_output_validator import validate_recs_request
from validator.validation_exception import ValidationException

app = Flask(__name__)


@app.route("/recommendations", methods=['POST'])
def hello_world():
    body_input = json.loads(request.data)
    print(f'received new cell recommendation request: {body_input}')
    try:
        validate_recs_request(body_input)
    except ValidationException as e:
        print(f'found request to be invalid: {e}')
        if isinstance(e.__cause__, AssertionError):
            return e.__cause__.args[0], 400
        else:
            return 'Invalid request', 400
    return "Hello, World!"
