#EXCEPTION HANDLING-

'''TYPES OF ERROR-

1.complie time error-
                    eg- mmissing(:),wrong sprlling

2.logical error- in this your code gets complied and
                   shows the output but wrong output. eg- wrong op

3.runtime error- in this there is no runtime error or
                 logical erro but in case user gave wrong output it
                 ives wrong output a well. eg-wrong input from user side

                                   '''
#EG-

a=5
b=1
try:
    print("resouce open")
    c=(a/b)
    print(c)
    m = int(input("enter a number"))
    print(m)
except ZeroDivisionError  as e:
    print("you cant dive a number b zero",e)

except ValueError  as e:
    print("invalid in put",e)
except Exception as e:
    print('someting went wrong')
finally:
    print("resouse closed")
