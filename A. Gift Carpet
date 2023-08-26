from collections import defaultdict
T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] > n:
        print("NO")
    else:
        map1 = defaultdict(int)
        for i in arr:
            map1[i] += 1
        num = 1
        flag = 0
        for i in range(len(arr)-1):
            if map1[num] != arr[i]-arr[i+1]:
                print("NO")
                flag = 1
                break
            num += 1
        if map1[num] == arr[-1] and flag == 0:
            print("YES")
        elif flag == 0:
            print("NO")
