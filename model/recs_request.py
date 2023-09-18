from dataclasses import dataclass

from model.cell_prediction_request import CellPredictionRequest

@dataclass
class RecsRequest:
    """
        Represents a request object of recs endpoint. Contains data about all cells to predict

        Attributes:
            cell_prediction_requests (list[CellPredictionRequest]): list of cells predictions in request
    """

    cell_prediction_requests: list[CellPredictionRequest]
