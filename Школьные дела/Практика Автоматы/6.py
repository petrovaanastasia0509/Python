max_r = 0
for n in range(1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '11' + b + '11'
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if r <= 113:
        max_r = max(r, max_r)
print(max_r)