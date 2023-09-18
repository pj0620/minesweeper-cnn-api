import unittest
from typing import Any

from tst.test_constants import *
from tst.test_utils import get_exception_message
from validator.error_messages import *
from validator.recs_input_output_validator import validate_recs_request
from validator.validation_exception import ValidationException


class TestRecsInputOutputValidator(unittest.TestCase):
    def test_validRequest_success(self):
        validate_recs_request(VALID_RES_REQUEST)

    def test_nondict_error(self):
        self.validate_with_error_message('invalid', [REQUEST_NOT_A_DICTIONARY_ERROR_MESSAGE])

    def test_emptyDict_error(self):
        self.validate_with_error_message({}, [BODY_MUST_CONTAIN_BOARD_SECTIONS_PROP_ERROR_MESSAGE])

    def test_noBoardSections_error(self):
        self.validate_with_error_message(EMPTY_BOARD_SECTIONS_REQUEST,
                                         [BOARD_SECTIONS_EMPTY_ERROR_MESSAGE])

    def test_noLocation_error(self):
        self.validate_with_error_message(NO_LOCATION_REQUEST,
                                         [KEY_NOT_PROVIDED_ERROR_MESSAGE, LOCATION_KEY])

    def test_noBoardRegion_error(self):
        self.validate_with_error_message(NO_ENCODED_BOARD_REQUEST,
                                         [KEY_NOT_PROVIDED_ERROR_MESSAGE, ENCODED_BOARD_SECTION_KEY])

    def test_noGuessSize_error(self):
        self.validate_with_error_message(NO_GUESS_SIZE_REQUEST,
                                         [KEY_NOT_PROVIDED_ERROR_MESSAGE, GUESS_SIZE_KEY])

    def test_locationNotList_error(self):
        self.validate_with_error_message(LOCATION_NOT_LIST_REQUEST,
                                         [INVALID_LOCATION_ERROR_MESSAGE, LOCATION_KEY])

    def test_locationWrongSize_error(self):
        self.validate_with_error_message(LOCATION_WRONG_SIZE_REQUEST,
                                         [INVALID_LOCATION_ERROR_MESSAGE, LOCATION_KEY])

    def test_locationWrongType_error(self):
        self.validate_with_error_message(LOCATION_WRONG_TYPE_REQUEST,
                                         [INVALID_LOCATION_ERROR_MESSAGE, LOCATION_KEY])

    def test_encodedBoardInvalid_error(self):
        self.validate_with_error_message(INVALID_ENCODED_BOARD_REQUEST,
                                         [INVALID_ENCODED_BOARD_ERROR_MESSAGE, ENCODED_BOARD_SECTION_KEY])

    def test_guessSizeWrongType_error(self):
        self.validate_with_error_message(GUESS_TYPE_WRONG_TYPE_REQUEST,
                                         [INVALID_GUESS_SIZE_MESSAGE, GUESS_SIZE_KEY])

    def validate_with_error_message(self, validate_input: Any, err_messages: list[str]) -> None:
        with self.assertRaises(ValidationException) as cm:
            validate_recs_request(validate_input)
        message = get_exception_message(cm.exception.__cause__)
        for err_message in err_messages:
            err_message_regex = err_message.replace('{}', '.*')
            self.assertRegex(message, err_message_regex)


if __name__ == '__main__':
    unittest.main()