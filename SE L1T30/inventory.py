from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    '''
    In this function, you must initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
    '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    '''
    Add the code to return the cost of the shoe in this method.
    '''
    def get_cost(self):
        product_cost = float(self.cost)
        return(product_cost)

    '''
    Add the code to return the quantity of the shoes.
    '''
    def get_quantity(self):
        product_quantity = int(self.quantity)
        return(product_quantity)

    '''
    Add a code to returns a string representation of a class.
    '''
    def __str__(self):
        return(f'''\nProduct: {self.product}.
Country: {self.country}.
Code: {self.code}.
Cost: {self.cost}.
Quantity: {self.quantity}.''')


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
The objectless_shoe_list will be used to tabulate the list.
'''
shoe_list = []
objectless_shoe_list = []

# On start of the program, already write the first list of shoes, in case the user forgets to run the "new" option.
# Use error handling in case there is no inventory.txt file and if there isn't, ask the user to create on first.
try:
    with open("inventory.txt", "r") as file:
        inventory = file.readlines()

        for shoe in inventory[1::]:
            temp = shoe.strip().split(",")
            shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

            objectless_shoe_list.append(temp)

        print("\nThe file has been read, you may now proceed with the other functions.")

except FileNotFoundError:
    print("\nThere does not seem to be an inventory.txt file.\n Please create this file and then try again.")

#==========Functions outside the class==============
'''
This function will open the file inventory.txt and read the data from this file, 
then create a shoes object with this data and append this object into the shoes list. 
One line in this file represents data to create one object of shoes.
You must use the try-except in this function for error handling. 
Remember to skip the first line using your code.
'''
def read_shoes_data():
    '''Create an empty shoe list which will store all the shoe objects.
    Create an empty objectless shoe list which will store just the information on the shoe.
    (the objectless shoe list will be used with the tabulate function later on)'''
    shoe_list = []
    objectless_shoe_list = []
    
    # Try to open the inventory.txt file. 
    # If there is none like that, tell the user to first create such a file.
    try:
        '''Go through each line of the file, strip and split it, then append the line to both shoe_list and objectless_shoe_list.
        Create a Shoe object in the shoe_list.
        Skip the first line of the file using [1::]'''

        with open("inventory.txt", "r") as file:
            inventory = file.readlines()

            for shoe in inventory[1::]:
                temp = shoe.strip().split(",")
                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
                objectless_shoe_list.append(temp)

            print("\nThe file has been read, you may now proceed with the other functions.")

    except FileNotFoundError:
        print("\nThere does not seem to be an inventory.txt file.\n Please create this file and then try again.")

'''
This function will allow a user to capture data about a shoe 
and use this data to create a shoe object
and append this object inside the shoe list.
'''
def capture_shoes():
    # Ask the user for the country, code and product information.
    country = input("\nWhat country is the shoe from?\n")
    code = input("\nWhat is the shoe's code?\n")
    product = input("\nWhat shoe is it?\n")

    # Use both a while loop and try and except ValueError for the cost and quantity of shoes.
    # Keep asking the user for cost and quantity until both are numbers.
    numbers_put = False
    while numbers_put == False:
        try:    
            cost = int(input("\nHow much is the shoe? (Only input number, do not include the currency symbol.)\n"))
            quantity = int(input("\nHow many of this shoe is in stock?\n"))

            numbers_put = True

        except ValueError:
            print("\nOops! One of your inputs was not a valid number! Please try again.")


    # Append this shoe to both the shoe_list and objectless_shoe_list.

    shoe_list.append(Shoe(country, code, product, cost, quantity))
    objectless_shoe_list.append([f"{country}",f"{code}",f"{product}",f"{cost}",f"{quantity}"])

    # Add this shoe to the inventory file.
    with open("inventory.txt", "a") as inventory:
        inventory.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("\nThank you, this shoe has been added.")

'''
This function will iterate over the shoes list 
and print the details of the shoes returned from the __str__ function. 
Optional: you can organise your data in a table format by using Python’s tabulate module.
'''
def view_all():
    # Use the tabulate function to create a table of all the products.
    # Use "Product", "Country", "Code", "Cost", "Quantity" as headers.
    print(tabulate(objectless_shoe_list, headers = ["Product", "Country", "Code", "Cost", "Quantity"], tablefmt = "fancy_grid"))

