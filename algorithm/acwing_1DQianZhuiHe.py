def qianzhuihe(num:list,n:int,l:int,r:int)->int:
    s=[0]*(n+1)
    for i in range(1,n+1):
        s[i]=s[i-1]+num[i-1]

    return s[r]-s[l-1]

if __name__=="__main__":
    n,m=map(int,input().split())
    num=list(map(int,input().split()))
    for i in range(m):
        l,r=map(int,input().split())
        print(qianzhuihe(num,n, l, r))
