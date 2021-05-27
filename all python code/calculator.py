
#basic calulator
1.num1 = input(int(("enter number 1:"))
num2 =input(int("enter number 2:"))
result = float(num1) + float(num2)
print(result)


#2.advance calculator
num1 = float(input("enter number 1:"))
operation = input("enter oprator:")
num2 = float(input("enter number 2:"))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
else:
    print("invalid operator")