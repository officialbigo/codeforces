from collections import defaultdict
import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # creating a dictionary with positions of different coloured planks
    map1 = defaultdict(list)
    for i in range(len(arr)):
        map1[arr[i]].append(i)

    # initializing the ans value to infinity
    ans = float('inf')
    for i in map1:
        # creating gap_between_planks array
        gap_between_planks = []
        prev = -1
        for j in map1[i]:
            gap_between_planks.append(j-prev-1)
            prev = j
        gap_between_planks.append(n-1-prev)

        # finding max value with index
        index = 0
        max_val = -1
        for i in range(len(gap_between_planks)):
            if gap_between_planks[i] > max_val:
                max_val = gap_between_planks[i]
                index = i

        # updating max value in gap_between_planks array
        if max_val % 2 == 0:
            max_val = (max_val//2)
        else:
            max_val = max_val//2
        gap_between_planks[index] = max_val

        # evaluating the value of ans
        ans = min(max(gap_between_planks), ans)

    # printing the minimum value answer
    print(ans)
