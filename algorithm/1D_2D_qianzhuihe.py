def qianzhuihe_1D(num:list,l:int,r:int)->int:
    m=len(num)
    s=[0]*(m+1)
    for i in range(1,m+1):
        s[i]=s[i-1]+num[i-1]
    #     print(i,end='\n')
    # print(s)

    return s[r]-s[l-1]
def qianzhuihe_2D(num_2D,x1,y1,x2,y2)->int:
    row,col=len(num_2D),len(num_2D[0])
    s=[[0 for j in range(col+1)]for i in range(row+1)]
    for i in range(1,row+1):
        for j in range(1,col+1):
            s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+num_2D[i-1][j-1]
    print(s)
    return s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1]

if __name__=='__main__':
    # num=list(map(int,input().split()))
    num=[1,2,3,4,5,6,7,8,9]
    l, r = 5, 9

    num_2D=[[i * 5 + j + 1 for j in range(5)]for i in range(4)]
    x1,y1,x2,y2=1,1,2,2
    # print(num_2D)
    # print(num_2D[2][2])

    print("*"*30)
    print("一维前缀和：l=5,r=9")
    print("结果为%d"%qianzhuihe_1D(num,l,r))
    print("*" * 30)
    print("二维前缀和:x1=1,y1=1;x2=2,y2=3")
    print(qianzhuihe_2D(num_2D, x1, y1, x2, y2))

