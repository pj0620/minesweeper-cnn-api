from controller.recs_controller import RecsController
from model.cell_prediction_request import CellPredictionRequest
from model.cell_prediction_response import CellPredictionResponse
from model.recs_request import RecsRequest
from model.recs_response import RecsResponse
import numpy as np
from keras.models import load_model

from utils.board_utils import base64_to_flat_arr, expand_cell_bytes


class RCNNRecsController(RecsController):
    def __init__(self):
        model_file = 'data_model/ten_by_ten_rcnn_v15.0.h5'

        # Load the saved model from the file
        self.model = load_model(model_file)

    def predict_cells(self, rec_request: RecsRequest) -> RecsResponse:
        boards_sections = self.load_board_sections(rec_request.cell_prediction_requests)
        print(f'extracted {boards_sections.shape=}')

        bomb_probs = self.model.predict(boards_sections)
        print(f'found {bomb_probs=}')

        # build response object
        predictions = []
        for cell_prediction_request, bomb_prob in zip(rec_request.cell_prediction_requests, bomb_probs.flatten()):
            predictions.append(CellPredictionResponse(
                cell_prediction_request.location,
                float(bomb_prob)
            ))

        return RecsResponse(predictions)

    def load_board_sections(self, cell_prediction_requests: list[CellPredictionRequest]):
        board_sections = []
        for request in cell_prediction_requests:
            # decode board
            board_encoded = request.encoded_board
            board_decoded = base64_to_flat_arr(board_encoded)
            print(f'raw board section: {board_decoded}')

            # expand each data byte
            # outOfBoard << 5 | isKnown << 4 | val = 00BKVVVV
            # id converted to
            # [outOfBoard, isKnown, val]
            board_decoded = expand_cell_bytes(board_decoded, request.guess_size)
            print(f'decoded cell values: {board_decoded}')

            # convert to numpy array
            board_decoded = np.array(board_decoded)
            print(f'final board shape: {board_decoded.shape}')

            board_sections.append(board_decoded)

        # convert to np array of (guess_size, guess_size, num_cells_to_predict)
        board_sections = np.array(board_sections)

        print(f'board_sections.shape: {board_sections.shape}')

        return board_sections
