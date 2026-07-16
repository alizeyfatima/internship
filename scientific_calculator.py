import math #for scientific calculations
history = [] #empty list to store history

#basic operations
def add(a,b):
    return a + b
def subtract (a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error! Cannot divide by zero."
    
#scientific operations
def power (a,b):
    return math.pow(a,b)
def square_root(a):
    if a < 0:
        return "Cannot calculate square root of negative number"
    return math.sqrt(a)

#trignometric functions
def sine(a):
    return math.sin(math.radians(a))
def cosine(a):
    return math.cos(math.radians(a))
def tangent(a):
    return math.tan(math.radians(a))

#log and factorial
def logarithm(a):
    if a <= 0:
        return "Logarithm only works for positive numbers."
    return math.log(a)
def factorial(a):
    if a < 0 or a != int(a):
        return "Factorial only works for positive whole numbers."
    return math.factorial(int(a))

def menu():
    print("-----------------------------")
    print ("Scientific Calculator:")
    print("-----------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")
    print ("12. View History")
    print ("13. Clear History")
    print("0. Exit")
    
def calculate(opt):
    if opt in ["1", "2", "3", "4", "5"]:
      while True:
        try:
            a = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
      while True:
        try:
            b = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

      if opt == "1":
        result = add(a, b)
        history.append(f"{a} + {b} = {result}")
        print("Result:", result)
      elif opt == "2":
        result = subtract(a, b)
        history.append(f"{a} - {b} = {result}")
        print("Result:", result)
      elif opt == "3":
        result = multiply(a, b)
        history.append(f"{a} * {b} = {result}")
        print("Result:", result)
      elif opt == "4":
        result = divide(a, b)
        history.append(f"{a} / {b} = {result}")
        print("Result:", result)
      elif opt == "5":
        result = power(a, b)
        history.append(f"{a} ^ {b} = {result}")
        print("Result:", result)

    elif opt in ["6", "7", "8", "9", "10", "11"]:
      while True:
        try:
            num = float(input("Enter number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

      if opt == "6":
        result = square_root(num)
        history.append(f"√{num} = {result}")
        print("Result:", result)
      elif opt == "7":
        result = sine(num)
        history.append(f"sin({num}) = {result}")
        print("Result:", result)
      elif opt == "8":
        result = cosine(num)
        history.append(f"cos({num}) = {result}")
        print("Result:", result)
      elif opt == "9":
        result = tangent(num)
        history.append(f"tan({num}) = {result}")
        print("Result:", result)
      elif opt == "10":
        result = logarithm(num)
        history.append(f"log({num}) = {result}")
        print("Result:", result)
      elif opt == "11":
        result = factorial(num)
        history.append(f"{num}! = {result}")
        print("Result:", result)
        
    elif opt == "12":
     if len (history) == 0:
         print("No history available.")
     else:
         print("Calculation History:")
         for item in history:
             print(item)
             
    elif opt == "13":
     history.clear()
     print("History cleared.")
       
    else:
     print("Invalid choice. Please select a valid option.")
     
#main program
while True: #keeps running till user exits
    menu()
    opt = input("Select operation (0-13): ")

    if opt == "0":
        print("Calculator closed.")
        break
    
    calculate(opt)
    
