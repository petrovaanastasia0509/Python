x = float('inf')
max_n = 0
for n in range(3, 100000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if abs(r - 130) < x:
        x = abs(r - 130)
        max_n = n
    elif abs(r - 130) == x:
        max_n = max(max_n, n)
print(max_n)