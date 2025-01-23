a=[1,2,3,4,5,6]
t=10
l=0
r=len(a)-1
while(l<r):
    act=a[l]+a[r]
    if act== t:
        print(l,r)
        break
    elif act<t:
        l+=1
    elif act>t:
        r-=1
    
