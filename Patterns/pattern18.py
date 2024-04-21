def pattern18(n: int):
    asciiOf = ord('E')
    for i in range(1, n):
        for j in range(0, i):
            print(chr(asciiOf), end=" ")
            asciiOf += 1
        asciiOf -= i + 1
        print("")


pattern18(6)
