def pattern17(n: int):

    for i in range(1, n + 1):
        for j in range(0, n - i):
            print(" ", end="")
        asciiStart = ord('A')
        for j in range(0, i):
            print(chr(asciiStart), end="")
            asciiStart += 1
        asciiStart -= 2
        for j in reversed(range(0, i-1)):
            print(chr(asciiStart), end="")
            asciiStart -= 1
        for j in range(0, n - i):
            print(" ", end="")
        print("")


pattern17(4)
