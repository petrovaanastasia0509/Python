def to_base_9(n):
    res = ''
    while n > 0:
        res = str(n % 9) + res
        n //= 9
    return res

for n in range(1, 10001):
    n9 = to_base_9(n)
    res = ''
    p = 1
    for c in n9:
        if c != '0':
            p *= int(c)
    s = sum(map(int, list(n9)))
    p_9 = to_base_9(p)
    s_9 = to_base_9(s)
    if p <= s:
        res = p_9 + s_9
    else:
        res = s_9 + p_9
    res = int(res, 9)
    if res == 12537:
        print(n)