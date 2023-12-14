T = int(input())
for t in range(T):
    row, column = map(int, input().split())
    arr = []
    for x in range(row):
        x = input()
        arr.append(x)
    if column < 4:
        print("NO")
    else:
        prev = ""
        for j in range(column):
            for i in range(row):
                if arr[i][j] == "v" and prev == "":
                    prev = "v"
                    break
                elif arr[i][j] == "i" and prev == "v":
                    prev = "i"
                    break
                elif arr[i][j] == "k" and prev == "i":
                    prev = "k"
                    break
                elif arr[i][j] == "a" and prev == "k":
                    prev = "a"
                    break
            if prev == "a":
                break
        if prev == "a":
            print("YES")
        else:
            print("NO")
