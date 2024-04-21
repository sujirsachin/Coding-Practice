def pattern10(n:int):
    for i in range(1, n):
        for j in range(0, i):
            print("*", end="")
        print("")
    for i in reversed(range(1, n+1)):
        for j in range(0, i):
            print("*", end="")
        print("")

pattern10(5)