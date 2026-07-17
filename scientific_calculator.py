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

#trigonometric functions
def sine(a,unit):
    if unit == "degrees":
        return math.sin(math.radians(a))
    elif unit == "radians":
        return math.sin(a)
    else:
        return "Invalid unit. Please enter degrees or radians."
def cosine(a,unit):
    if unit == "degrees":
        return math.cos(math.radians(a))
    elif unit == "radians":
        return math.cos(a)  
    else:
        return "Invalid unit. Please enter degrees or radians."
def tangent(a,unit):
    if unit == "degrees":
        return math.tan(math.radians(a))
    elif unit == "radians":
        return math.tan(a)
    else:
        return "Invalid unit. Please enter degrees or radians."

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
    print("\n-----------------------------")
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
      elif opt == "2":
        result = subtract(a, b)
        history.append(f"{a} - {b} = {result}")
      elif opt == "3":
        result = multiply(a, b)
        history.append(f"{a} * {b} = {result}")
      elif opt == "4":        
        result = divide(a, b)
        history.append(f"{a} / {b} = {result}")
      elif opt == "5":
        result = power(a, b)
        history.append(f"{a} ^ {b} = {result}")
        
      print("Result:", result)
      input("\nPress Enter to return to the menu...")
    

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
      elif opt == "7":
        while True:
            unit = input ("Enter unit (degrees/radians): ").lower() 
            if unit == "degrees" or unit == "radians":
                break
            else:
                print("Invalid unit. Please enter 'degrees' or 'radians'.")
        result = sine(num, unit)
        history.append(f"sin({num}) = {result}")
      elif opt == "8":
        while True:
            unit = input ("Enter unit (degrees/radians): ").lower() 
            if unit == "degrees" or unit == "radians":
                break
            else:
                print("Invalid unit. Please enter 'degrees' or 'radians'.")
        result = cosine(num, unit)
        history.append(f"cos({num}) = {result}")
      elif opt == "9":
        while True:
            unit = input ("Enter unit (degrees/radians): ").lower() 
            if unit == "degrees" or unit == "radians":
                break
            else:
                print("Invalid unit. Please enter 'degrees' or 'radians'.")
        result = tangent(num, unit)
        history.append(f"tan({num}) = {result}")
      elif opt == "10":
        result = logarithm(num)
        history.append(f"log({num}) = {result}")
      elif opt == "11":
        result = factorial(num)
        history.append(f"{num}! = {result}")
       
      print("Result:", result)
      input("\nPress Enter to return to the menu...")
        
    elif opt == "12":
     if len (history) == 0:
         print("No history available.")
         input("\nPress Enter to return to the menu...")
     else:
         print("Calculation History:")
         for item in history:
             print(item)
         input("\nPress Enter to return to the menu...")
             
    elif opt == "13":
     history.clear()
     print("History cleared.")
     input("\nPress Enter to return to the menu...")
       
    else:
     print("Invalid choice. Please select a valid option.")
     
#main program
while True: #keeps running till user exits
    menu()
    opt = input("Select operation (1-13) or type 'end' to exit: ")

    if opt.lower() == "end":
        print("Calculator shutting down.")
        break
    
    calculate(opt)
    
