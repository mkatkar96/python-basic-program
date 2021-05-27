#1.lambda(unnamed fuction)

'''f = lambda a,b:a+b
result = f(5,3)
print(result)'''


#1.1 filter command :- it filters the ist using given comand

'''nums =[1,2,3,4,5,6,7,8]
even = list(filter(lambda n : n%2==0,nums))

print(even)'''

#1.2 map :-it can perform operation using given condition


'''nums =[1,2,3,4,5,6,7,8]
double = list(map(lambda n : n*2,nums))

print(double)'''

#1.3 reduce:- it can perform operation using given condition

from functools import reduce
nums =[1,2,3,4,5,6,7,8]
sum = reduce(lambda a,b:a+b ,nums)

print(sum)



