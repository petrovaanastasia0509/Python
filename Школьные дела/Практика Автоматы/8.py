for n in range(10000, 100000):
    s = str(n)
    sum1 = int(s[0]) + int(s[2]) + int(s[4])
    sum2 = int(s[1]) + int(s[3])
    if sum1 <= sum2:
        res = str(sum1) + str(sum2)
    else:
        res = str(sum2) + str(sum1)
    res = int(res)
    if res == 621:
        print(n)
        break