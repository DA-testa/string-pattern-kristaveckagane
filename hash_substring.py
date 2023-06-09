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
            with open('./tests/06', 'r') as f:
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
    th= 0
    for i in range(plen):
        th = (B * th + ord(text[i])) % Q
    for s in range(tlen - plen + 1):
        if th == r:
            if text[s:s + plen] == pattern:
                result.append(s)
        if s < tlen - plen:
            th = (th - m * ord(text[s])) % Q
            th = (th * B + ord(text[s + plen])) % Q
            th = (th + Q) % Q
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
