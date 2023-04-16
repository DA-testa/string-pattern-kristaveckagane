B = 13
Q = 256

def read_input():
    ievade = input().strip()
    if "f" == ievade.lower():
        file = input("").strip()
        try:
            file = open("./tests/" + file, mode="r")
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
            return (pattern, text)
        except OSError as e:
            print(e)
    if "i" == ievade.lower():
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)


def print_occurrences(output):
 
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    global B,Q
    r = 0

    intpattern = int(pattern)
    intpattern_len = len(intpattern)
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

