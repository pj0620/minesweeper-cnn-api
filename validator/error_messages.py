from constants.request_constants import BOARD_SECTIONS_KEY

REQUEST_NOT_A_DICTIONARY_ERROR_MESSAGE = 'request is not a dictionary'
BODY_MUST_CONTAIN_BOARD_SECTIONS_PROP_ERROR_MESSAGE = f'request must contain {BOARD_SECTIONS_KEY} property'
BOARD_SECTIONS_NOT_LIST_ERROR_MESSAGE = f'{BOARD_SECTIONS_KEY} property must contain a list of cells to predict'
BOARD_SECTIONS_EMPTY_ERROR_MESSAGE = f'{BOARD_SECTIONS_KEY} property must contain a list of cells to predict'
KEY_NOT_PROVIDED_ERROR_MESSAGE = 'prediction input at index {} does not contain {} key'
INVALID_LOCATION_ERROR_MESSAGE = 'prediction input at index {} has invalid {}: {}'
INVALID_ENCODED_BOARD_ERROR_MESSAGE = 'prediction input at index {} has invalid {}, should be a base64 ' \
                                      'encoded string: {} '
INVALID_GUESS_SIZE_MESSAGE = 'prediction input at index {} has invalid {}, should be an odd integer: {}'
