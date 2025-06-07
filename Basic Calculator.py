# Making a calculator

print("Choose your option :")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Power")
print("5.Division")
print("6.Mod")
print("________________________")

option =input(":")

match option:
    case"1":
        num1=int(input("enter your 1st number: "))
        num2=int(input("enter your 2nd number: "))
        sum=(num1+num2)
        print(sum)
    case"2":
        num1=int(input("enter your 1st number: "))
        num2=int(input("enter your 2nd number: "))
        subtraction=(num1-num2)
        print(subtraction)
    case"3":
        num1=int(input("enter your 1st number: "))
        num2=int(input("enter your 2nd number: "))
        multiplication=(num1*num2)
        print(multiplication)
    case"4":
        num1=int(input("enter your 1st number: "))
        num2=int(input("enter your 2nd number: "))
        power=(num1**num2)
        print(power)
    case"5":
        num1=int(input("enter your 1st number: "))
        num2=int(input("enter your 2nd number: "))
        division=(num1/num2)
        print(division)
    case"6":
        num1=int(input("enter your 1st number: "))
        num2=int(input("enter your 2nd number: "))
        mod=(num1%num2)
        print(mod)
    case _:
        print("Invalid option")


if num1%num2 !=0:
    remainder= num1%num2'''


