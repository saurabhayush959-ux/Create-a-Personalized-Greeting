
def basic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = None
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"
    
    return addition, subtraction, multiplication, division


def main():
   
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
      
        addition, subtraction, multiplication, division = basic_operations(num1, num2)
        
       
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
