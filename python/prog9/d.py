def alphapat(n):
    num = 65 # ASCII Value for A
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print("\r")

n = 5
alphapat(n)
