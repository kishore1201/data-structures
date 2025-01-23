arr=[1,10,11,5,2]
for i in range(0,len(arr)-1):
    for j in  range(0,len(arr)-1):
        #if arr[j]<arr[j+1]:
           #  continue     and using elif also
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# while loop
while(True):
    a=True#local variable it will be re inatialize untill while loop runing 
    for k in  range(0,len(arr)-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
            a=False
    if a== True:
        break
    else:
        continue
print(arr)
