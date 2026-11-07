max_n = 0
for n in range(100000):
    b = ''
    n_old = n
    for _ in range(2):
        b = bin(n)[2:]
        if n % 2 == 0:
            b += '1'
        else:
            b += '0'
        n = int(b, 2)
    r = int(b, 2)
    if r < 171:
        max_n = max(n_old, max_n)
print(max_n)