def pattern19(n: int):
    spaces = 0
    for i in range(0, n):
        for j in range(0, n-i):
            print('*', end="")
        for j in range(0, spaces):
            print(' ', end="")
        for j in range(0, n-i):
            print('*', end="")
        print("")
        spaces += 2
    spaces -= 2
    for i in reversed(range(0, n)):
        for j in range(0, n-i):
            print('*', end="")
        for j in range(0, spaces):
            print(' ', end="")
        for j in range(0, n-i):
            print('*', end="")
        spaces -= 2
        print("")


pattern19(12)
