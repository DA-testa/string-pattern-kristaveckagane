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
            with open("tests/06.txt", mode="r") as f:
              lines = f.readlines()
              pattern = lines[0].rstrip()
              text = lines[1].rstrip()
            return (pattern, text)
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
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    global B,Q
    r = 0

    intpattern_len = len(pattern)
    for i in range(intpattern_len):
        r = (B * r + ord(pattern[i])) % Q
    tlen = len(text)
    plen = len(pattern)
    m = 1
    for i in range(1, plen):
        m = (m * B) % Q
    result = []
    thash = 0
    for i in range(plen):
        thash = (B * thash + ord(text[i])) % Q
    for s in range(tlen - plen + 1):
        if thash == r:
            if text[s:s + plen] == pattern:
                result.append(s)
        if s < tlen - plen:
            thash = (thash - m * ord(text[s])) % Q
            thash = (thash * B + ord(text[s + plen])) % Q
            thash = (thash + Q) % Q
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
