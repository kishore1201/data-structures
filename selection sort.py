a=[4,5,2,3,1]
for pos in range(len(a)-1):
     min =pos
     for i in range(pos+1,len(a)):
         if a[min] > a[i]:
             min =i
     a[min],a[pos]=a[pos],a[min]
print(a)
