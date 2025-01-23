#array
#syntax --> array("type_code",[])
''' import array as ar
   arr=ar.array('i',[1,2,3,4,5])
   print(arr)
'''
# in python array have dynamic memory 
from array import *
arr=array('i',[1,2,3,4,5])
print(arr)
# arr=array('i',[1,2,3,4,5,-1])
#arr=array('I',[1,2,3,4,5]) only positive
#arr=array('f',[1.0,2.30,3.0,4.0,5.0]) in point
#arr=array('u',[a,s,d,f,g])    the out will be give in string "asdfg"
