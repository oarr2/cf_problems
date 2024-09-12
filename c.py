t = int(input())
for _ in range(t):
    n = int(input())
    cad = input()
    mp = {}
    for letter in cad:
        if letter in mp:
            mp[letter]+=1
        else:
            mp[letter] = 1
    ans = []
    is_there_letters = True
    while is_there_letters:
        is_there_letters = False
        for letter in mp:
            if mp[letter] > 0:
                is_there_letters = True
                ans.append(letter)
                mp[letter]-=1
    for a in ans:
        print(a, end='')
    print()