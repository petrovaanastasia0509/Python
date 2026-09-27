n=int(input())
zero=0
otr=0
summ=0
k=0
for i in range(n):
    x=int(input())
    if x == 0:
        zero+=1
    if x <0:
        otr+=1
    if x>0:
        k+=1
        summ+=x
print(f"Нулей: {zero}")
print(f"Отрицательных: {otr}")
print(f"Среднее положительных: {summ/k:.2f}")
