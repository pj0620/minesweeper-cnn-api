from typing import Optional


def get_exception_message(e: Optional[BaseException]) -> str:
    if e is None:
        return ''
    else:
        return e.args[0]

