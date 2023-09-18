from constants.request_constants import BOARD_SECTIONS_KEY, LOCATION_KEY, GUESS_SIZE_KEY, ENCODED_BOARD_SECTION_KEY
from model.cell_prediction_request import CellPredictionRequest
from model.recs_request import RecsRequest


def convert_ext_request_to_recs_request(external_request: dict) -> RecsRequest:
    board_sections: list[CellPredictionRequest] = []
    for raw_cell_prediction_request in external_request[BOARD_SECTIONS_KEY]:
        new_cell_prediction = CellPredictionRequest(
            raw_cell_prediction_request[LOCATION_KEY],
            raw_cell_prediction_request[ENCODED_BOARD_SECTION_KEY],
            raw_cell_prediction_request[GUESS_SIZE_KEY],
        )
        board_sections.append(new_cell_prediction)
    return RecsRequest(board_sections)
