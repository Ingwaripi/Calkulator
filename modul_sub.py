def  sub_result():
        num1 = int(input("Enter first number: "))
        num2 = int(input('Enter second number: '))
        su_re = num1 - num2
        print(f"{num1} - {num2} = {su_re}")

def sub_result_com():
        num1 = complex(input("Enter first number: "))
        num2 = complex(input("Enter the imaginatyn part: "))
        num3 = complex(input("Enter second number: "))
        num4 = complex(input("Enter the imaginatyn part: "))
        com1 = complex(num1, num2)
        com2 = complex(num3,num4)
        result = com1 - com2
        print(f"Result of the sum of complex numbers = {result}") 