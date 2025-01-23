#linear search
ar=[1,2,3,4,5]
x=3
for i in range(0,len(ar)):
    if ar[i]==x:
        print(i)
        break
else:
    print("the x element not foumd in list")
'''
#using without range
ar=[1,2,3,4,5]
x=3
for i in ar:
    if i==x:
        print("yes")
        break
else:
    print("the x element not foumd in list")
    '''
