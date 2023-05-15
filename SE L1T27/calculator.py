def history():
    # Use a while loop that will loop through asking the user for the file name until they enter the correct name.
    history_shown = False

    while history_shown == False:
        file_name = input('''\nWhat is the name of the file that stores your history? (Add .txt to the end)
(The file name is history.txt)
: ''')

        # Try to read through history.txt and print each line from that file.
        # Once done, set history_shown to true and break the while loop.
        try:
            with open(file_name, "r") as history:
                print("\nHISTORY")

                for calc in history:
                    print(calc + '\n')

                history_shown = True

    # If it runs into the FileNotFoundError, ask the user if they entered the correct file name.
    # If yes, show that there is no history and then set history_shown to True, breaking the while loop.
    # If anything but yes, run through the loop again.

        except FileNotFoundError:
            correct_name = input("\nDid you enter the correct file name and add .txt at the end? Yes/No\n").lower()
            if correct_name == "yes":
                print("\nNO HISTORY\n")
                history_shown = True


def calculator():
    # Create a while loop that loops until the user has entered two numbers.
    # If the user enters anything but a number (ValueError), get them to try again.
    numbers_found = False

    while numbers_found == False:
        try:
            user_num1 = float(input("\nPlease enter your first number: "))
            user_num2 = float(input("Please enter your second number: "))
            numbers_found = True

        except ValueError:
            print("\nOops! Something your entered was not a valid number! Please try again.\n")

    # Create a while loop that will run until the user chooses to no longer do calculations with their two chosen numbers.
    choose_another = "yes"

    while choose_another == "yes":
        # Give the user the option to choose between adding, subtracting, multiplication and dividing.
        oper = input('''\nWhat operation would you like to do on these two numbers?
        Plus: +
        Minus: -
        Times: *
        Divide: /
        Return to menu: -1
        : ''').lower()

        # If the user chooses to add, call the add function and then ask if the user would like to do another operation with these numbers.
        if (oper == "+") or (oper == "plus"):
            adding(user_num1, user_num2)

            choose_another = input("\nWould you like to do another operation with these numbers? Yes/No\n").lower()
        
        # IF the user chooses to subtract, call the subtracting function and then ask if the user would like to do another operation with these numbers.
        elif (oper == "-") or (oper == "minus"):
            subtracting(user_num1, user_num2)

            choose_another = input("\nWould you like to do another operation with these numbers? Yes/No\n").lower()

        # IF the user chooses to times, call the multiplying function and then ask if the user would like to do another operation with these numbers.
        elif (oper == "*") or (oper == "times"):
            multiplying(user_num1, user_num2)

            choose_another = input("\nWould you like to do another operation with these numbers? Yes/No\n").lower()

        # IF the user chooses to divide, call the dividing function and then ask if the user would like to do another operation with these numbers.
        elif (oper == "/") or (oper == "divide"):
            dividing(user_num1, user_num2)

            choose_another = input("\nWould you like to do another operation with these numbers? Yes/No\n").lower()

        # If the user chooses to go back, set choose_another to no and break the loop.
        elif oper == "-1":
            choose_another = "no"

        # If none of these options were chosen, get the user to try again.
        else:
            print("\nYou have not entered a valid operation.")

def adding(num1, num2):
    # Find the sum of num1 and num2, then print the result.
    # Append the eqaution to history.txt.
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
                    
    with open("history.txt", "a") as calc:
        calc.write(f"{num1} + {num2} = {result}\n")

