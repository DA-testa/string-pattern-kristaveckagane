def read_input():
    try:
        ievade = input().rstrip()
    except EOFError:
        return ("", "")

    if "f" == ievade.lower():
        try:
            file = input("").rstrip()
            with open("/tests/" + file, mode="r") as f:
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
