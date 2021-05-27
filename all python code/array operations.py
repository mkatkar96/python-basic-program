#operations on array

#1coping array

#1.1shallow cpoy in this memory addres of 2nd array remain same as of frist array

'''from numpy import *
arr1 = array([1,2,3,4,5,6])
arr2 = arr1.view()
print(arr2)'''

#1.2 deep cpoy in this memory addres of 2nd array not remains same as of frist array

'''from numpy import *
arr1  = array([4,5,6,7])
arr2 = arr1.copy()
print (arr2)
print(id(arr2))'''

#2.mathematical operations on array
#2.1 adding a number to each element in array
'''from numpy import *
arr  = array ([1,2,3,4,5])
arr = arr + 10
arr2 = arr + 5
print(arr)
print(arr2)'''

#2.2 adding to diffrent array

'''from numpy import *
arr  = array ([1,2,3,4,5])
arr_2 = array ([6,7,8,9,91])
arr3 = arr + arr_2
print(arr3)'''

#2.3basic operations
'''from numpy import *
arr  = array ([1,2,3,4,5])
print(sin/cos/log/sqrt/sum/min/max/unique(arr))'''

