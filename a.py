t = int(input())
for x in range(t):
    k = int(input())
    s = input()
    if len(s) >= 2 and s[0] != s[len(s) - 1]:
        print("yes")
    else:
        print("no")