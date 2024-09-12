t = int(input())
for x in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[len(numbers)//2])

