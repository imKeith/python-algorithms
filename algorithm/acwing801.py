n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    print("%d"%(x[i].bit_count()),end=" ")