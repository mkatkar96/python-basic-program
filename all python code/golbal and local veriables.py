#1.global verible and local veriable

#eg-

'''a= 10    #this a is a global veriable
def something():
    a = 15         #and this a is a local veriable because this is inside function and it is local to fuction
    print (a)
something()
print(a)'''

 #1.1 use golbal veriable inside afunction by calling a keyword "global"

'''a= 10
def something():
    global a
    a = 15
    print (a)
something()
print(a)'''

 #1.2 use multiple golbal veriales inside a local veriable

a= 10
b =20
def something():
    a = 15
    x = globals()["a"]   #a is in square brack. because we only want to acees a.
    print (a)
something()
print(a)

