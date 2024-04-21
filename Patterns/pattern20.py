def pattern20(n: int):
    k = n+1
    for i in range(1, n//2+2):
        for j in range(0, i):
            print('*', end="")
        for j in range(0, k - i*2):
            print(' ', end="")
        for j in range(0, i):
            print('*', end="")
        print("")
    for i in reversed(range(1, n//2+1)):
        for j in range(0, i):
            print('*', end="")
        for j in range(0, k - i*2):
            print(' ', end="")
        for j in range(0, i):
            print('*', end="")
        print("")


pattern20(9)
