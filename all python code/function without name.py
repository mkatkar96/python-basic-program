#anonymous function- function without name (LAMBDA)
#1.EG-
'''f = lambda a,b : a+b
result = f(5,6)
print(result)'''

# TYPES
#1.1-FILTER,map,reduce(to use reduce we have to import functool)

nums =[1,2,3,45,6,7,8,9]
even = list(filter(lambda n:n%2==0, nums))
double = list(map(lambda n: n*2,nums))
sum = list(reduce(lambda a,b:a+b,nums))
print(even)
print(double)
print(sum)