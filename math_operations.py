def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
     return a / b
    else:   
     return "error: division by zero"
    
while True:
    print("simple calculator")   
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choice =input("enter your choice(1-4):")

    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number"))

    if choice =='1':
      result = add(num1, num2)
      print(f"the result of addition is:{result}")
    elif choice == '2':
     result = subtract(num1, num2)
     print(f"the result of subtraction is:{result}")
    elif choice == '3':
      result = multiply(num1, num2)
      print(f"the result of multiplication is:{multiply}")
    elif choice == '4':
      result = divide(num1, num2)
      print(f"the result of division is:{result}")
    else:
      print(f"invalid choice. please select a valid option.")