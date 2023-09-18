from dataclasses import dataclass

from model.cell_prediction_response import CellPredictionResponse


@dataclass
class RecsResponse:
    """
        Represents a response object of recs endpoint. Contains safe click probability of a all cells in request.

        Attributes:
            board_predictions (list[CellPredictionResponse]): list of predictions for all cells in request
    """

    board_predictions: list[CellPredictionResponse]