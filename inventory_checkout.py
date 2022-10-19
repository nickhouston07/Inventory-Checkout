import pickle
import cart

INVENTORY_CUTOFF = 5

def main():
    # Set variable to false until the end of the
    # file is reached.
    end_of_file = False

    # Open the dict.dat file for reading.
    infile = open('dict.dat', 'rb')

    # Run until the end of the file saving the
    # data to a dictionary.
    while not end_of_file:
        try:
            inventory = pickle.load(infile)
        except EOFError:
            end_of_file = True

    # Close the file.
    infile.close()

    # Start the login screen.
    log_in(inventory)


def log_in(inventory):
    # Notify the user they can enter q to quit back to the log in
    # screen.
    print("Entering 'q' will quit back to the login screen.")
    print("Entering 'q' while at the login screen will end the program.")
    print('----------------------------------------------------------')
    
    # Ask the user if they are logging in as a customer or employee.
    print('Customer or Employee?')
    print("Enter 'c' for customer or 'e' for employee.")
    choice = input('Login: ')

    # Input validation loop to make sure the user enters a valid
    # option.
    while choice.lower() != 'c' and choice.lower() != 'e' and \
    choice.lower() != 'q':
        choice = input('Error. Re-enter c or e: ')

    # If 'c' start the customer function.
    if choice.lower() == 'c':
        print()
        print('Login successful.')
        print('-----------------')
        my_cart = cart.Cart()
        customer(inventory, my_cart)

    # If 'e' start verify the password and if correct start
    # the employee function.
    if choice.lower() == 'e':
        password = input('Password: ')
        while password != 'password':
            print('The password you entered is incorrect.')
            password = input('Enter the correct password: ')

        print()
        print('Login successful.')
        print('-----------------')
        employee(inventory)

    # If 'q' then open dict.dat for writing, dump the inventory
    # dictionary to the dict.dat file, close the file, and then
    # return to the main function ending the program.
    if choice.lower() == 'q':
        outfile = open('dict.dat', 'wb')
        pickle.dump(inventory, outfile)
        outfile.close()
        return
        

def customer(inventory, cart):
    print()

    # Present an options menu to the customer.
    print('---------------------------')
    print('1. Display entire inventory')
    print('2. Search for specific item')
    print('3. Add item to cart')
    print('4. Remove item from cart')
    print('5. Display items in cart')
    print('6. Check out')
    print("Enter 'q' to return to the log in screen.")

    # Get the customers choice.
    choice = input('Enter: ')
    print()

    # Validate customer's choice.
    while choice != '1' and choice != '2' and choice != '3' and choice != '4' \
    and choice != '5' and choice != '6' and choice.lower() != 'q':
        print('Error. Invalid entry.')
        choice = input('Enter 1 through 5 or q to quit.')

    # Pass inventory to the function that matches the customer's choice.
    if choice.lower() == 'q':
        log_in(inventory)
    elif choice == '1':
        display_inventory_cust(inventory, cart)
    elif choice == '2':
        search_item_cart(inventory, cart)
    elif choice == '3':
        add_item_cart(inventory, cart)
    elif choice == '4':
        remove_item_cart(inventory, cart)
    elif choice == '5':
        display_cart(inventory, cart)
    elif choice == '6':
        check_out(inventory, cart)

    
def display_inventory_cust(inventory, cart):
    # Create an empty list to hold the values matching the key
    list1 = []

    print('Here is the current inventory.')
    print('-----------------------------')

    # Run through inventory and display the key, price, and available
    # units.
    for key in inventory:
        list1 = inventory.get(key)
        print('Item: ', key)
        print('Price: $', list1[0], sep='')
        print('Units: ', list1[1])

    customer(inventory, cart)


