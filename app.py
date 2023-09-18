from flask import Flask, request, jsonify
import json

from controller.impl.rcnn_recs_controller import CnnV1RecsController
from converter.recs_input_output_converter import convert_ext_request_to_recs_request
from model.recs_request import RecsRequest
from model.recs_response import RecsResponse
from validator.recs_input_output_validator import validate_recs_request
from validator.validation_exception import ValidationException

app = Flask(__name__)

recs_controller = CnnV1RecsController()


@app.route("/recommendations", methods=['POST'])
def hello_world():
    body_input = json.loads(request.data)
    print(f'received new cell recommendation request: {body_input}')
    try:
        # validate request
        validate_recs_request(body_input)

        # convert to recs request model
        recs_request: RecsRequest = convert_ext_request_to_recs_request(body_input)

        # apply converter to get output
        recs_response: RecsResponse = recs_controller.predict_cells(recs_request)

        return json.dumps(recs_response), 200

    except ValidationException as e:
        print(f'found request to be invalid: {e}')
        if isinstance(e.__cause__, AssertionError):
            return e.__cause__.args[0], 400
        else:
            return 'Invalid request', 400
