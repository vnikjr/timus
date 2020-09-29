def where_we_can_go(x, y):
    ans = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (abs(i) + abs(j) == 3) and (1 <= x + i <= 8) and (1 <= y + j <= 8):
                ans += 1
    return ans


char_to_idx = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
for i in range(int(input())):
    j = input()
    x = char_to_idx[j[0]]
    y = int(j[1])
    ans = where_we_can_go(x, y)
    print(ans)
