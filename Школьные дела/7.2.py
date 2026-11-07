def average(marks):
    k=0
    dg=0
    for i in marks:
        k+=int(i)
        dg+=1
    return k/dg
n=input()
if n == '':
    print(0)
else:
    print(average(n))