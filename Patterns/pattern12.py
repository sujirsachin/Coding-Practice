def pattern12(n:int):
    k = n
    for i in (range(1, n+1)):
        for j in range(0, i):
            print(j+1, end="")
        for j in range(1, k*2-2):
            print(" ", end="")
        for j in reversed(range(0, i)):
            print(j+1, end="")
        k -= 1
        print("")

pattern12(6)