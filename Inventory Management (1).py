#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
product_lines = {}


# In[5]:


def get_current_timestamp():
    return datetime.now().isoformat()


# In[9]:


def confirm():
    while True: 
        confirm = input("Is information entered above correct? Enter 'yes' or 'no'.")
        confirm_clean = confirm.strip().lower() # Cleans input

        # sends a true or false to whatever part of code is being ran to confirm or reject inputted information 
        if confirm_clean == "yes":
            return True
        if confirm_clean == "no": 
            return False
        else: 
            print("Please enter a 'yes' or a 'no'.")   

def cont_add():
    while True:
        add_more = input("Do you wish to add more? Enter 'yes' or 'no'.")
        add_more_clean = add_more.strip().lower() # Cleans input

        # Sends a true or false to whatever part of code is being ran 
        if add_more_clean == "yes":
            return True
        if add_more_clean == "no":
            return False
        else: 
            print("Please enter a 'yes' or a 'no'.")
        


# In[13]:


def add_product_line():

    while True:
        # Input to enter new product line
        new_product_line = input("What is your new product line? Or type main menu to return to the main menu.")
        new_product_line_clean = new_product_line.strip().lower() # cleans product line for consistent formatting

        # Returns user to main menu
        if new_product_line_clean == "main menu":
            return

        # If input is already in the product line list, tells user. Lets user input a different product line.
        if new_product_line_clean in product_lines:
            print("That product line already exists.")
            continue # lets user retry

        # Print the entered inputs
        print(f"The new product line you entered was {new_product_line_clean}. Is this correct?")

        # Double checks product line was entered correctly
        if confirm() == True:
            
            # Amends the product line to product line dictionary
            product_lines[new_product_line_clean] = {}
            print(f"'{new_product_line_clean}' has been added.")
            
            # Asks user if they want to input more
            if not cont_add():
                return
            else: 
                continue 

        else:
            print("Please enter information again.")
            continue


def remove_product_line():

    while True:
        # Asks user to enter product line they wish to remove and cleans it
        removed_product_line = input("Which product line would you like to remove? Or type main menu to return to the main menu")
        removed_product_line_clean = removed_product_line.strip().lower()

        # Returns user to main menu
        if removed_product_line_clean == "main menu":
            return

        # If product line is not in product lines dictionary, tells user that product line doesn't exist and to try again
        elif removed_product_line_clean not in product_lines:
            print("Product line doesn't exist. Please try again.")
            continue

        # Prints the entered input
        print(f"The product line you wish to remove is {removed_product_line_clean}.")

        # Double checks product line was entered correctly
        if confirm() == True:

            # If yes, removes product line from product line dictionary and tells user it has been deleted 
            del product_lines[removed_product_line_clean]
            print(f"'{removed_product_line_clean}' has been successfully removed.")

            # Asks user if they want to input more
            if not cont_add():
                return
            else: 
                continue 

        else:
            print("Please enter information again.")
            continue

def edit_product_line():
    while True:

        # Asks user for input and cleans it for consistency
        change_choice = input("Please enter the product line you wish to edit. Or enter main menu to return to main menu.")
        change_choice_clean = change_choice.strip().lower()

        # Returns user to main menu
        if change_choice_clean == "main menu":
            return

        # Asks user for what they wish to change product line to 
        elif change_choice_clean in product_lines:
            changed_product_line = input(f"What do you wish to change {change_choice_clean} to. Or type back to return.")
            changed_product_line_clean = changed_product_line.strip().lower()

            # If product line is already what was entered, tells them, and sends them back to top of edit_product_line
            if changed_product_line_clean == change_choice_clean:
                print("Product line is already that value. Please try again.")
                continue

            # Returns user to edit product line
            if changed_product_line_clean == "back":
                continue

            # If the changes to the product line are different than the previously entered product line, ask for confirmation on changes
            elif changed_product_line_clean != change_choice_clean:
                if not confirm():
                    continue # If the user says it is wrong, don't make changes, go back to top of defintion

                # Makes changes to the product line
                product_lines[changed_product_line_clean] = product_lines.pop(change_choice_clean)
                print(f"Product line has been successfully changed to '{changed_product_line_clean}'.")

                # Asks user if they want to make more changes
                more_changes = input("Do you want to make more changes? Enter 'yes' or 'no'.")
                more_changes_clean = more_changes.strip().lower() # cleans input
                if more_changes_clean == "yes":
                    continue # Go back to top of definition to allow more changes
                else: 
                    return # Stop the code

        # Raises error if product line doesn't exist and sends them to enter a product line to edit
        else:
            print("Product line not found. Please try again.")
            continue
               


