''' CONSTRUCTOR-in class bassed object oriented programing , a contructor is a special type of subroutin call to create an
object for use, often accepting arguments that the constructor uses to set required number of veriable'''
#EG-
class info:
    def __init__(self):
        self.name = 'mukul'
        self.age = 22
    def update(self):
         self.age = 40
person1 = info()
print(person1.name,person1.age)
person2 = info()
person2.update()
print(person2.name,person2.age)
person1.name = "suyash"
print(person1.name,person1.age)



#CONSTRUCTOR IN INHERITANCE
#EG-

class a:
    def __init__(self):
        print("in a init")

    def feacture1(self):
        print("feacture 1 is working")

    def feacture2(self):
        print("feacture 2 is working")
class b:
    def __init__(self):
        print("in b init")

    def feacture3(self):
        print("feacture 3 is working")

    def feacture4(self):
        print("feacture 4 is working")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("in c init")

    def feacture5(self):
        print("feacture 5 is working")

    def feacture6(self):
        print("feacture 6 is working")

a1 = c()