def search_item_cart(inventory, cart):
    again = 'y'
    name = ''

    # Run the loop searching for items until they enter 'q' or dont enter 'y'
    # at the end.
    while again.lower() == 'y' and name != 'q':
        print('----------------------------')

        # Ask the customer for the name of the item they wish to find.
        name = input('Enter the item to search for: ')

        # If the item isn't in inventory give them the option to re-enter
        # the correct item or quit back to the customer options menu.
        while name != 'q' and name not in inventory:
            print('That item is does not exist.')
            name = input("Re-enter the item or 'q' to quit: ")

        # If they enter 'q' quit back to the customer screen.
        if name == 'q':
            customer(inventory, cart)
        else:
            # Display the item, its price, and the units available
            #del inventory[name]
            list1 = inventory.get(name)
            print('Item: ', name)
            print('Price: $', list1[0], sep='')
            print('Units: ', list1[1])
            print()
            print('Would you like to add this item to the cart?')
            choice = input("'y' for yes or 'n' for no: ")
            while choice.lower() != 'y' and choice.lower() != 'n':
                print("Error. Must enter 'y' or 'n'.")
                choice = input()

            print()
            # If they answer yes ask how many they would like and add
            # the item to the cart object using the purchase_item method.
            if choice.lower() == 'y':
                units = int(input('Number of this item to add to cart: '))
                # This loop prevents the user from entering negative for
                # the amount or an amount higher than what is available in
                # inventory.
                while units < 1 or units > list1[1]:
                    print('Error. Amount cannot be less than 1 or greater')
                    print('than the total units available.')
                    units = int(input('Re-enter the amount: '))

                # Add the item to the cart object.
                cart.purchase_item(name, units, list1[0])
                print('Item added to cart.')

            # Ask the customer if they would like to search for another item.
            print('Would you like to search for another item?')
            again = input("enter 'y' or 'n' if not: ")
            
    customer(inventory, cart)    
    


def add_item_cart(inventory, cart):
    again = 'y'
    name = ''

    # Run the loop adding items until they enter 'q' or dont enter 'y'
    # at the end.
    while again.lower() == 'y' and name != 'q':
        print('----------------------------')

        # Ask the customer for the name of the item they wish to add.
        name = input('Enter the item to add to cart: ')

        # If the item isn't in inventory give them the option to re-enter
        # the correct item or quit back to the customer options menu.
        while name != 'q' and name not in inventory:
            print('That item is does not exist.')
            name = input("Re-enter the item or 'q' to quit: ")

        # If they enter 'q' quit back to the customer screen.
        if name == 'q':
            customer(inventory, cart)
        else:
            # Create a list to hold the units and price
            list1 = inventory.get(name)
            print()
            # Tell the customer how many of that itme are available
            print('There are', list1[1], 'of that item available.')

            # Ask the customer how many of the item they want to add
            # to their cart.
            units = int(input('Number of this item to add to cart: '))
            
            # This loop prevents the user from entering negative for
            # the amount or an amount higher than what is available in
            # inventory.
            while units < 1 or units > list1[1]:
                print('Error. Amount cannot be less than 1 or greater')
                print('than the total units available.')
                units = int(input('Re-enter the amount: '))

            # Add the item to the cart object.
            cart.purchase_item(name, units, list1[0])
            print('Item added to cart.')

            # Ask the customer if they would like to search for another item.
            print('Would you like to search for another item?')
            again = input("enter 'y' or 'n' if not: ")
            
    customer(inventory, cart)


def remove_item_cart(inventory, cart):
    again = 'y'
    name = ''

    # Run the loop removing items until they enter 'q' or dont enter 'y'
    # at the end.
    while again.lower() == 'y' and name != 'q':
        print('----------------------------')

        # Ask the customer for the name of the item they wish to remove.
        name = input('Enter the item to remove from the cart: ')

        # If the item isn't in inventory give them the option to re-enter
        # the correct item or quit back to the customer options menu.
        while name != 'q' and name not in cart.show_items():
            print('That item is does not exist in the cart.')
            name = input("Re-enter the item or 'q' to quit: ")

        # If they enter 'q' quit back to the customer screen.
        if name == 'q':
            customer(inventory, cart)
        else:
            # Remove the item from the cart
            list1 = cart.show_items()[name]
            cost = list1[0] * list1[1]
            cart.remove_item(name, cost)
            print('Item removed from cart.')

            # Ask the customer if they would like to remove another item.
            print('Would you like to remove another item?')
            again = input("enter 'y' or 'n' if not: ")
            
    customer(inventory, cart)
    

    
def display_cart(inventory, cart):
    print('----------------------------')

    # Display all the items currently in the cart and the
    # current cart total.
    print(cart.show_items())
    print('Cart total: $', cart.get_total(), sep='')

    customer(inventory, cart)


def check_out(inventory, cart):
    print('----------------------------')

    # Display the items in the cart and the total
    print(cart.show_items())
    print('The total is: $', cart.get_total(), sep='')

    # This for loop runs through all the keys in the cart object
    # and subtracts the units of each key from the units of the
    # matching key in the inventory dictionary. 
    for key in cart.show_items():
        cart_list = cart.show_items()[key]
        inv_list = inventory.get(key)
        new_units = inv_list[1] - cart_list[1]
        inventory[key] = [inv_list[0], new_units]

    # Clears all items from the cart object and sets the
    # total back to 0
    cart.clear()

    customer(inventory, cart)
        


