def pattern5(n:int):
    for i in reversed(range(1, n+1)):
        for j in range(0, i):
            print("*", end="")
        print("")

pattern5(5)