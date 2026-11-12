def minimumRecolors(blocks:str,k:int)->int:
    ans=101
    cnt=0
    for i,c in enumerate(blocks):
        # print(c, end=" ")
        # print(cnt, end="\n")
        if c=='W':
            # print(c,end=" ")
            cnt+=1
            # print(cnt,end="\n")
        left=i-k+1
        if left<0:
            continue
        ans=min(ans,cnt)
        if blocks[left]=='W':
            cnt-=1
    return ans

if __name__=="__main__":
    blocks="WBBWWBBWBW"
    k=7
    print(minimumRecolors(blocks,k))