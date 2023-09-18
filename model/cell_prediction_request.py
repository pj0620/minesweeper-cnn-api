from dataclasses import dataclass


@dataclass
class CellPredictionRequest:
    """
        Represents a request for predicting the safe click probability of a cell in a game board.

        Attributes:
            location (list[int]): The row and column indices of the cell in the board [x, y].
            encoded_board (str): A base64 encoded representation of the entire game board.
            guess_size (int): size of window used for predicting cell. (guess_size x guess_size)
    """

    location: list[int]
    encoded_board: str
    guess_size: int
