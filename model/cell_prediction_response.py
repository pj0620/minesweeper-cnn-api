from dataclasses import dataclass

@dataclass
class CellPredictionResponse:
    """
        Represents a request for predicting the safe click probability of a cell in a game board.

        Attributes:
            location (list[int]): The row and column indices of the cell in the board [x, y].
            safe_click_probability (float): probability that it is safe to click this cell
    """

    location: list[int]
    safe_click_probability: float
