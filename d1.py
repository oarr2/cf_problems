t = int(input())
for _ in range(t):
    n,m = list(map(int, input().split()))
    max_value = 0
    for _ in range(n):
        arr = list(map(int, input().split()))
        arr = [-1] + arr[1:] + [100000000000000000000000]
        #print(arr)
        arr.sort()
        flag = False
        initial_val = 0
        for index in range(1, len(arr)):
            if arr[index] - arr[index - 1] == 2 and flag == False:
                flag = True
            elif arr[index] - arr[index - 1] >= 2 and flag == True:
                initial_val = arr[index - 1] + 1
                break
            elif arr[index] - arr[index - 1] > 2:
                initial_val = arr[index - 1] + 2
                break

        #print("init", initial_val)
        max_value = max(max_value, initial_val)
    #print("max val", max_value)
    if m <= max_value:
        print(max_value * (m + 1))
    else:
        ans = max_value * (max_value + 1) // 2
        ans = (m * (m + 1) // 2) - ans
        ans = ans + (max_value * (max_value + 1))
        print((ans)) 