# if Statment

male = True
is_tall = False
if male and is_tall:
    print("you are male tall  both")
elif male and not (is_tall):
    print("you are male but not tall")
elif not (male) and is_tall:
    print("you are not male but tall")
else:
    print("you are not male not tall")


#ifcamarison
def max_num(num1,num2,num3):
    if num1 >= num2 and >= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3
print(max_num(45,48,12))
