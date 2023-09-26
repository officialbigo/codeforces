for t in range(int(input())):
    n = int(input())
    x = input()
    arr = []
    for i in x:
        arr.append(i)
    l = 0
    r = n-1
    same = 0
    diff = 0
    possibilites = set()
    while l < r:
        if arr[l] == arr[r]:
            same += 1
        else:
            diff += 1
        l += 1
        r -= 1
    if n % 2 == 0:
        while same >= 0:
            possibilites.add(2*same+diff)
            same -= 1
    else:
        while same >= 0:
            possibilites.add(2*same+diff)
            possibilites.add((2*same+diff)+1)
            same -= 1
    ans = ""
    for i in range(n+1):
        if i in possibilites:
            ans += "1"
        else:
            ans += "0"
    print(ans)
