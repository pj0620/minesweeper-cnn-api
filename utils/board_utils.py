import base64

import numpy as np


def base64_to_flat_arr(base64_str: str) -> list[int]:
    decoded_bytes = base64.b64decode(base64_str)
    return list(decoded_bytes)


def expand_cell_bytes(bytes: list[int], guess_size: int):
    usable_values = []
    border_channel = []
    known_values = []
    for encoded_byte in bytes:
        # Extract outOfBoard by shifting right by 5 bits and taking the least significant bit
        outOfBoard = (encoded_byte >> 5) & 0b1
        # Extract isKnown by shifting right by 4 bits and taking the least significant bit
        isKnown = (encoded_byte >> 4) & 0b1

        # Extract val by masking the byte with 0b1111 to get the 4 rightmost bits
        val = encoded_byte & 0b1111

        usable_values.append(val / 8.)
        border_channel.append(outOfBoard)
        known_values.append(isKnown)

    usable_values = np.array(usable_values).reshape((guess_size, guess_size)).astype(np.float16)
    border_channel = np.array(border_channel).reshape((guess_size, guess_size)).astype(np.float16)
    known_values = np.array(known_values).reshape((guess_size, guess_size)).astype(np.float16)

    print('usable_values')
    print(usable_values)
    print('border_channel')
    print(border_channel)
    print('known_values')
    print(known_values)

    return np.stack([usable_values, border_channel, known_values], axis=2)
