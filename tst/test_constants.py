from constants.request_constants import BOARD_SECTIONS_KEY, LOCATION_KEY, ENCODED_BOARD_SECTION_KEY, GUESS_SIZE_KEY

LOCATION = [0, 3]
ENCODED_BOARD_SECTION = "ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAAAAAASAAAAIAAAAAAAAAAAIAAAAAAAAAAA" + \
                        "IAAAAAAAAAAAIAAAAAAAAAAA"
GUESS_SIZE = 9

VALID_RES_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: LOCATION,
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

EMPTY_BOARD_SECTIONS_REQUEST = {BOARD_SECTIONS_KEY: []}

NO_LOCATION_REQUEST = {BOARD_SECTIONS_KEY: [{
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

NO_ENCODED_BOARD_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: LOCATION,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

NO_GUESS_SIZE_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: LOCATION,
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
}]}

LOCATION_NOT_LIST_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: 'invalid',
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

LOCATION_WRONG_SIZE_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: [1, 2, 3],
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

LOCATION_WRONG_TYPE_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: ["1", True],
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

INVALID_ENCODED_BOARD_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: LOCATION,
    ENCODED_BOARD_SECTION_KEY: 1234,
    GUESS_SIZE_KEY: GUESS_SIZE
}]}

GUESS_TYPE_WRONG_TYPE_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: LOCATION,
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: "abc"
}]}

GUESS_TYPE_EVEN_REQUEST = {BOARD_SECTIONS_KEY: [{
    LOCATION_KEY: LOCATION,
    ENCODED_BOARD_SECTION_KEY: ENCODED_BOARD_SECTION,
    GUESS_SIZE_KEY: 12
}]}


