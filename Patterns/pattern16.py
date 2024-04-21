def pattern16(n: int):
    asciiOf = ord('A')
    for i in range(1, n):
        for j in range(0, i):
            print(chr(asciiOf), end="")
        print("")
        asciiOf += 1


pattern16(6)
