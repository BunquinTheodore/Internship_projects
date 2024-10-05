'''
 CALCULATOR
 A basic calculator that can perform basic arithmetic operations such as addition, 
 subtraction, multiplication, and division
'''

class Operations:
    @staticmethod
    def addition(x, y):
        return x + y
    
    @staticmethod
    def subtraction(x, y):
        return x - y
    
    @staticmethod
    def multiplication(x, y):
        return x * y
    
    @staticmethod
    def division(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nWelcome to Simple Calculator\n")
        
        num1 = get_number_input("Enter 1st number: ")
        num2 = get_number_input("Enter 2nd number: ")
        
        print("\nChoose Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        try:
            choice = int(input("Enter choice: "))
            
            if choice == 5:
                print("Exiting Program...")
                break
            
            if choice < 1 or choice > 4:
                raise ValueError("Invalid choice")
            
            operations = [
                Operations.addition,
                Operations.subtraction,
                Operations.multiplication,
                Operations.division
            ]
            
            result = operations[choice - 1](num1, num2)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()