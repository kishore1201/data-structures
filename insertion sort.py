a=[7,1,4,5,3,2]
for i in range(1,len(a)):
    cur=a[i]
    j=i-1
    while(j>=0 and cur<a[j] ): #for  compare and move place checking untill
          a[j+1]=a[j]
          j-=1
    a[j+1]=cur
print(a)
