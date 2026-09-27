start_sum=int(input())
target_sum=int(input())
percent=int(input())
k=0
percent/=12
while start_sum<target_sum:
    k+=1
    start_sum+=((percent/100)*start_sum)
    print(f"{k} - {start_sum:.2f}")
