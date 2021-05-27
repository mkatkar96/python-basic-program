#multidimentinal array

#1.two dimentinal array
'''from numpy import *
arr = array([
              [1,2,3],
              [4,5,6]
            ])
print(arr)
print(arr.dtype) #print datatype of arrray
print(arr.ndin) #gives number of dimentions of array
print(arr.shape) #prints shape of array
print(arr.size) #prints size of array
'''

#2.converting 2d array in to 1d array
'''from numpy import *
arr = array([
              [1,2,3],
              [4,5,6]
            ])
arr2 = arr.flatten() #convert 2d array in 1d array
print(arr2)'''

#3.matrix
#3.1 creating a matrix
'''from numpy import *
arr = array([
              [1,2,3,7],
              [4,5,6,8]
            ])
m = matrix (arr) # this function will create matrix
print(m)'''

      #   or

'''from numpy import *
m = matrix('1 2 3 ; 4 5 6 ; 7  8 9') #in this ;=newline
print(m)'''

#3.2 operations on matrix
#add,sub,min,max
from numpy import *
m1 = matrix('1 2 3 ; 4 5 6 ; 7  8 9') #in this ;=newline
m2 = matrix('2 5 7  ; 4 5 6 ; 7  8 9')
m3 = m1 + / * / min / max m2
print(m3)



