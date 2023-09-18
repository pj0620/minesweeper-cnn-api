from abc import ABC, abstractmethod

from model.recs_request import RecsRequest
from model.recs_response import RecsResponse


class RecsController(ABC):
    """
        Given a minesweeper cell with surrounding cells, returns the probability that that cell is
        safe to click

        Args:
            rec_request (RecsRequest): Model representation all the info needed tp predict a cell + some
                info about the cell
        Returns:
            int: The product of a and b.
    """
    @abstractmethod
    def predict_cells(self, rec_request: RecsRequest) -> RecsResponse:
        pass
