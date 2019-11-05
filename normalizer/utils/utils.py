def str_similarity(string: str, candidate: str):
    points = 0
    for string_word in string.split(" "):
        points += 1 if string_word in candidate else 0

    return points


def hardcoded_city(key: str):
    if "oeiras" in key:
        return key
    return ""
