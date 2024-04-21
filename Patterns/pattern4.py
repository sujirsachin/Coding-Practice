def pattern4(n:int):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print("")

pattern4(5)