def subtracting(num1, num2):
    # Create a while loop where the user can choose to subtract the numbers in a different order, or return to the main menu.
    option_picked = False
                    
    while option_picked == False:
        # Ask the user how they would like to subtract the numbers.
        which_way = input(f'''\nWhich order would you like the numbers to be subtracted in?
    Option 1: {num1} - {num2}
    Option 2: {num2} - {num1}
    Option 3: Return to main menu.
    : ''').lower()
                        
        # If the user chooses to do num1 - num2, find the result and then print the equation.
        # Append the equation to history.txt.
        if which_way == "option 1" or which_way == "1":
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}\n")

            with open("history.txt", "a") as calc:
                calc.write(f"{num1} - {num2} = {result}\n")

            # Ask the user if they would like to subtract num1 and num2 again.
            # If yes, go through the option_picked loop again.
            # If no, set option_picked to no and break the loop.
            again = input(f"Would you like to subtract {num1} and {num2} again? Yes/No\n").lower()

            if again == "no":
                option_picked = True

        # If the user chooses to do num2 - num1, find the result and then print the equation.
        # Append the equation to history.txt.
        elif which_way == "option 2" or which_way == "2":
            result = num2 - num1
            print(f"\n{num2} - {num1} = {result}\n")

            with open("history.txt", "a") as calc:
                calc.write(f"{num2} - {num1} = {result}\n")

            # Ask the user if they would like to subtract num1 and num2 again.
            # If yes, go through the option_picked loop again.
            # If no, set option_picked to True and break the loop.
            again = input(f"\nWould you like to subtract {num1} and {num2} again? Yes/No\n").lower()

            if again == "no":
                option_picked = True

        # If the user chooses to exit, set option_picked to True and break the loop.
        elif which_way == "option 3" or which_way == "3":
            option_picked = True

        # If none of these options were picked, tell the user to try again.
        else: 
            print("\nYou did not select a valid option, please type in option 1 or option 2.\n")

def multiplying(num1, num2):
    # Find the product of num1 and num2, then print the result.
    # Append the equation to history.txt.
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")

    with open("history.txt", "a") as calc:
        calc.write(f"{num1} * {num2} = {result}\n")

def dividing(num1, num2):
    # Create a while loop where the user can choose to divide the numbers in a different order, or return to the main menu.
    option_picked = False
                     
    while option_picked == False:
        # Ask the user how they would like to divide the numbers.               
        which_way = input(f'''\nWhich order would you like the numbers to be divided in?
    Option 1: {num1} / {num2}
    Option 2: {num2} / {num1}
    Option 3: Go back to main menu.
    : ''').lower()

        # If the user chooses to do num1 / num2, find the result and then print the equation.
        # Append the equation to history.txt.    
        if which_way == "option 1" or which_way == "1":
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}\n")

            with open("history.txt", "a") as calc:
                calc.write(f"{num1} / {num2} = {result}\n")

            # Ask the user if they would like to divide num1 and num2 again.
            # If yes, go through the option_picked loop again.
            # If no, set option_picked to no and break the loop.
            again = input(f"Would you like to divide {num1} and {num2} again? Yes/No\n").lower()

            if again == "no":
                option_picked = True

        # If the user chooses to do num2 / num1, find the result and then print the equation.
        # Append the equation to history.txt. 
        elif which_way == "option 2" or which_way == "2":
            result = num2 / num1
            print(f"\n{num2} / {num1} = {result}\n")

            with open("history.txt", "a") as calc:
                calc.write(f"{num2} / {num1} = {result}\n")

            # Ask the user if they would like to divide num1 and num2 again.
            # If yes, go through the option_picked loop again.
            # If no, set option_picked to no and break the loop.
            again = input(f"\nWould you like to divide {num1} and {num2} again? Yes/No\n").lower()

            if again == "no":
                option_picked = True

        # If the user chooses to exit, set option_picked to True and break the loop.
        elif which_way == "option 3" or which_way == "3":
            option_picked = True

        # If none of these options were picked, tell the user to try again.
        else: 
            print("\nYou did not select a valid option, please type in option 1 or option 2.\n")

# Run a while loop infinitely until the user says to exit the loop.
while True:
    # Give the user the option of viewing the calculator, viewing history, or exiting the loop/
    choice = input('''\nWhich would you like to view:
    Option 1: Calculator
    Option 2: History
    Option 3: Exit
    : ''').lower()

    # If the user chooses option 1, call the calculator function.
    if choice == "option 1" or choice == "1" or choice == "calculator":
        calculator()

    # If the user chooses option 2, call the history function.
    elif choice == "option 2" or choice == "2" or choice == "history":
        history()

    # If the user chooses option 3, close the program.
    elif choice == "option 3" or choice == "3" or choice == "exit":
        print("\nGoodbye!")
        exit()

    # If the user chooses none of these options, get them to try again.
    else:
        print("\nYou have not chosen a valid option.")