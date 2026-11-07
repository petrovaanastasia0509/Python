def to_base_3(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

for n in range(1, 10001):
    n3 = to_base_3(n)
    res = ''
    p = 1
    for c in n3:
        if c != '0':
            p *= int(c)
    s = max(map(int, list(n3))) - min(map(int, list(n3)))
    p_3 = to_base_3(p)
    s_3 = to_base_3(s)
    if p <= s:
        res = p_3 + s_3
    else:
        res = s_3 + p_3
    res = int(res, 3)
    if res == 113:
        print(n)
        break