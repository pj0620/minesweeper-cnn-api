import base64


def base64_to_flat_arr(base64_str: str) -> list[int]:
    decoded_bytes = base64.b64decode(base64_str)
    return list(decoded_bytes)


def expand_cell_bytes(bytes: list[int]):
    result = []
    for encoded_byte in bytes:
        # Extract outOfBoard by shifting right by 5 bits and taking the least significant bit
        outOfBoard = (encoded_byte >> 5) & 0b1

        # Extract isKnown by shifting right by 4 bits and taking the least significant bit
        isKnown = (encoded_byte >> 4) & 0b1

        # Extract val by masking the byte with 0b1111 to get the 4 rightmost bits
        val = encoded_byte & 0b1111

        result.append([val, outOfBoard, isKnown])
    return result
