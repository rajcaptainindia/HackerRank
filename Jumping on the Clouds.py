def jumpingOnClouds(c):
    n=len(c)
    i=0
    ans=0
    if(n==2):
        ans=1
    else:
        while(i<n-2):
            if c[i+2]==0:
                ans=ans+1
                i=i+2
            elif c[i+1]==0:
                ans=ans+1
                i=i+1
        if c[n-3]==1:
            ans=ans+1
    return ans
