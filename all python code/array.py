#taking array from user
from array import *

arr= array("i",[] )
n = int(input("enter the length of array"))
for e in range(n):
     x = int(input("enter the values"))
     arr.append(x)
print(arr)

val = int(input("enter element to be searched"))
print(arr.index(val))