# In[14]:


def add_product(): 

    # Asks users to choose a product line to add to
    while True:
        try: 
            print("Please select which product line you would like to add a product to.")
            product_line_list = list(product_lines.keys())

            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")
                
            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index - 1]
            
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue # Takes user back to start of loop
            
        # Asks user to confirm choice 
        print(f"Is {selected_product_line} the correct product line?")
        if confirm() == True:
            break
        # Loops back to try again
        else:
            continue
            
    # Asks user to enter product name 
    while True: 
        product_to_add = input(f"Please input the product you wish to add to {selected_product_line}.")
        product_to_add_clean = product_to_add.strip().lower()

        # Asks user to confirm input
        print(f"Is {product_to_add_clean} the product you wish to add to {selected_product_line}?")

        # if input is confirmed, give option to edit new product's details
        if confirm() == True:
            product_lines[selected_product_line][product_to_add_clean] = {}
            print(f"{product_to_add_clean} has been added to {selected_product_line}. \n"
            f"Would you like to edit {product_to_add_clean} details now?")
            yes_or_no = input("Please enter yes or no.")
            yes_or_no_clean = yes_or_no.strip().lower()

            # if user enters 'no', exit loop
            if yes_or_no_clean == "no":
                print("Have a nice day.")
                return

            # if user enters 'yes', take to edit product details
            elif yes_or_no_clean == "yes":
                edit_product_details()
                return # exits after user edits the product details

            # if user enters something other than 'yes' or 'no', raise error and take back to start of loop
            else: 
                print("Invalid input. Please try again.")

        # if input is noted as incorrect, send back to top of loop to try again
        else:
            continue
            

def remove_product():
    # Asks users to choose a product line they would like to remove a product from 
    while True:
        try: 
            print("Please select which product line you would like to remove a product from.")
            product_line_list = list(product_lines.keys())

            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")
                
            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index - 1]
            
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue

        # ONLY runs if try succeeds
        # Asks user to confirm choice
        print(f"Is {selected_product_line} the correct product line?")
        if confirm() == True:
            break
        else: 
            print("Please enter correct product line.")
            continue

    # Prints products under that product line
    while True: 
        try:
            print(f"Please select which product under {selected_product_line} you would like to delete.")
            product_list = list(product_lines[selected_product_line].keys())
            for i, product in enumerate(product_list, 1):
                print(f" {i}:{product}")
            choice_index = int(input("Please input the number of your selection"))
            selected_product = product_list[choice_index - 1]
            
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue

        # Asks user to confirm selection 
        print(f"Is {selected_product} the correct product?")

        # if user confirms, selected product is deleted 
        if confirm() == True:
            del product_lines[selected_product_line][selected_product]
            print(f"{selected_product.title()} has been deleted.")
            return
        else: 
            print("Please enter the correct product you wish to delete.")
            continue # takes back to start of loop to try again

            
def edit_product_name():
    # Asks for product line and confirms with user entered product line is correct
    while True:
        product_line_name = input("Please enter product line name that the product you would like to edit is under.")
        product_line_name_clean = product_line_name.strip().lower()
        # If product line not in entered product line list, gives error and asks to try again.
        if product_line_name_clean not in product_lines:
            print("That product line doesn't exist. Please try again.")
            continue

        # Asks for confirmation on product line name 
        print(f"Is {product_line_name_clean} correct?")
        
        # Continue with rest of code if confirmed
        if confirm() == True:
            break

    while True:
        try:
            # Gives list of products under selected product line for user to select from
            print(f"Please select which product under {product_line_name_clean} you would like to edit.")
            product_list = list(product_lines[product_line_name_clean].keys())
            for i, product in enumerate(product_list, 1):
                print(f" {i}:{product}")
            choice_index = int(input("Please input the number of your selection"))
            selected_product = product_list[choice_index - 1]
            
        # Loops back if user doesn't enter a number
        except (ValueError, IndexError):
            print("Please enter a number.")
            continue

        # Asks user to confirm selection 
        print(f"Is {selected_product} the product you wish to edit?")
        if confirm() == True:
            break # continues with next bit of code
        else: 
            continue # Repeats code to allow user to retry

    # Asks user what they want to replace with
    new_product_name = input(f"Please enter the product name you would like to replace {selected_product} with.")

    # Asks user to confirm selection
    while True:    
        print(f"Is {new_product_name} what you want to replace {selected_product} with?")
        if confirm() == True: 
            # Changes the product's name
            product_lines[product_line_name_clean][new_product_name] = \
            product_lines[product_line_name_clean].pop(selected_product)
            print(f"The product name of {new_product_name} has been saved.")
            break
        else:
            print("Please try again.")
            new_product_name = input(f"Please enter your new product name to replace {selected_product}.")

            


