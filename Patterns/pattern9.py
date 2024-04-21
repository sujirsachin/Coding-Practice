def pattern9(n:int):
    for i in (range(1, n+1)):
        for j in range(0, n-i):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for j in range(0, n - i):
            print(" ", end="")
        print("")
    for i in reversed(range(1, n+1)):
        for j in range(0, n-i):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for j in range(0, n - i):
            print(" ", end="")
        print("")

pattern9(5)