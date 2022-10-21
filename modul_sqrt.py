def  sqrt_result():
        num1 = int(input("Enter number: "))
        
        su_re = num1 ** 0.5
        print(f"SQRT {num1} = {su_re}")

def sqrt_result_com():
        num1 = complex(input("Enter first number: "))
        num2 = complex(input("Enter the imaginatyn part: "))
        num3 = complex(input("Enter second number: "))
        num4 = complex(input("Enter the imaginatyn part: "))
        com1 = complex(num1, num2)
        com2 = complex(num3, num4)
        result = (com1 ** 2 + com2 ** 2) ** 0.5
        print(f"Result of the sum of complex numbers = {result}") 