# In[2]:


# Still need to add confirmation checks before saving the product details

def add_product_details():
    # Asks user to choose product line from list
    while True: 
        try:
            print("Please select which product line the product you would like to add details is under.")
            product_line_list = list(product_lines.keys())

            # Gives user list of product lines to select from 
            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")

            # Asks user for selection from product line list
            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index -1]

        # If entered product line is not an integer or exceeds range, raises error and asks user to try again (loops)    
        except (ValueError, IndexError): 
            print("Please enter a valid input from the list.")
            continue

        # Prints selected product line
        print(f"Is {selected_product_line} the product line you would like to add product details to?")

        # Asks user to confirm selected product line choice
        if confirm() == True:
            break # moves on to next code
        else: 
            print("Please try again.") # Loops back to try again

    # Asks user to choose product from chosen product line's product list
    while True: 
        try:
            print(f"Please select which product you would like to add details to under the {selected_product_line}'s products.")
            product_list = list(product_lines[selected_product_line].keys())

            # Gives user a list of products from selected product line to choose from 
            for i, product in enumerate(product_list, 1):
                print(f"{i}: {product}")

            # Asks user to select number of product 
            choice_index = int(input("Please input the number of your selection: "))
            selected_product = product_list[choice_index - 1]

        # If user enters a non-integer or an integer out of range, gives error and asks to try again
        except (ValueError, IndexError): 
            print("Please enter a valid input from the list.")
            continue # loops to allow user to try again

        # Prints user's choice to ask for confirmation 
        print(f"Is {selected_product} the product you want to add details to?")
        if confirm() == True:
            break # moves on to next code
        else:
            print("Please try again.") # loops back to try again


    # Asks user to input product id number or skip. Skip stores id number as none. 
    while True: 
        product_id_input = input("Please enter the product id number or enter 'skip'.")
        if product_id_input.lower().strip() == "skip":
            product_id = None
            break
        # raises an error if entered product id is not an error. Loops to try again
        try:
            product_id = int(product_id_input)
            break # if product id is an integer, exits loop 
        except ValueError:
            print("Please enter an integer for the product id or skip.")

    # Asks user to confirm the product id number
    if product_id is not None:
        print(f"Is entered {product_id} correct.") 
        while True:
            try:
                if confirm() == True:
                    break # if confirmed, moves on to ask for sku number 
                else: 
                    print("Please try again.")
                    product_id = int(input("Please enter product id.")) # loops back to try again

            except ValueError:
                print("Please enter an integer.") #if not an integer, raises error and loops back to try again
            
    # Asks user to input sku number or skip. Skip stores sku as none
    while True: 
        sku_input = input("Please enter the sku number of this product or enter 'skip'.")
        if sku_input.lower().strip() == "skip":
            sku = None
            break # ends loop and stores sku as None
        try: 
            sku = int(sku_input)
            break # if sku is an integer, breaks out of loop
        except ValueError: 
            print("Please enter an integer for the sku number or skip.") # if sku isn't an integer, raises error, and loops to try again

    # Asks user to confirm the sku number
    if sku is not None:
        print(f"Is entered {sku} correct.") 
        while True:
            try:
                if confirm() == True:
                    break # if confirmed, ends loop
                # if not confirmed, asks user for correct sku
                else: 
                    print("Please try again.")
                    sku = int(input("Please enter product id.")) 

            except ValueError:
                print("Please enter an integer.") # raises an error if entered sku isn't an integer. Loops to try again

    # Asks user to input price or skip. Skip stores price as none. 
    while True: 
        price_input = input("Please enter the price of this product or enter 'skip'.")
        if price_input.lower().strip() == "skip":
            price = None # if price is entered as skip, stores price as none and ends loop
            break 
        try:
            price = float(price_input) 
            break # if price is entered as a decimal, ends loop
        except ValueError: 
            print("Please enter a decimal for the price or skip.") # if price isn't entered as a loop, raises error, and allows user to try again

    # Asks user to confirm the price
    if price is not None:
        print(f"Is entered {price} correct.") 
        while True:
            try:
                if confirm() == True:
                    break # if price is confirmed, ends loop
                # if not confirmed, asks user to enter correct price
                else: 
                    print("Please try again.")
                    price = float(input("Please enter price.")) 
                    
            except ValueError:
                print("Please enter an decimal.") # raises error if not a decimal value and allows user to try again


    # Asks user to input the quantity on hand of the product or skip. Skip stores quantity as none. 
    while True: 
        quantity_input = input("Please enter the quantity on hand of this product or enter 'skip'.")
        if quantity_input.lower().strip() == "skip":
            quantity = None # if quantity is entered as skip, stores as none, and ends loop
            break
        try: 
            quantity = int(quantity_input)
            break # if quantity is entered as an integer, moves on to next code
        except ValueError:
            print("Please enter an integer for the quantity on hand or skip.") # if not entered as integer, raises error, and allows user to try again

    # Asks user to confirm the quantity on hand
    if quantity is not None:
        print(f"Is entered {quantity} correct.") 
        while True:
            try:
                # if confirmed, ends loop
                if confirm() == True:
                    break
                # if not confirmed, asks user to try again
                else: 
                    print("Please try again.")
                    quantity = int(input("Please enter quantity."))

            # raises an error if entered value isn't an integer and allows user to try again
            except ValueError:
                print("Please enter an integer.")

    # Asks user to input the reorder level (1-10) of the product. Skip stores reorder level as not determined. 
    # 1 is low, 10 is highest
    while True:
        reorder_input = input("Enter reorder level (1-10) or 'skip'")
        reorder_input_clean = reorder_input.lower().strip()

        # if reorder value is entered as skip, store as none, and end loop
        if reorder_input_clean == "skip":
            reorder_level = None
            break

        try:
            reorder_level = int(reorder_input)

            # ensures reorder level is between 1 and 10
            if 1 <= reorder_level <= 10:
                break # if reorder level is between 1 and 10, moves on to next part of code
            else:
                print("Please enter a number from 1 to 10.") # if not, asks user to try again

        except ValueError:
            print("Please enter a valid integer or 'skip'.") # if not an integer, asks user to try again

    # Asks user to confirm reorder level
    if reorder_level is not None:
        while True:
            print(f"Is entered {reorder_level} correct?")

            # if reorder level is confirmed, moves onto next part of code
            if confirm():
                break

            # if not confirmed, asks user to try again
            else:
                print("Please try again.")

            try:
                # checks for same parameters as before (must be an integer between 1 and 10)
                reorder_level = int(input("Please enter reorder value (1–10): "))
                if not (1 <= reorder_level <= 10):
                    print("Must be 1–10.")
            except ValueError:
                print("Please enter an integer.")

    # Asks user to input supplier name or skip 
    supplier_input = input("Please enter the supplier of this product or enter 'skip'.")
    if supplier_input.lower().strip() == "skip":
        supplier = None # if supplier is entered as skip, stores as none, and moves onto next part of code
    else:
        supplier = str(supplier_input)

    # Asks user to confirm the supplier name
    if supplier is not None:
        while True:
            print(f"Is entered {supplier} correct.") 

            if confirm() == True:
                break # if supplier is confirmed, moves onto next part of code
                
            # if not confirmed, asks user to try again
            else: 
                print("Please try again.")
                supplier = input("Please enter supplier.")

    # Stores the inputs in the designated product dictionary for future reference
    product_lines[selected_product_line][selected_product]["product_id"] = product_id
    product_lines[selected_product_line][selected_product]['sku'] = sku
    product_lines[selected_product_line][selected_product]['price'] = price
    product_lines[selected_product_line][selected_product]['quantity'] = quantity 
    product_lines[selected_product_line][selected_product]['supplier'] = supplier
    product_lines[selected_product_line][selected_product]['reorder_level'] = reorder

    # Stores current time as time last updated
    product_lines[selected_product_line][selected_product]['last_updated'] = get_current_timestamp()

