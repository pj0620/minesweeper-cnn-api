from constants.request_constants import BOARD_SECTIONS_KEY, LOCATION_KEY, GUESS_SIZE_KEY, ENCODED_BOARD_SECTION_KEY
from validator.error_messages import *
from validator.validation_exception import ValidationException


def assert_contains_key(dict_object: dict, key: str, index: int) -> None:
    assert key in dict_object, KEY_NOT_PROVIDED_ERROR_MESSAGE.format(index, key)


def check_int(x, key, index, error_format):
    assert isinstance(x, int), error_format.format(index, key, x)
    return x


def validate_recs_request(request):
    try:
        # request body must be a json object
        assert isinstance(request, dict), REQUEST_NOT_A_DICTIONARY_ERROR_MESSAGE

        # validate board section key
        assert BOARD_SECTIONS_KEY in request, BODY_MUST_CONTAIN_BOARD_SECTIONS_PROP_ERROR_MESSAGE
        prediction_inputs = request[BOARD_SECTIONS_KEY]
        assert isinstance(prediction_inputs, list), BOARD_SECTIONS_NOT_LIST_ERROR_MESSAGE
        assert len(prediction_inputs) > 0, BOARD_SECTIONS_EMPTY_ERROR_MESSAGE
        for i, prediction_input in enumerate(prediction_inputs):

            # must contain all required fields for prediction
            for k in [LOCATION_KEY, ENCODED_BOARD_SECTION_KEY, GUESS_SIZE_KEY]:
                assert_contains_key(prediction_input, k, i)

            # location is valid should be a int array of size two [x,y]
            location = prediction_input[LOCATION_KEY]
            assert isinstance(location, list), INVALID_LOCATION_ERROR_MESSAGE.format(i, LOCATION_KEY, location)
            [check_int(x, LOCATION_KEY, i, INVALID_LOCATION_ERROR_MESSAGE) for i, x in enumerate(location)]
            assert len(location) == 2, INVALID_LOCATION_ERROR_MESSAGE.format(i, LOCATION_KEY, location)

            # encoded board is a string
            encoded_board = prediction_input[ENCODED_BOARD_SECTION_KEY]
            assert isinstance(encoded_board, str), INVALID_ENCODED_BOARD_ERROR_MESSAGE.format(i,
                    ENCODED_BOARD_SECTION_KEY, encoded_board)

            # guess size should be an odd integer
            guess_size = prediction_input[GUESS_SIZE_KEY]
            assert isinstance(guess_size, int), INVALID_GUESS_SIZE_MESSAGE.format(i, GUESS_SIZE_KEY, guess_size)
            assert guess_size % 2 == 1, INVALID_GUESS_SIZE_MESSAGE.format(i, guess_size)


    except AssertionError as e:
        raise ValidationException(f"invalid request") from e
