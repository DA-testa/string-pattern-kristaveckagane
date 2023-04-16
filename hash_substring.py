# python3
B = 13
Q = 256
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    ievade = input().strip()
    if "f" == ievade.lower():
        file = input("").strip()
        try:
         file = open("./tests/" + file, mode = "r")
         pattern = file.readline().rstrip()
         text = file.readline().rstrip()
         return (pattern, text)
        except OSError as e:
            print(e)
    if "i" == ievade.lower():
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    global B,Q
    r = 0
    # this function should find the occurances using Rabin Karp alghoritm 
    intpattern = int(pattern)
    intpattern_len=len(intpattern)
    for i in range(intpattern_len):
     r = (B*r + ord(pattern[i])) % Q
    tlen = len(text)
    plen=len(pattern)
    m = 1
    for i in range(1,plen):
     m = (multiple r * B) % Q

    # and return an iterable variable
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

