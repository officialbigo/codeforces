T = int(input())
for t in range(T):
    left_value, right_value, n = map(int, input().split())
    n = n-2
    decrement_number = 1
    middle_array = []
    flag = 0
    previous = right_value
    right = right_value
    for i in range(n):
        current = right-decrement_number
        middle_array.append(current)
        if current < left_value:
            print(-1)
            flag = 1
            break
        decrement_number += 1
        previous = right
        right = current
    if current-left_value <= previous-current and flag == 0:
        print(-1)
        flag = 1
    if flag == 0:
        ans = ([left_value]+middle_array[::-1]+[right_value])
        output = ' '.join(str(element) for element in ans)
        print(output)
