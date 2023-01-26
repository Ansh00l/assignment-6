def is_pangram(string):
    alphabet = set(string.lower())
    return len(alphabet) == 26

