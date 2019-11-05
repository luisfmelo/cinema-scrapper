import base64


def decode_string(b64_str: str) -> str:
    return base64.b64decode(b64_str)