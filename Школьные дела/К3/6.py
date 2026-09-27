g1=input()
g2=input()
total_sum=int(input())
if (g1 in "AB")!=(g2 in "AB"):
    group=g1 if g1 in "AB" else g2
    price=5 if group == "A" else 3
    print((total_sum - price) // 2)
else:
    print("NOT TO GO")

