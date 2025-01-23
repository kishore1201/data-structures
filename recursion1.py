#recursion
def getrowcount(bno):
    if lstbench==5:
        return 1
    else:
        return 1+getrowcount(bno+1)
# in class room

print(getrowcount())
