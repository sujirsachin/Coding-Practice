def pattern7(n:int):
    k = 1
    for i in range(1, n+1):
        for j in range(0, k):
            print("*", end="")
        k += 2
        print("")
def pattern7_2(n:int):
    k = 1
    for i in range(1, n+1):
        for j in range(0, n-i):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        for j in range(0, n - i):
            print(" ", end="")
        print("")

pattern7_2(5)