def remove_product_details():
    # Asks user to choose product line from list
    while True: 
        try:
            print("Please select which product line the product you would like to remove details is from.")
            product_line_list = list(product_lines.keys())

            for i, product_line in enumerate(product_line_list, 1):
                print(f"{i}: {product_line}")

            choice_index = int(input("Please input the number of your selection: "))
            selected_product_line = product_line_list[choice_index -1]
            break
        except (ValueError, IndexError): 
            print("Please enter a valid input from the list.")

    # Asks user to confirm choice
    while True:
        print(f"Is {selected_product_line} correct?")
        if confirm() == True:
            break
        else:
            print("Please select again.")

    # Asks user to choose product from chosen product line's product list
    while True: 
        try:
            print(f"Please select which product you would like to remove details to under the {selected_product_line}'s products.")
            product_list = list(product_lines[selected_product_line].keys())
    
            for i, product in enumerate(product_list, 1):
                print(f"{i}: {product}")

            choice_index = int(input("Please input the number of your selection: "))
            selected_product = product_list[choice_index - 1]
            
        except (ValueError, IndexError): 
            print("Please enter a valid input from the list.")
            continue

    # Asks user to confirm selection
        print(f"Is {selected_product} the product you wish to delete details from?")
        if confirm() == True:
            break

        else:
            print("Please select again.")

    # Displays previously entered information for product
    while True:
        try:
            fields = list(product_lines[selected_product_line][selected_product].keys())

            print("\nWhat information would you like to view?")
            for i, field in enumerate(fields, start=1):
                print(f"{i}. {field}")

            choice = int(input("Enter the number of what you would like to delete: "))

            selected_field = fields[choice - 1]

        except (ValueError, IndexError):
            print("Please enter a valid input from the list.")
            continue

        # Asks user to confirm selection
        print(f"You selected {product_lines[selected_product_line][selected_product][selected_field]}. Is this what you want to delete?")

        if confirm() == True:
            break

        else: 
            print("Please try again.")

    # Deletes selected part of product details
    del product_lines[selected_product_line][selected_product][selected_field]

    # Saves deletion
    # Asks if user wants to delete more

