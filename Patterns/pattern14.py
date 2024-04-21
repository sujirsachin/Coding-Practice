def pattern14(n: int):
    asciiOf = ord('A')
    for i in range(1, n):
        for j in range(0, i):
            print(chr(asciiOf), end="")
            asciiOf += 1
        print("")
        asciiOf = ord('A')


pattern14(6)
