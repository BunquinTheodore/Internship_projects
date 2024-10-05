import random

def guess_number():
    random_num = random.randint(0,100)
    while (True):
        try:
            guess_num = int(input("Guess the random number(1-100): "))
            if (guess_num < random_num):
                print ("The random number is greater than your guessed number\n Try again")
            elif (guess_num >random_num):
                print ("The random number is less than your guessed number\n Try again")
            else:
                print ("You guessed the random number!")
                break
        except ValueError as e:
            print ("Invalid Input, try again...")
        
def menu ():
    while True:
        print ("Welcome to Number Guessing Game!")
        print ("1. Start")
        print ("2. Exit")
        
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                guess_number()
            elif choice == 2: 
                print ("Exiting Program.....")
                break
            else:
                print ("Invalid Input")
        except ValueError as error:
            print (f"Value Error: {error}")

def main():
    menu()
    
if __name__ == "__main__":
    main()