def edit_product_details():
    pass


# In[ ]:


def update_inventory()


# In[ ]:


def show_best_sellers()


# In[ ]:


# CLI menu 
def main_menu():
    while True:
        print("Inventory Management Menu")
        print("1. Adjust product line")
        print("2. Adjust product")
        print("3. Update inventory")
        print("4. Show best sellers")
        print("5. Exit")

        choice = input("Enter the number of what you would like to do.")

        # Gives options for adjusting product line
        if choice == "1":
            while True:
                product_line_choice = input("Would you like to add, remove or edit a product line? Or type back to return to menu.")
                product_line_choice_clean = product_line_choice.strip().lower()
                if product_line_choice_clean == "add":
                    add_product_line()
                elif product_line_choice_clean == "remove":
                    remove_product_line()
                elif product_line_choice_clean == "edit":
                    edit_product_line_()
                elif product_line_choice_clean == "back":
                    break # Exits sub menu and goes back to main menu
                else: 
                    print("Please enter 'add', 'remove', or 'edit'")

        # Gives options for adjusting product
        elif choice == "2":
            while True:
                product_choice = input("Would you like to add, remove, or edit a product? Or type back to return to the main menu.")
                product_choice_clean = product_choice.strip().lower()
                if product_choice_clean == "add":
                    add_product()
                elif product_choice_clean == "remove":
                    remove_product()
                elif product_choice_clean == "edit":
                    choice = input("Would like to edit product name or details. Please enter 'name' or 'details'")
                    choice_clean = choice.strip().lower()
                    if choice_clean == "name":
                        edit_product_name()
                    elif choice_clean == "details":
                        edit_product_details()
                    else:
                        print("Invalid input. Try again.")
                        continue
                elif product_choice_clean == "back":
                    break # Exits sub menu and goes back to main menu
                else:
                    print("Please enter 'add', 'remove', or 'edit'")

        # Takes user to sub menu to update inventory
        elif choice == "3":
            update_inventory()

        # Shows user best sellers
        elif choice == "4":
            show_best_sellers()

        # Exits the menu
        elif choice == "5":
            print("Have a nice day.")
            break

        # Loops back to the main menu if user enters an invalid input         
        else:
            print("Invalid choice. Please try again.")
            
main_menu() # Runs the main menu


# In[ ]:




