import sys

B = 256
Q = 101


def read_input():
    try:
        ievade = input().rstrip()
    except EOFError:
        return ("", "")

    if "f" == ievade.lower():
        try:
            file = input().strip()
            with open("./tests/" + file, mode="r") as f:
                pattern, text = f.readlines()
            return (pattern.rstrip(), text.rstrip())
        except OSError as e:
            print(e)
            return ("", "")
    elif "i" == ievade.lower():
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)
    else:
        return ("", "")


def print_occurrences(output):
    if len(output) == 0:
        print("-1")
    else:
        print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    global B, Q
    r = 0

    pattern_len = len(pattern)
    for i in range(pattern_len):
        r = (B * r + ord(pattern[i])) % Q

    text_len = len(text)
    pattern_hash = 0
    text_hash = 0
    h = pow(B, pattern_len - 1, Q)

    result = []

    for i in range(pattern_len):
        pattern_hash = (B * pattern_hash + ord(pattern[i])) % Q
        text_hash = (B * text_hash + ord(text[i])) % Q

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i + pattern_len]:
            result.append(i)

        if i < text_len - pattern_len:
            text_hash = (B * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_len])) % Q

    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
