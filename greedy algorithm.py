amt=8
coins=[1,2,5]

coins.sort(reverse=True)
count=0
for coin in coins:
   count += amt//coin
   amt= amt%coin
if amt==0:
    print(count)
else:
    print("the change is not possible")