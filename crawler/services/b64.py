import base64


def encode_string(data: str) -> str:
	encoded_bytes = base64.b64encode(data.encode("utf-8"))
	encoded_str = str(encoded_bytes, "utf-8")

	return encoded_str
