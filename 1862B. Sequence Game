T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            ans.append(1)
        ans.append(arr[i])
    print(len(ans))
    output = ' '.join(str(element) for element in ans)
    print(output)