def employee(inventory):
    print()

    # Empty list to hold the list items associated with each key
    # in the inventory dictionary.
    list1 = []

    # For each key in the inventory dictionary check how many units
    # are left and if less than 6 are left notify the employee.
    for key in inventory:
        list1 = inventory.get(key)
        if list1[1] <= INVENTORY_CUTOFF:
            print('There are only', list1[1], 'units of ', key, ' left.')

    # Present an options menu to the employee.
    print('---------------------------')
    print('1. Display entire inventory')
    print('2. Add a new item to inventory')
    print('3. Remove an item from inventory')
    print('4. Make changes to an existing item in inventory')
    print("Enter 'q' to return to the log in screen.")
        
    # Get the employees menu choice.
    choice = input('Enter: ')
    print()
    
    # Validate the employees entry.
    while choice != '1' and choice != '2' and choice != '3' and choice != '4' \
    and choice.lower() != 'q':
        print('Error. Invalid entry.')
        choice = input('Enter 1 through 4 or q to quit.')
    
    # Pass inventory to the function that matches the employees choice.
    if choice.lower() == 'q':
        log_in(inventory)
    elif choice == '1':
        display_inventory_emp(inventory)
    elif choice == '2':
        add_item(inventory)
    elif choice == '3':
        remove_item(inventory)
    elif choice == '4':
        change_item(inventory)


def display_inventory_emp(inventory):
    # Create an empty list to hold the values matching the key
    list1 = []

    print('Here is the current inventory.')
    print('-----------------------------')

    # Run through inventory and display the key, price, and available
    # units.
    for key in inventory:
        list1 = inventory.get(key)
        print('Item: ', key)
        print('Price: $', list1[0], sep='')
        print('Units: ', list1[1])

    employee(inventory)
    

def add_item(inventory):
    # Set again to 'y' and name to an empty string
    again = 'y'
    name = ''

    # This first while loop runs as long as the employee enters 'y'
    # at the end of each loop.
    while again.lower() == 'y' and name != 'q':
        print('----------------------------')
        name = input('Enter the item you would like to add: ')
        # This while loop runs until the enter an item that doesn't
        # already exist in inventory or until they enter 'q' to quit.
        while name != 'q' and name in inventory:
            print('That item already exists. Enter another item')
            name = input(" or enter 'q' to quit: ")

        # If they did not enter 'q' to quit then ask for the price
        # and units of the item, then add it to inventory. Then ask
        # if they have more items to enter.
        if name != 'q':
            price = float(input('Enter the price of the item: '))
            units = int(input('Enter the amount of units of this item: '))
            inventory[name] = [price, units]
            print('Item added. If you have more items to add')
            again = input("enter 'y' or 'n' if not: ")

    employee(inventory)



def remove_item(inventory):
    again = 'y'
    name = ''

    # Run the loop removing items until they enter 'q' or dont enter 'y'
    # at the end.
    while again.lower() == 'y' and name != 'q':
        print('----------------------------')

        # Ask the employee for the name of the item they wish to remove.
        name = input('Enter the item to remove: ')

        # If the item isn't in inventory give them the option to re-enter
        # the correct item or quit back to the employee options menu.
        while name != 'q' and name not in inventory:
            print('That item is does not exist.')
            name = input("Re-enter the item or 'q' to quit: ")

        # If they enter 'q' quit back to the employee screen.
        if name == 'q':
            employee(inventory)
        else:
            # Delete the item from inventory
            del inventory[name]
            print('Item removed. If you have more items to remove')
            again = input("enter 'y' or 'n' if not: ")
            
    employee(inventory)        


def change_item(inventory):
    # Set again to 'y' and name to an empty string
    again = 'y'
    name = ''

    # Run the loop changing items until they enter 'q' or dont enter 'y'
    # at the end.
    while again.lower() == 'y' and name != 'q':
        print('----------------------------')
        # Ask the employee for the name of the item they would like to change.
        name = input('Enter the item you would like to change: ')

        # If the item isn't in inventory give them the option to re-enter
        # the correct item or quit back to the employee options menu.
        while name != 'q' and name not in inventory:
            print("That item doens't exist in inventory.")
            name = input("Re-enter the item or 'q' to quit: ")

        # If they enter 'q' quit back to the employee screen.
        if name == 'q':
            employee(inventory)
        else:
            # Get the new price and units and change them
            price = float(input('Enter the new price: '))
            units = int(input('Enter the new units: '))
            inventory[name] = [price, units]
            print('Item changed. If you have more items to change')
            again = input("enter 'y' or 'n' if not: ")

    employee(inventory)                


main()

