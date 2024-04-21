def pattern13(n: int):
    end = 1
    for i in range(1, n):
        for j in range(0, i):
            print(end, end=" ")
            end += 1
        print("")

pattern13(6)