'''
This function will find the shoe object with the lowest quantity,
which is the shoes that need to be re-stocked. 
Ask the user if they want to add this quantity of shoes and then update it.
This quantity should be updated on the file for this shoe.
'''
def re_stock():
    # Create an empty list to store all the quanties.
    quantity_list = []

    # Go through each object and append their quantity to the quantity list.
    for ind in range(len(shoe_list)):
        quantity_list.append(shoe_list[ind].get_quantity())

    # Find the index of the smallest value.
    # From that index, search the shoe_list for the shoe with that quantity.
    least_shoe_index = quantity_list.index(min(quantity_list))
    least_shoe = shoe_list[least_shoe_index]

    # Print the shoe information and then ask if the user would like to update the quanityt.
    print(f"\nThe shoe with the least quantity is code {least_shoe.code} with {least_shoe.quantity} available.")

    qty_increase = input("\nWould you like to update this quantity? (Yes/No)\n").lower()

    # If yes, use a while loop and try and except ValueError to ask the user to enter the new number until they enter an integer.
    if qty_increase == "yes":
        number_put = False
        
        while number_put == False:
            try:
                least_shoe.quantity = int(input("\nHow many of this shoe is now available?\n"))

                # Once an integer has been entered, update the inventory with that new quantity.
                with open("inventory.txt", "w") as inventory:
                    inventory.write("Country,Code,Product,Cost,Quantity")

                    for shoe in shoe_list:
                        inventory.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

                print("\nInventory updated.")

                # Exit the loop.
                number_put = True

            except ValueError:
                print("\nOops! Your input was not a valid number! Please try again.")

    # If anything but yes is entered, don't update the quantity and go back.
    else:
        print(f"\nThank you, code {least_shoe.code} has been left as is.")

'''
This function will search for a shoe from the list using the shoe code 
and return this object so that it will be printed.
'''
def search_shoe():
    # Create a boolean that will be used for a while loop.
    code_entered = False

    # Create an empty code list that will store all the codes of each shoe.
    code_list = []

    # Go through the shoe list and append each shoe's code to the code list.
    for shoe in shoe_list:
        code_list.append(shoe.code)

    # While the user hasn't entered a code that is in code list, keep asking for a code.
    while code_entered == False:    
        shoe_code = input("\nWhat is the code for the shoe you are searching for?\n")

        # Once a code that is in code_list has been entered, go through the shoe list to find that code.
        if shoe_code in code_list:
            for shoe in shoe_list:
                if shoe.code == shoe_code:
                    # Once the code from the shoe list corresponds with the user's code, print that shoe.
                    # Break the for loop.
                    print(shoe)

                    break

            # Set the code entered variable to true to break the while loop.
            code_entered = True

        else:
            print("\nYou have not entered a valid code. Please try again.")

'''
This function will calculate the total value for each item.
Please keep the formula for value in mind: value = cost * quantity.
Print this information on the console for all the shoes.
'''
def value_per_item():
    # Create an empty list to add the codes and total values to.
    code_price_list = []

    '''Go through the shoe list and get the quantity and cost of each object
    Get the total value then append this and the code to code_price_list.
    Tabulate this list with the headers Code and Total Value'''
    for shoe in shoe_list:
        qty = shoe.get_quantity()
        price = shoe.get_cost()

        # Multiple the quantity and cost then print this total.
        total_val = qty * price

        code_price_list.append([f"{shoe.code}",f"{total_val}"])

    print(tabulate(code_price_list, headers = ["Code", "Total Value"], tablefmt = "fancy_grid"))

'''
Write code to determine the product with the highest quantity 
and print this shoe as being for sale.
'''
def highest_qty():
    # Create an empty list to store all the quanties.
    quantity_list = []

    # Go through each object and append their quantity to the quantity list.
    for ind in range(len(shoe_list)):
        quantity_list.append(shoe_list[ind].get_quantity())

    # Find the index of the highest value.
    # From that index, search the shoe_list for the shoe with that quantity.
    most_shoe_index = quantity_list.index(max(quantity_list))
    most_shoe = shoe_list[most_shoe_index]
   
    # Print the shoe information and then say that it is on sale.
    print(f"\nThe shoe with the largest quanity is code {most_shoe.code} with {most_shoe.quantity} available.")

    print(f"Item code {most_shoe.code} is now on sale")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    menu = input('''\nSelect one of the following Options below:
    data - Create a new list of data
    new - Add a new shoe
    va - View all shoes
    re - Restock on the shoe with the least quantity
    find - Search for a shoe
    val - See the values of each item
    most - See the item with the highest quantity
    quit - Exit
: ''').lower()
    
    # If menu = data, call the read_shoes_data function.
    if menu == "data":
        read_shoes_data()

    # If menu = new, call the capture_shoes function.
    elif menu == "new":
        capture_shoes()

    # If menu = va, call the view_all function.
    elif menu == "va":
        view_all()

    # If menu = re, call the re_stock() function.
    elif menu == "re":
        re_stock()

    # If menu = sear, call the search_shoe function.
    elif menu == "find":
        search_shoe()

    # If menu = val, call the value_per_item function.
    elif menu == "val":
        value_per_item()

    # If menu = highest, call the highest_qty function.
    elif menu == "most":
        highest_qty()

    # If menu = quit, print goodbye and quit the proram.
    elif menu == "quit":
        print("\nGoodbye!")

        break

    # If none of these are entered, tell the user to try again.
    else:
        print("\nYou have entered an invalid option, please try again.\n")