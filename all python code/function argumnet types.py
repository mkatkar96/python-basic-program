#FUNCTION ARGUMENT TYPES
#1.position argument
#eg-

'''def person(name , age):
    print(name)
    print(age)
person("mukul",22)
#or-if you dont knoow thw position of arguments.
person(age=22,name="mukul")'''

#2.default argumnet

'''def person(name , age=22):  #in this example we are passing deault value for age
    print(name)
    print(age)
person("mukul")'''

#3.verable length argument

def sum(*b) :#*b because value of b is not fixed or multiple values
    c = 0
    for i in b:
        c = c + i
    return c
result = sum(1,2,3,4,5)
print(result)

