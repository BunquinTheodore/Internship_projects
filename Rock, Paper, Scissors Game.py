import random 

def main(): 
    while (True):
        print ("\nWelcome to Rock, Paper, Scissor Game!\n")
        try: 
            print ("1. Start")
            print ("2. Exit")
            choice = int(input ("Enter choice: "))
            if choice == 1:
                menu()
            elif choice == 2:
                print ("Exiting Program...")
                break
            else: 
                print ("Invalid Input, try again...")
        except ValueError as e: 
            print (f"Error: {e}")
        
def menu(): 
    while (True):
        print ("\nGame started, pick your weapon!")
        print ("1. Rock")
        print ("2. Paper")
        print ("3. Scissor")
        print ("4. Exit")
        try: 
            move = int(input("Enter choice: "))
            computer_move = computer_choice()
            print (f"Computer move: {computer_move}")
            
            if move == 4: 
                break
            elif move == computer_move: 
                print ("It's a tie!")
            elif (
                (move ==  1  and  computer_move == "Scissor") or
                (move == 2 and computer_move == "Rock") or
                (move == 3 and computer_move == "Paper")
            ):
                print ("You win!")
            else:
                print ("Computer wins, you lose!")
            
                
        except ValueError as e: 
            print (f"Error: {e}")
    
def computer_choice():
    options = ["Rock", "Paper", "Scissor"]
    return random.choice(options)

if __name__ == "__main__": 
    main()